
import pickle
from typing import Dict, Any, List, Callable
from cama.memory import WorkingMemory, EpisodicMemory
from cama.representation import get_dataset_representation, ToolRepresentation
from cama.prompts import get_overview_report_prompt
from cama.prompts import get_prompt_for_feature_explanation
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
from langfuse.callback import CallbackHandler
from langchain_core.messages import AIMessage
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import json


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
    

    def process_feature(self, feature, dataset_info: Dict, llm):
        feature_info = feature.as_dict()
        final_prompt = get_prompt_for_feature_explanation(feature_info, dataset_info)
        chain = final_prompt | llm
        output = chain.invoke({})
        sleep(0.1)  # Keep the sleep if it's necessary for rate limiting
        
        text = Text(f"Feature: {feature_info['name']}", justify="left", style="bold yellow")
        panel = Panel(text)
        print(panel)
        print(output.content)
        print("\n", "="*100, "\n")
        
        return {'feature': feature_info['name'], 'report': output.content}
    
    def break_down(self, state: WorkingMemory) -> WorkingMemory:
        dataset_info = {
            'dataset_title': state['dataset_representation'].name,
            'dataset_description': state['dataset_representation'].description
        }
        
        # Process features in parallel
        with ThreadPoolExecutor() as executor:
            future_to_feature = {
                executor.submit(self.process_feature, feature, dataset_info, self.llm): feature
                for feature in state['dataset_representation'].features
            }
            
            list_outputs = []
            for future in as_completed(future_to_feature):
                list_outputs.append(future.result())

        state['generations']['feature_reports'] = list_outputs

        # Process label
        label_info = state['dataset_representation'].label.as_dict()
        label_prompt = get_prompt_for_label_explanation(label_info, dataset_info)
        label_chain = label_prompt | self.llm
        label_output = label_chain.invoke({})
        text = Text(f"Label: {label_info['name']}", justify="left", style="bold yellow")
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


        # Overview report generation
        # print("waiting for 1 seconds to avoid rate limiting")
        # sleep(1)
        sleep(0.01)
        
        overview_start = time.time()
        overview_report_prompt = get_overview_report_prompt(dataset_representation, feature_outputs, label_report)
        chain = overview_report_prompt | self.llm
        # overview_output = chain.invoke({})
        # overview_report = overview_output.content
        overview_report = "Overview report"
        state['generations']['overview_report'] = overview_report
        overview_end = time.time()
        print(f"Overview report generation took {overview_end - overview_start:.4f} seconds")


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
        # langfuse_handler = CallbackHandler()
        for output in self.decision_procedure.stream(initial_state):
            for node_name, state in output.items():
                skip_keys = ['semantic_memory', 'slow_tools_results', 'fast_tools_results']
                # print("State: ", {k: value for k, value in state.items() if k not in skip_keys})

        return output
    
    def run_batch(self, initial_state: WorkingMemory):
        output = self.decision_procedure.invoke(initial_state)
        
        return output

class EnhancedStateGraph(StateGraph):
    def add_node(self, node_name, function):
        decorated_function = print_function_name(function)
        super().add_node(node_name, decorated_function)

