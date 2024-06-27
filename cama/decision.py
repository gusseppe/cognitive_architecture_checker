
import pickle
from typing import Dict, Any, List, Callable
from cama.memory import WorkingMemory, EpisodicMemory
from cama.representation import get_dataset_representation, ToolRepresentation
from cama.prompts import get_prompt_for_explanation, get_overview_report_prompt
from langgraph.graph import StateGraph, END
from rich import print
from rich.panel import Panel
from rich.text import Text
from rich.markdown import Markdown
from cama.insight import DeepInsight, FeatureInsight, QuickInsight
from docarray import DocList
from cama.utils import print_function_name
from cama.prompts import get_prompt_for_label_explanation
from time import sleep

class DecisionProcedure:
    def __init__(self, llm, debug=False):
        self.llm = llm
        self.graph = EnhancedStateGraph(WorkingMemory)
        self.build_plan()
        self.decision_procedure = self.graph.compile(debug=debug)

    def build_plan(self):
        # Add nodes
        self.graph.add_node('episodic_memory_retriever', self.episodic_memory_retriever)
        self.graph.add_node('fast_tools', self.fast_tools_node)
        self.graph.add_node('slow_tools', self.slow_tools)
        self.graph.add_node('refactor', self.refactor)
        self.graph.add_node('break_down', self.break_down)
        self.graph.add_node('compile', self.compile_)

        # Add conditional edges
        self.graph.add_conditional_edges('episodic_memory_retriever', self.episodic_memory_condition, {
            'fast_tools': 'fast_tools',
            'end': END,
        })
        self.graph.add_conditional_edges('fast_tools', self.proxy_condition, {
            'slow_tools': 'slow_tools',
            'end': END,
        })

        # Add direct edges
        self.graph.add_edge('slow_tools', 'refactor')
        self.graph.add_edge('refactor', 'break_down')
        self.graph.add_edge('break_down', 'compile')
        self.graph.add_edge('compile', END)

        # Set entry and finish points
        self.graph.set_entry_point('episodic_memory_retriever')

    def episodic_memory_classify(self, last_episode: EpisodicMemory) -> int:
        if last_episode.task == 0:
            return 0  # Empty memory. Original task
        else:
            task = 1
            return task  # Insight was found

    def episodic_memory_retriever(self, state: WorkingMemory) -> WorkingMemory:
        state['found_insight'] = False
        episodic_memory = state['episodic_memory']
        task = self.episodic_memory_classify(episodic_memory[-1])
        if task >= 1:
            state['found_insight'] = True
            episodic_memory[-1].task = task
            state['deep_insight_output'] = episodic_memory[-1].deep_insight_output
        return state

    def episodic_memory_condition(self, state: WorkingMemory) -> str:
        if state['found_insight']:
            print("Insight was found. Returning retrieved insights.")
            return 'end' 
        else:
            print("Insight was not found. Proceeding with fast tools.")
            return 'fast_tools'

    def fast_tools_node(self, state: WorkingMemory) -> WorkingMemory:
        episodic_memory = state['episodic_memory']
        semantic_memory = state['semantic_memory']
        tools_results_ = DocList[ToolRepresentation]()
        print("Calculating drift report")
        tool_name = 'get_drift_report'
        get_drift_report_function = semantic_memory.tools[tool_name].function
        tool_result = get_drift_report_function(
            semantic_memory.reference_dataset.description, 
            semantic_memory.reference_dataset.X_train, 
            episodic_memory[-1].current_dataset.X, 0.7
        )['dataset']
        state['fast_tools_results'] = tool_result
        episodic_memory[-1].quick_insight = QuickInsight(
            dataset_title=semantic_memory.reference_dataset.description['DATASET_TITLE'],
            quick_insight=tool_result['share_of_drifted_columns']
        )
        state['episodic_memory'] = episodic_memory
        return state

    def proxy_condition(self, state: WorkingMemory) -> str:
        drift_threshold = state['threshold']
        episodic_memory = state['episodic_memory']
        if episodic_memory[-1].quick_insight.quick_insight > drift_threshold:
            print(f"Drift ({episodic_memory[-1].quick_insight.quick_insight}) is greater than threshold ({drift_threshold}). Need for deep insights")
            return 'slow_tools'
        else:
            print("No need for deep insights")
            return 'end'

    def slow_tools(self, state: WorkingMemory) -> WorkingMemory:
        episodic_memory = state['episodic_memory']
        semantic_memory = state['semantic_memory']
        X_test_current = episodic_memory[-1].current_dataset.X
        print("Calculating drift report by column")
        tool_name = 'get_drift_report'
        get_drift_report_function = semantic_memory.tools[tool_name].function
        drift_report = get_drift_report_function(
            semantic_memory.reference_dataset.description, 
            semantic_memory.reference_dataset.X_train, 
            episodic_memory[-1].current_dataset.X, 0.7
        )['drift_by_columns']
        print("Calculating SHAP values by column")
        tool_name = 'get_shap_values'
        get_shap_values_report_function = semantic_memory.tools[tool_name].function
        shap_report_train_reference = get_shap_values_report_function(
            semantic_memory.model, semantic_memory.reference_dataset.X_train, 
            semantic_memory.reference_dataset.description
        )
        shap_report_test_current = get_shap_values_report_function(
            semantic_memory.model, X_test_current, 
            semantic_memory.reference_dataset.description
        )
        shap_report = {feature: {
            'reference': shap_report_train_reference[feature], 
            'current': shap_report_test_current[feature]
        } for feature in shap_report_train_reference}
        state['slow_tools_results'] = {'get_drift_report': drift_report, 'get_shap_values': shap_report}
        return state

    def refactor(self, state: WorkingMemory) -> WorkingMemory:
        dataset_representation = get_dataset_representation(state['semantic_memory'], state['slow_tools_results'])
        state['dataset_representation'] = dataset_representation
        return state

    def break_down(self, state: WorkingMemory) -> WorkingMemory:
        list_outputs = list()

        # Process the features
        for index, feature in enumerate(state['dataset_representation'].features):
            feature_name = feature.name
            input_message = feature.as_dict()
            input_dict = {
                "input": input_message, 
                'feature_name': feature_name, 
                'dataset_title': state['dataset_representation'].name,
                'dataset_description': state['dataset_representation'].description
            }
            final_prompt = get_prompt_for_explanation(state['semantic_memory'])
            chain = final_prompt | self.llm
            output = chain.invoke(input_dict)
            sleep(1)
            text = Text(f"Feature: {feature_name}", justify="left", style="bold yellow")
            panel = Panel(text)
            print(panel)
            print(output.content)
            print("\n", "="*100, "\n")
            list_outputs.append({'feature': feature_name, 'report': output.content})
            
        

        state['generations']['feature_reports'] = list_outputs

        # Process label
        label = state['dataset_representation'].label
        input_message = label.as_dict()
        input_dict = {
            "input": input_message,
            'label_name': label.name,
            'dataset_title': state['dataset_representation'].name,
            'dataset_description': state['dataset_representation'].description
        }
        label_prompt = get_prompt_for_label_explanation(state['semantic_memory'])
        label_chain = label_prompt | self.llm
        label_output = label_chain.invoke(input_dict)
        text = Text(f"Label: {label.name}", justify="left", style="bold yellow")
        panel = Panel(text)
        print(panel)
        print(label_output.content)
        print("\n", "="*100, "\n")
        
        state['generations']['label_report'] = label_output.content

        
        return state

    def compile_(self, state: WorkingMemory) -> WorkingMemory:
        dataset_representation = state['dataset_representation']
        feature_outputs = state['generations']['feature_reports']
        label_report = state['generations'].get('label_report', "No specific report available for the label.")
        overview_report_prompt = get_overview_report_prompt(dataset_representation, feature_outputs, label_report)
        chain = overview_report_prompt | self.llm
        overview_output = chain.invoke({})
        overview_report = overview_output.content
        state['generations']['overview_report'] = overview_report
        dataset_title = state['semantic_memory'].reference_dataset.description['DATASET_TITLE']
        dataset_description = state['semantic_memory'].reference_dataset.description['DATASET_DESCRIPTION']

        feature_reports = DocList([FeatureInsight(feature=d['feature'], insight=d['report']) for d in feature_outputs])
        final_report = DeepInsight(
            dataset_title=dataset_title,
            dataset_description=dataset_description,
            overview=overview_report,
            feature_insights=feature_reports,
            label_insight=label_report
        )
        state['episodic_memory'][-1].deep_insight = final_report
        text = Text(f"Final report", justify="left", style="bold green")
        panel = Panel(text)
        print(panel)
        print(final_report.generate_markdown_report())
        return state

    def run(self, initial_state: WorkingMemory):
        for output in self.decision_procedure.stream(initial_state):
            for node_name, state in output.items():
                skip_keys = ['semantic_memory', 'slow_tools_results', 'fast_tools_results']
                print("State: ", {k: value for k, value in state.items() if k not in skip_keys})

        return output


class EnhancedStateGraph(StateGraph):
    def add_node(self, node_name, function):
        decorated_function = print_function_name(function)
        super().add_node(node_name, decorated_function)

