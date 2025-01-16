import os
import json
from datetime import datetime
from typing import Dict, Any, List
from langsmith import trace, Client
from cama.decision import DecisionProcedure
from cama.memory import WorkingMemory
from cama.utils import save_to_file, load_from_file, load_from_json, escape_curly_braces
from cama.insight import DeepInsight, FeatureInsight, QuickInsight
from docarray import DocList
from langchain_core.prompts import ChatPromptTemplate
from cama.utils import get_answers_from_report_prompt, load_from_json, save_json_to_file, evaluate_answers_with_unknowns, extract_json

client = Client()
project_name = "Checker"

class AblationDecisionProcedure(DecisionProcedure):    
    def __init__(self, llm, debug=False, ablation_config=None):
        super().__init__(llm, debug)
        self.ablation_config = ablation_config or {}

    def refactor(self, state: WorkingMemory) -> WorkingMemory:
        if self.ablation_config.get('remove_refactor', False):
            print("Refactor step removed due to ablation config")
            return state
        return super().refactor(state)

    def break_down(self, state: WorkingMemory) -> WorkingMemory:
        if self.ablation_config.get('remove_break_down', False):
            print("Break down step removed due to ablation config")
            return state
        elif self.ablation_config.get('simplify_break_down', False) or self.ablation_config.get('remove_refactor', False):
            return self.simplify_break_down(state)
        return super().break_down(state)

    def simplify_break_down(self, state: WorkingMemory) -> WorkingMemory:
        semantic_memory = state['semantic_memory']
        dataset_description = semantic_memory.reference_dataset.description
        tools_description = semantic_memory.tools

        system_prompt = f"""
        You are a data scientist analyzing the '{dataset_description['DATASET_TITLE']}' dataset.
        Dataset description: {dataset_description['DATASET_DESCRIPTION']}
        
        Available tools:
        {escape_curly_braces(', '.join(tools_description.keys()))}
        
        Analyze each feature and the label. Provide insights on their characteristics and potential impact on the chronic condition prediction.
        """

        human_prompt = "Analyze the following feature or label: {feature_name}. Description: {feature_description}. Type: {feature_type}. Possible values: {possible_values}."

        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("human", human_prompt),
        ])

        feature_reports = []
        for feature_name in dataset_description['FEATURES'] + [dataset_description['LABEL']]:
            feature_type = 'numerical' if feature_name in dataset_description['NUMERICAL_FEATURES'] else 'categorical'
            feature_description = dataset_description['FEATURE_DESCRIPTIONS'].get(feature_name, dataset_description['LABEL_DESCRIPTION'])
            possible_values = dataset_description['COLUMN_VALUES'].get(feature_name, "Not specified")

            input_dict = {
                'feature_name': feature_name,
                'feature_description': feature_description,
                'feature_type': feature_type,
                'possible_values': possible_values
            }

            chain = prompt | self.llm
            output = chain.invoke(input_dict)

            if feature_name == dataset_description['LABEL']:
                state['generations']['label_report'] = output.content
            else:
                feature_reports.append({'feature': feature_name, 'report': output.content})

        state['generations']['feature_reports'] = feature_reports
        return state

    def compile_(self, state: WorkingMemory) -> WorkingMemory:
        if self.ablation_config.get('remove_compile', False):
            print("Compile step removed due to ablation config")
            return state
        elif self.ablation_config.get('simplify_compile', False) or self.ablation_config.get('remove_refactor', False):
            return self.simplify_compile(state)
        return super().compile_(state)

    def simplify_compile(self, state: WorkingMemory) -> WorkingMemory:
        semantic_memory = state['semantic_memory']
        dataset_description = semantic_memory.reference_dataset.description
        
        feature_reports = state['generations']['feature_reports']
        label_report = state['generations'].get('label_report', "No specific report available for the label.")
        
        system_prompt = f"""
        You are a data scientist summarizing the analysis of the '{dataset_description['DATASET_TITLE']}' dataset.
        Dataset description: {dataset_description['DATASET_DESCRIPTION']}
        
        Provide a concise overview of the dataset based on the feature and label analyses.
        """

        human_prompt = """
        Feature reports:
        {feature_reports}

        Label report:
        {label_report}

        Summarize the key findings and potential implications for chronic condition prediction.
        """

        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("human", human_prompt),
        ])

        input_dict = {
            'feature_reports': '\n'.join([f"{report['feature']}: {report['report']}" for report in feature_reports]),
            'label_report': label_report
        }

        chain = prompt | self.llm
        overview_output = chain.invoke(input_dict)
        overview_report = overview_output.content
        
        state['generations']['overview_report'] = overview_report
        
        dataset_title = dataset_description['DATASET_TITLE']
        dataset_description_text = dataset_description['DATASET_DESCRIPTION']
        
        feature_insights = DocList([FeatureInsight(feature=d['feature'], insight=d['report']) for d in feature_reports])
        final_report = DeepInsight(
            dataset_title=dataset_title,
            dataset_description=dataset_description_text,
            overview=overview_report,
            feature_insights=feature_insights,
            label_insight=label_report
        )
        state['episodic_memory'][-1].deep_insight = final_report
        
        return state

