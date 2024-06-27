import pickle

from typing import Dict, Any, List, Callable
from cama.memory import WorkingMemory, EpisodicMemory

from cama.representation import get_dataset_representation, ToolRepresentation
from cama.prompts import get_prompt_for_explanation, get_overview_report_prompt
from langgraph.graph import StateGraph, END
from rich import print
from time import sleep
from rich.panel import Panel
from rich.text import Text
from rich.markdown import Markdown
from cama.insight import DeepInsight, FeatureInsight, QuickInsight
from docarray import DocList
from langchain_groq import ChatGroq
from cama.utils import print_function_name
from dotenv import load_dotenv
from langgraph.graph import Graph

load_dotenv('env')
# llm = ChatGroq(cache=False, temperature=0.0, model_name="llama3-8b-8192") #GPT-4, GPT-3.5, Openchat, Starling, phi-2, 
llm = ChatGroq(cache=False, temperature=0.0, model_name="llama3-70b-8192")

def episodic_memory_classify(last_episode: EpisodicMemory) -> int:


    if last_episode.task == 0:
        return 0 # Empty memory. Original task
    else:
        # Here we can add logic to classify the current task based on the episodic memory
        task = 1

        return task # Insight was found
    
    # return task


def episodic_memory_retriever(state: WorkingMemory) -> WorkingMemory:
    # Logic to retrieve training data, metadata, model

    state['found_insight'] = False
    episodic_memory = state['episodic_memory']

    task = episodic_memory_classify(episodic_memory[-1])
    

    if task >= 1:
        state['found_insight'] = True
        episodic_memory[-1].task = task
        # retrieved_em = [em for em in episodic_memory if em.task == task] 
        state['deep_insight_output'] = episodic_memory[-1].deep_insight_output
        
    return state


def episodic_memory_condition(state: WorkingMemory) -> str:

    
    if state['found_insight']:
        print("Insight was found. Returning retrieved insights.")
        return 'end' 
    else:
        print("Insight was not found. Proceeding with fast tools.")
        return 'fast_tools' 


def fast_tools_node(state: WorkingMemory) -> WorkingMemory:
    
    
    episodic_memory = state['episodic_memory']
    semantic_memory = state['semantic_memory']

    tools_results_ = DocList[ToolRepresentation]()
    print("Calculating drift report")
    tool_name = 'get_drift_report'
    get_drift_report_function = semantic_memory.tools[tool_name].function
    tool_result = get_drift_report_function(semantic_memory.reference_dataset.description, 
                                            semantic_memory.reference_dataset.X_train, 
                                             episodic_memory[-1].current_dataset.X, 0.7)['dataset']
    # tool_description = semantic_memory.tools_description[tool_name]['description']

    # tools_results_.append(ToolRepresentation(name=tool_name, description=tool_description, result=tool_result))
    
    

    state['fast_tools_results'] = tool_result 
    episodic_memory[-1].quick_insight = QuickInsight(dataset_title=semantic_memory.reference_dataset.description['DATASET_TITLE'],
                                                        quick_insight=tool_result['share_of_drifted_columns'])

    state['episodic_memory'] = episodic_memory

    return state

def proxy_condition(state: WorkingMemory) -> str:

    drift_threshold = state['threshold']
    episodic_memory = state['episodic_memory']

    if episodic_memory[-1].quick_insight.quick_insight > drift_threshold:
        print(f"Drift ({episodic_memory[-1].quick_insight.quick_insight}) is greater than threshold ({drift_threshold}). Need for deep insights")
        return 'slow_tools' 
    else:
        print("No need for deep insights")
        return 'end' 


def slow_tools(state: WorkingMemory) -> WorkingMemory:

    episodic_memory = state['episodic_memory']
    semantic_memory = state['semantic_memory']

    X_test_current = episodic_memory[-1].current_dataset.X

    print("Calculating drift report by column")
    tool_name = 'get_drift_report'
    get_drift_report_function = semantic_memory.tools[tool_name].function
    drift_report = get_drift_report_function(semantic_memory.reference_dataset.description, semantic_memory.reference_dataset.X_train, 
                                             episodic_memory[-1].current_dataset.X, 0.7)['drift_by_columns']
    

    print("Calculating SHAP values by column")
    tool_name = 'get_shap_values'
    get_shap_values_report_function = semantic_memory.tools[tool_name].function

    shap_report_train_reference = get_shap_values_report_function(semantic_memory.model, semantic_memory.reference_dataset.X_train, semantic_memory.reference_dataset.description)
    shap_report_test_current = get_shap_values_report_function(semantic_memory.model, X_test_current, semantic_memory.reference_dataset.description)

    shap_report = {feature: {'reference': shap_report_train_reference[feature], 'current': shap_report_test_current[feature]} for feature in shap_report_train_reference}


    state['slow_tools_results'] = {'get_drift_report': drift_report, 'get_shap_values': shap_report}
    
    return state