def run_ablation_experiment(ablation_config: Dict[str, bool], working_memory: WorkingMemory, llm_generator: Any, dataset_folder: str) -> Dict[str, Any]:
    decision_procedure = AblationDecisionProcedure(llm_generator, debug=False, ablation_config=ablation_config)
    
    config_name = "_".join([f"{k}_{v}" for k, v in ablation_config.items() if v])
    method_name = f"ablation_{config_name}" if config_name else "baseline"
    
    report_filename = f'{dataset_folder}/report_{method_name}.md'
    metadata_filename = f'{dataset_folder}/metadata_{method_name}.json'
    
    start_time = datetime.now()
    with trace(method_name, "chain") as rt:
        output = decision_procedure.run_batch(working_memory)
        rt.end(outputs={'output': output})
    end_time = datetime.now()
    elapsed_time = end_time - start_time
    
    last_episodic_memory = output['episodic_memory'][-1]
    report = last_episodic_memory.deep_insight.generate_markdown_report()
    save_to_file(report, report_filename)
    
    tool_runs = client.list_runs(
        project_name=project_name,
        run_type="chain",
        select=["trace_id", "name", "total_tokens"],  
        filter=f'or(eq(name, "{method_name}"))',
        is_root=1,
        limit=1,
    )
    
    metadata = {
        "trace_id": None,
        "name": method_name,
        "total_tokens": 0,
        "elapsed_time": elapsed_time.total_seconds(),
        "ablation_config": ablation_config
    }
    
    for run in tool_runs:
        metadata.update({
            "trace_id": str(run.trace_id),
            "name": run.name,
            "total_tokens": run.total_tokens,
        })
        break
    
    with open(metadata_filename, 'w') as f:
        json.dump(metadata, f)
    
    return metadata

def run_all_ablation_experiments(working_memory: WorkingMemory, llm_generator: Any, dataset_folder: str) -> Dict[str, Dict[str, Any]]:
    ablation_configs = [
        {},  # Baseline
        {'remove_refactor': True},
        {'remove_break_down': True},
        {'simplify_break_down': True},
        {'remove_compile': True},
        {'simplify_compile': True},
    ]
    
    results = {}
    for config in ablation_configs:
        config_name = "_".join([f"{k}_{v}" for k, v in config.items()]) if config else "baseline"
        results[config_name] = run_ablation_experiment(config, working_memory, llm_generator, dataset_folder)
    
    return results

def analyze_ablation_results(results: Dict[str, Dict[str, Any]], dataset_folder: str, qa_list: List[Dict[str, str]], llm_name: str, openai_llm) -> None:
    print("Ablation Study Results:")
    print("----------------------")
    
    baseline = results['baseline']
    baseline_time = baseline['elapsed_time']
    baseline_tokens = baseline['total_tokens']
    
    accuracy_results = {}
    
    for config, data in results.items():
        if config == 'baseline':
            continue
        
        time_diff = data['elapsed_time'] - baseline_time
        token_diff = data['total_tokens'] - baseline_tokens
        
        print(f"\nConfiguration: {config}")
        print(f"Execution time: {data['elapsed_time']:.2f}s ({time_diff:+.2f}s compared to baseline)")
        print(f"Total tokens: {data['total_tokens']} ({token_diff:+d} compared to baseline)")
        
        # Calculate accuracy
        report_filename = f'{dataset_folder}/report_ablation_{config}.md'
        answers_filename = f'{dataset_folder}/answers_ablation_{config}_{llm_name}.json'
        
        if os.path.exists(report_filename):
            with open(report_filename, 'r') as f:
                report = f.read()
            
            if  os.path.exists(answers_filename):
                print(f"Generating answers for {config}")
                get_answer_prompt = get_answers_from_report_prompt(report, qa_list)
                chain = get_answer_prompt | openai_llm | extract_json
                answers = chain.invoke({})
                save_json_to_file(answers, answers_filename)
            else:
                answers = load_from_json(answers_filename)
            
            accuracy_score, unknown_ratio = evaluate_answers_with_unknowns(qa_list, answers)
            accuracy_results[config] = {
                "accuracy_score": accuracy_score,
                "unknown_ratio": unknown_ratio
            }
            print(f"Accuracy: {accuracy_score:.2f}%")
            print(f"Unknown ratio: {unknown_ratio:.2f}%")
        else:
            print(f"Report file not found for {config}")
    
    print("\nAccuracy Summary:")
    for config, result in accuracy_results.items():
        print(f"{config}: Accuracy = {result['accuracy_score']:.2f}%, Unknown ratio = {result['unknown_ratio']:.2f}%")
    
    print("\nNote: For a complete analysis, manually review the generated reports for each configuration.")