def refactor(state: WorkingMemory) -> WorkingMemory:
    # create the dataset_representation

    dataset_representation = get_dataset_representation(state['semantic_memory'],
                                                         state['slow_tools_results'])
    state['dataset_representation'] = dataset_representation
    
    return state


def break_down(state: WorkingMemory) -> WorkingMemory:

    list_outputs = list()
    # Iterate over all the features and generate the explanation
    for index, feature in enumerate(state['dataset_representation'].features):
        feature_name = feature.name
        input_message = feature.as_dict()
        input_dict = {"input": input_message, 'feature_name': feature_name, 
                      'dataset_title': state['dataset_representation'].name,
                      'dataset_description': state['dataset_representation'].description}

        final_prompt = get_prompt_for_explanation(state['semantic_memory'])
        chain = final_prompt | llm
        output = chain.invoke(input_dict)
        text = Text(f"Feature: {feature_name}", justify="left", style="bold yellow")
        panel = Panel(text)
        print(panel)
        print(output.content)
        # display(Markdown(output.content))
        print("\n", "="*100, "\n")

        # sleep(2)

        list_outputs.append({'feature': feature_name,  'report': output.content})

        # break

    # add the list_outputs to the episodic memory deep insight output  
    state['generations']['feature_reports'] = list_outputs 

    return state

def compile_(state: WorkingMemory) -> WorkingMemory:
    dataset_representation = state['dataset_representation']
    feature_outputs = state['generations']['feature_reports']


    overview_report_prompt = get_overview_report_prompt(dataset_representation, feature_outputs)
    chain = overview_report_prompt | llm
    overview_output = chain.invoke({})
    overview_report = overview_output.content

    state['generations']['overview_report'] = overview_report

    dataset_title = state['semantic_memory'].reference_dataset.description['DATASET_TITLE']
    dataset_description = state['semantic_memory'].reference_dataset.description['DATASET_DESCRIPTION']

    feature_reports = DocList([FeatureInsight(feature=d['feature'], insight=d['report'])
                               for d in feature_outputs])


    # Create and return the final report
    final_report = DeepInsight(
        dataset_title=dataset_title,
        dataset_description=dataset_description,
        overview=overview_report,
        feature_insights=feature_reports,
        # conclusion=conclusion_report
    )

    state['episodic_memory'][-1].deep_insight = final_report
    text = Text(f"Final report", justify="left", style="bold green")
    panel = Panel(text)
    print(panel)
    print(final_report.generate_markdown_report())
    
    return state

class EnhancedStateGraph(StateGraph):
    def add_node(self, node_name, function):
        # Decorate the function with the decorator
        decorated_function = print_function_name(function)
        # Call the original add_node with the decorated function
        super().add_node(node_name, decorated_function)

graph = EnhancedStateGraph(WorkingMemory)
# graph = StateGraph(WorkingMemory)

# Add nodes
graph.add_node('episodic_memory_retriever', episodic_memory_retriever)
graph.add_node('fast_tools', fast_tools_node)

# graph.add_node('semantic_memory_retriever', semantic_memory_retriever)
graph.add_node('slow_tools', slow_tools)

graph.add_node('refactor', refactor)
graph.add_node('break down', break_down)
# graph.add_node('explain', split)
graph.add_node('compile', compile_)


graph.add_conditional_edges('episodic_memory_retriever', episodic_memory_condition, {
    'fast_tools': 'fast_tools',
    'end': END,
})

graph.add_conditional_edges('fast_tools', proxy_condition, {
    'slow_tools': 'slow_tools',
    'end': END,
})


# graph.add_edge('semantic_memory_retriever', 'slow_tools')
graph.add_edge('slow_tools', 'refactor')
# graph.add_edge('semantic_memory_retriever', 'fusion')


graph.add_edge('refactor', 'break down')
graph.add_edge('break down', 'compile')

# graph.add_edge('type_1_tools', 'llm')
# graph.add_edge('llm', 'hotl')
graph.add_edge('compile', END)
# graph.add_edge('hotl', 'deep_insight')
# graph.add_edge('deep_insight', END)

# Set entry and finish points
graph.set_entry_point('episodic_memory_retriever')
# graph.set_finish_point('deep_insight')

# Compile the graph
agent_graph = graph.compile(debug=False)


