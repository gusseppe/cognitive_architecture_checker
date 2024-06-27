import json
import operator
import re
import textwrap
from typing import Any, Annotated, Callable, Dict, List, Tuple, Union, Optional, TypedDict, Literal

from rich import print
from rich.panel import Panel
from rich.text import Text

from cama.memory import EpisodicMemory, SemanticMemory
from cama.representation import DatasetRepresentation

from langchain import hub
from langchain.agents import Tool
from langchain_openai import ChatOpenAI

from langchain_core.agents import AgentAction, AgentFinish
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.exceptions import OutputParserException
# from langchain_core.runnables import chain as as_runnable
from langchain_core.pydantic_v1 import BaseModel, Field

from langgraph.graph import END, MessageGraph, StateGraph
from langgraph.prebuilt import ToolInvocation
from langgraph.prebuilt.tool_executor import ToolExecutor
from langchain.tools.render import ToolsRenderer, render_text_description


def print_function_name(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        text = Text(f"Node: {func.__name__}", justify="center", style="bold white")
        panel = Panel(text)
        print(panel)
        return func(*args, **kwargs)
    return wrapper

def escape_curly_braces(text: str) -> str:
    text = str(text)
    return text.replace("{", "{{").replace("}", "}}")


def ground_truth_template(dataset_metadata: Dict[str, Any], 
                                 drift_metrics: Dict[str, Any],
                                 shap_values_training: Dict[str, Any], 
                                 shap_values_current: Dict[str, Any]) -> str:
    # Extract metadata for ease of use
    dataset_title = dataset_metadata['DATASET_TITLE']
    dataset_description = dataset_metadata['DATASET_DESCRIPTION']
    features = dataset_metadata['FEATURES']
    label = dataset_metadata['LABEL']
    feature_descriptions = dataset_metadata['FEATURE_DESCRIPTIONS']
    column_values = dataset_metadata['COLUMN_VALUES']
    column_types = dataset_metadata['COLUMN_TYPES']
    label_description = dataset_metadata['LABEL_DESCRIPTION']

    drift_by_columns = drift_metrics['drift_by_columns']

    # Create markdown sections
    report = textwrap.dedent(f"""
# Comprehensive Report

## Executive Summary

(Here the LLM should provide an executive summary of the report.)

## Dataset Synopsis
**Title**: {dataset_title}  
**Features Analyzed**: {', '.join(features)}
**Label Variable**: {label}  
{dataset_description}

## Label Description
**{label}**: {label_description}
(Here the LLM should provide an explanation if the label has issues or not. Remember that the label was not used in the drift analysis and SHAP values.)

## Feature Analysis
""")

    for feature in features:
        feature_drift = drift_by_columns[feature]
        shap_train_value = shap_values_training[feature]['value']
        shap_train_position = shap_values_training[feature]['position']
        shap_current_value = shap_values_current[feature]['value']
        shap_current_position = shap_values_current[feature]['position']

        report += textwrap.dedent(f"""
### Feature name: {feature}
- **Description**: {escape_curly_braces(feature_descriptions[feature])}
- **Type**: {"Numerical" if feature in dataset_metadata['NUMERICAL_FEATURES'] else "Categorical"}
- **Possible Values**: {escape_curly_braces(column_values[feature])}
- **Data Type**: {escape_curly_braces(column_types[feature])}

#### Distribution Drift Analysis
- **Statistical Test**: {escape_curly_braces(feature_drift['stattest_name'])}
- **Drift Score**: {feature_drift['drift_score']}
- **Detection**: {"Drift detected" if feature_drift['drift_detected'] else "No drift detected"}
- **Current vs. Reference Distribution**:
  - Current: {escape_curly_braces(feature_drift['current'])}
  - Reference: {escape_curly_braces(feature_drift['reference'])}
  - Interpretation: (Here the LLM should provide an interpretation of the current vs reference distribution. Gives examples of the differences.)

#### Feature Attribution Analysis
  - Method: Tree SHAP
  - Training Data: {shap_train_value} (Rank {shap_train_position})
  - Current Data: {shap_current_value} (Rank {shap_current_position})
  - Interpretation: (Here the LLM should provide an interpretation of the current vs reference SHAP values.)

#### Overal Interpretation**: 
  (Here the LLM should provide an overall interpretation for the feature: {feature}.)
""")

    report += """
## Overall Analysis
(Here the LLM should provide an overall analysis of the dataset based on the drift analysis and SHAP values on all the features and label. Gives examples if needed.)
"""
#     for name, effect in shap_values_training.items():
#         report += f"- **{escape_curly_braces(name)}**: {effect['value']:.6f} (Rank {effect['position']})\n"

#     report += """
# ### Current Data SHAP Values (Drifted)
# For the current dataset, where drift has been detected, the SHAP values are:
# """
#     for name, effect in shap_values_current.items():
#         report += f"- **{escape_curly_braces(name)}**: {effect['value']:.6f} (Rank {effect['position']})\n"

#     report += """
# ### Implications of SHAP Value Changes
# (Here the LLM should provide further insights into the implications of these changes.)
# """

    report += textwrap.dedent("""
## Conclusion
(Here the LLM should provide further insights into the conclusion.)
""")

    return report

def get_ground_truth_template(semantic_memory: SemanticMemory, episodic_memory: EpisodicMemory, dataset_representation: DatasetRepresentation) -> str:
    # Extract dataset metadata
    dataset_metadata = {
        'DATASET_TITLE': dataset_representation.name,
        'DATASET_DESCRIPTION': dataset_representation.description,
        'FEATURES': [feature.name for feature in dataset_representation.features],
        'NUMERICAL_FEATURES': [feature.name for feature in dataset_representation.features if feature.type == 'numerical'],
        'CATEGORICAL_FEATURES': [feature.name for feature in dataset_representation.features if feature.type == 'categorical'],
        'LABEL': dataset_representation.label.name,
        'FEATURE_DESCRIPTIONS': {feature.name: feature.description for feature in dataset_representation.features},
        'COLUMN_VALUES': {feature.name: feature.possible_values for feature in dataset_representation.features},
        'COLUMN_TYPES': {feature.name: feature.data_type for feature in dataset_representation.features},
        'LABEL_DESCRIPTION': dataset_representation.label.description
    }

    # Extract drift metrics and SHAP values from dataset_representation
    drift_metrics = {
        'drift_by_columns': {feature.name: feature.tools_results[0].result for feature in dataset_representation.features}
    }

    # print(drift_metrics)
    shap_values_training = {feature.name: feature.tools_results[1].result['reference'] for feature in dataset_representation.features}
    shap_values_current = {feature.name: feature.tools_results[1].result['current'] for feature in dataset_representation.features}

    # Create the comprehensive markdown report
    markdown_report = ground_truth_template(
        dataset_metadata, 
        drift_metrics, 
        shap_values_training, 
        shap_values_current
    )
    
    return markdown_report


def generate_ground_truth_prompt(report: str) -> ChatPromptTemplate:
    system_prompt = textwrap.dedent(f"""
    You are an expert in data science and machine learning. Read the following report and complete it by filling inside the text '(Here the LLM should provide...)' with your explanations. Keep all the remaining text as it is.

    {report}


    """)

    final_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "Think step by step to solve your task. Provide only the raw markdown."),
        ]
    )

    return final_prompt

def save_to_file(gt_report: str, file_path: str) -> None:
    with open(file_path, 'w') as file:
        file.write(gt_report)

    print(f'{file_path} saved successfully')

def save_json_to_file(qa_list: List[Dict[str, str]], file_path: str) -> None:
    # file_path = f'{dataset_folder}/{file_name}'
    with open(file_path, 'w') as file:
        json.dump(qa_list, file, indent=4)
    print(f'{file_path} saved successfully')

def load_from_file(file_path: str) -> str:
    with open(file_path, 'r') as file:
        gt_report = file.read()
    return gt_report

def load_from_json(file_path: str) -> List[Dict[str, str]]:
    # file_path = f'{dataset_folder}/{file_name}'
    with open(file_path, 'r') as file:
        qa_list = json.load(file)
    print(f'{file_path} object loaded successfully')
    return qa_list

def generate_questions_and_answers_prompt(report: str) -> List[Dict[str, str]]:
    prompt_template = textwrap.dedent(f"""
    Generate 50 multiple detailed questions and concise answers based on the following report:
                                      
    {escape_curly_braces(report)}

    Your output should be in json format (```json and ``` tags) as follows:

    [
      {escape_curly_braces({"question": "question here", "answer": "answer here"})},
      {escape_curly_braces({"question": "question here", "answer": "answer here"})},
      ...
      {escape_curly_braces({"question": "question here", "answer": "answer here"})},
    ]

    Only output the json (using ```json and ``` tags), no explanations. Think step by step to solve your task. 
    
    """)

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are an expert in data science"),
            ("human", prompt_template),
        ]
    )

    return prompt

def generate_mchoice_qa_prompt(report: str, number_qa: int) -> List[Dict[str, str]]:
    prompt_template = textwrap.dedent(f"""
    Generate {number_qa} detailed multiple-choice questions and concise answers based on the following comprehensive report. 
    Each question should have five options (A, B, C, D, E) and should cover various aspects of the report. Ensure the correct answer is clearly indicated and is unique. 
    Make sure to include numerical comparisons and insights drawn from the current and reference distributions wherever applicable:
    
                                                                 
    {escape_curly_braces(report)}

    Your output should be in json format (```json and ``` tags) as follows:

    [
      {escape_curly_braces({"question": "question here", "options": ["A) option1", "B) option2", "C) option3", "D) option4", "E) option5"], "answer": "A"})},
      {escape_curly_braces({"question": "question here", "options": ["A) option1", "B) option2", "C) option3", "D) option4", "E) option5"], "answer": "C"})},
      ...
      {escape_curly_braces({"question": "question here", "options": ["A) option1", "B) option2", "C) option3", "D) option4", "E) option5"], "answer": "E"})},
    ]

    Only output the json (using ```json and ``` tags), no explanations. Think step by step to solve your task.
    """)

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are an expert in data science."),
            ("human", prompt_template),
        ]
    )

    return prompt

def extract_json(message: AIMessage) -> List[dict]:
    """Extracts JSON content from a string where JSON is embedded between ```json and ``` tags.

    Parameters:
        text (str): The text containing the JSON content.

    Returns:
        list: A list of extracted JSON strings.
    """
    text = message.content
    # Define the regular expression pattern to match JSON blocks
    pattern = r"```json(.*?)```"

    # Find all non-overlapping matches of the pattern in the string
    matches = re.findall(pattern, text, re.DOTALL)

    # Return the list of matched JSON strings, stripping any leading or trailing whitespace
    try:
        return [json.loads(match.strip()) for match in matches][0]
    except Exception:
        raise ValueError(f"Failed to parse: {message}")
    
def extract_markdown(message):
    """Extracts Markdown content from a string where Markdown is embedded between ```markdown and ``` tags.

    Parameters:
        message (AIMessage): The message object containing the Markdown content.

    Returns:
        str: The extracted Markdown content.
    """
    text = message.content
    # Define the regular expression pattern to match Markdown blocks
    pattern = r"```markdown(.*?)```"

    # Find all non-overlapping matches of the pattern in the string
    matches = re.findall(pattern, text, re.DOTALL)

    # Return the list of matched Markdown strings, stripping any leading or trailing whitespace
    try:
        return matches[0].strip() if matches else None
    except Exception:
        raise ValueError(f"Failed to parse: {message}")
    
def get_answers_from_report_prompt_old(report: str, questions: List[Dict[str, str]]) -> str:
    system_prompt = textwrap.dedent(f"""
    You are an expert in data science. Read the following report carefully and answer the questions concisely.
    If you do not know say I DON'T KNOW, do not make up answers.                               
                                    
    Report:
                                      
    {escape_curly_braces(report)}

    Your output should be in json format (```json and ``` tags) as follows:

    [
      {escape_curly_braces({"question": "copy the question here", "answer": "your answer here"})},
      {escape_curly_braces({"question": "copy the question here", "answer": "answer here"})},
      ...
      {escape_curly_braces({"question": "copy the question here", "answer": "answer here"})},
    ]

    Questions:

    """)

    # Convert questions list to a string that can be included in the prompt
    questions_str = '\n'.join([f'{i+1}. {q["question"]}' for i, q in enumerate(questions)])
    
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", questions_str)
        ]
    )

    return prompt

def get_answers_from_report_prompt(report: str, questions: List[Dict[str, str]]) -> str:
    system_prompt = textwrap.dedent(f"""
    You are an expert in data science. Read the following report carefully and answer the multiple-choice questions concisely. 
    For each question, provide the correct option (A, B, C, D or E). If you do not know the answer, your answer should be I DON'T KNOW, do not make up answers.
                                    
    Report:
                                      
    {escape_curly_braces(report)}

    Your output should be in json format (```json and ``` tags) as follows:

    [
      {escape_curly_braces({"question": "copy the question here", "answer": "A"})},
      {escape_curly_braces({"question": "copy the question here", "answer": "E"})},
      ...
      {escape_curly_braces({"question": "copy the question here", "answer": "C"})},
    ]

    Questions:

    """)

    # Convert questions list to a string that can be included in the prompt
    questions_str = '\n'.join([f'{q["question"]} Options: {", ".join(q["options"])}' for i, q in enumerate(questions)])
    
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", escape_curly_braces(questions_str))
        ]
    )

    return prompt

def evaluate_all_questions(qa_ground_truth: List[Dict[str, str]], 
                           answers_generated: List[Dict[str, str]],
                           evaluator) -> List[Dict[str, any]]:
    scores = []

    for i in range(len(qa_ground_truth)):
        eval_result = evaluator.evaluate_strings(
            prediction=answers_generated[i]['answer'],
            reference=qa_ground_truth[i]['answer'],
            input=qa_ground_truth[i]['question'],
        )
        scores.append({
            'question': qa_ground_truth[i]['question'],
            'predicted_answer': answers_generated[i]['answer'],
            'reference_answer': qa_ground_truth[i]['answer'],
            'score': eval_result['score'],
            'reasoning': eval_result['reasoning']
        })

    return scores

def generate_comparison_prompt(criteria: dict, ground_truth: list, llm_answers: list) -> str:
    criteria_str = "\n".join([f'{key}: """{value.strip()}"""' for key, value in criteria.items()])
    ground_truth_str = json.dumps(ground_truth, indent=4)
    llm_answers_str = json.dumps(llm_answers, indent=4)

    system_prompt = textwrap.dedent(f"""
        Read the following criteria to evaluate LLM answers. Then, read the set of ground truth questions and answers. Your task is to compare each LLM answer with the corresponding ground truth answer (matching the question) and provide a score.

        # Criteria

        {escape_curly_braces(criteria_str)}

        # Ground Truth

        {escape_curly_braces(ground_truth_str)}

        # LLM Answers

        {escape_curly_braces(llm_answers_str)}

        # Output

        Your output should be a JSON array of scores where each score corresponds to the comparison between the ground truth answer and the LLM answer for each question.

        For example:

        [
            10,
            7,
            5,
            ...
        ]

    """)
    
    final_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "Only output the json format (```json and ``` tags) array of scores. Do not include any explanations. Think step by step to solve your task."),
        ]
    )

    return final_prompt

# Create a function that evaluate only two whole texts, one prediction and one reference
def evaluate_two_texts(prediction: str, reference: str, evaluator) -> Dict[str, any]:
    eval_result = evaluator.evaluate_strings(
        prediction=prediction,
        reference=reference,
        input="",
    )

    return {
        'predicted_answer': prediction,
        'reference_answer': reference,
        'score': eval_result['score'],
        'reasoning': eval_result['reasoning']
    }

def get_final_accuracy(evaluation_results: List[Dict[str, any]]) -> float:
    total_score = sum(result['score'] for result in evaluation_results)
    num_questions = len(evaluation_results)
    final_score = total_score / num_questions
    return final_score

def get_average_accuracy(evaluation_results: List) -> float:
    total_score = sum(evaluation_results)
    num_questions = len(evaluation_results)
    final_score = total_score / num_questions
    return final_score

def generate_only_prompt_report_prompt(slow_tools_results: Dict, description: Dict) -> ChatPromptTemplate:
    system_prompt = textwrap.dedent(f"""
    You are an expert in data science. Based on the following information, generate a comprehensive report that includes an executive summary, dataset synopsis, detailed tools analysis, and conclusion.

    Dataset information:

    {escape_curly_braces(description)}

    Tools results:              
                                                                 
    {escape_curly_braces(slow_tools_results)}

    """)

    final_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "Your output should be in markdown format."),
        ]
    )

    return final_prompt

def generate_only_prompt_cot_report_prompt(slow_tools_results: Dict, description: Dict) -> ChatPromptTemplate:
    system_prompt = textwrap.dedent(f"""
    You are an expert in data science. Based on the following information, generate a comprehensive report that includes an executive summary, dataset synopsis, detailed tools analysis, and conclusion.

    Dataset information:

    {escape_curly_braces(description)}

    Tools results:              
                                                                 
    {escape_curly_braces(slow_tools_results)}

    """)

    final_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "Your output should be in markdown format. Think step by step to solve your task."),
        ]
    )

    return final_prompt


def evaluate_answers(ground_truth: List[Dict[str, str]], generated_answers: List[Dict[str, str]]) -> float:
    """
    Evaluates the generated answers against the ground truth answers and returns a score.

    Parameters:
    ground_truth (List[Dict[str, str]]): A list of dictionaries containing ground truth questions and answers.
    generated_answers (List[Dict[str, str]]): A list of dictionaries containing generated questions and answers.

    Returns:
    float: The score as a percentage of correct answers.
    """
    if len(ground_truth) != len(generated_answers):
        raise ValueError("The number of questions in ground truth and generated answers must be the same.")

    correct_count = 0

    for gt, ga in zip(ground_truth, generated_answers):
        if gt["question"] != ga["question"]:
            raise ValueError(f"Question mismatch: {gt['question']} != {ga['question']}")
        
        if gt["answer"] == ga["answer"]:
            correct_count += 1

    score = (correct_count / len(ground_truth)) * 100
    return score

def evaluate_answers_with_unknowns(ground_truth: List[Dict[str, str]], generated_answers: List[Dict[str, str]]) -> Tuple[float, float]:
    """
    Evaluates the generated answers against the ground truth answers and returns the accuracy score
    along with the ratio of "I DON'T KNOW" responses.

    Parameters:
    ground_truth (List[Dict[str, str]]): A list of dictionaries containing ground truth questions and answers.
    generated_answers (List[Dict[str, str]]): A list of dictionaries containing generated questions and answers.

    Returns:
    Tuple[float, float]: A tuple containing (accuracy_score, unknown_ratio), where:
        - accuracy_score is the percentage of correct answers
        - unknown_ratio is the percentage of "I DON'T KNOW" responses
    """
    if len(ground_truth) != len(generated_answers):
        raise ValueError("The number of questions in ground truth and generated answers must be the same.")

    correct_count = 0
    unknown_count = 0

    for gt, ga in zip(ground_truth, generated_answers):
        if gt["question"] != ga["question"]:
            raise ValueError(f"Question mismatch: {gt['question']} != {ga['question']}")
        
        if gt["answer"] == ga["answer"]:
            correct_count += 1
        
        if ga["answer"] == "I DON'T KNOW":
            unknown_count += 1

    total_questions = len(ground_truth)
    accuracy_score = (correct_count / total_questions) * 100
    unknown_ratio = (unknown_count / total_questions) * 100

    return accuracy_score, unknown_ratio


class ReflectionReportGenerator:
    def __init__(self, llm=None):
        self.llm = llm
        self.graph = self.build_graph()

    def build_graph(self) -> MessageGraph:
        builder = MessageGraph()
        builder.add_node("generate", self.generation_node)
        builder.add_node("reflect", self.reflection_node)
        builder.set_entry_point("generate")

        builder.add_conditional_edges("generate", self.should_continue)
        builder.add_edge("reflect", "generate")
        return builder.compile()

    async def generation_node(self, state):
        return await self.generate.ainvoke({"messages": state})

    async def reflection_node(self, messages):
        cls_map = {"ai": HumanMessage, "human": AIMessage}
        translated = [messages[0]] + [
            cls_map[msg.type](content=msg.content) for msg in messages[1:]
        ]
        res = await self.reflect.ainvoke({"messages": translated})
        return HumanMessage(content=res.content)

    def should_continue(self, state):
        if len(state) > 3:  # End after 3 iterations (initial + 2 reflections)
            return END
        return "reflect"

    def create_prompts(self, slow_tools_results: Dict, description: Dict):
        dataset_info = escape_curly_braces(description)
        tools_results = escape_curly_braces(slow_tools_results)

        system_prompt = textwrap.dedent(f"""
        You are an expert in data science tasked with generating a comprehensive report that includes an executive summary, dataset synopsis, detailed tools analysis, and conclusion. Use the following information:

        Dataset information:
        {dataset_info}

        Tools results:              
        {tools_results}

        Your output should be in markdown format.
        """)

        self.generate = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                MessagesPlaceholder(variable_name="messages"),
            ]
        ) | self.llm

        self.reflect = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You are a senior data scientist reviewing a report. Provide detailed critique and recommendations, focusing on:"
                    "\n1. Clarity and structure of the executive summary"
                    "\n2. Completeness of the dataset synopsis"
                    "\n3. Depth and accuracy of the tools analysis"
                    "\nSuggest specific improvements for each section."
                ),
                MessagesPlaceholder(variable_name="messages"),
            ]
        ) | self.llm

    async def generate_report(self, slow_tools_results: Dict, description: Dict):
        self.create_prompts(slow_tools_results, description)
        initial_message = SystemMessage(content="Generate the report.")

        async for event in self.graph.astream([initial_message]):
            # print(event)
            print("---")
            if isinstance(event, dict) and "generate" in event:
                final_report = event["generate"].content

        return final_report
    


class AgentState(Dict):
    input: str
    chat_history: list[BaseMessage]
    agent_outcome: Union[AgentAction, AgentFinish, None]
    return_direct: bool
    intermediate_steps: Annotated[List[Tuple[AgentAction, str]], operator.add]
    slow_tools_results: Dict


class ReactReportGenerator:
    def __init__(self, llm=None):
        self.llm = llm
        self.tools = None  # Will be set in create_tools
        self.tool_executor = None  # Will be set in create_tools
        self.agent_runnable = None  # Will be set in create_tools
        self.graph = self.build_graph()

    def create_tools(self, slow_tools_results: Dict) -> List[Tool]:
        self.tools = [
            Tool(
                name="GetDriftReport",
                func=lambda _: str(slow_tools_results['get_drift_report']),
                description="Retrieves the pre-calculated drift report, providing insights into dataset drift changes.",
            ),
            Tool(
                name="GetSHAPValues",
                func=lambda _: str(slow_tools_results['get_shap_values']),
                description="Retrieves the pre-calculated SHAP values, showing feature importance in both datasets.",
            ),
        ]
        self.tool_executor = ToolExecutor(self.tools)

        # Custom prompt for the agent
        template = '''You are an expert data scientist tasked with generating a comprehensive monitoring report on dataset changes. You have access to the following tools:

{tools}

Use the following format:

Question: the input task you must solve
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin your analysis and report generation!

Question: {input}
Thought:{agent_scratchpad}'''
        from langchain.agents import create_react_agent
        prompt = PromptTemplate.from_template(template)
        self.agent_runnable = create_react_agent(self.llm, self.tools, prompt)

        return self.tools

    def build_graph(self) -> StateGraph:
        workflow = StateGraph(AgentState)
        workflow.add_node("agent", self.run_agent)
        workflow.add_node("action", self.execute_tools)
        workflow.set_entry_point("agent")
        workflow.add_conditional_edges(
            "agent",
            self.should_continue,
            {
                "continue": "action",
                "end": END
            }
        )
        workflow.add_edge('action', 'agent')
        return workflow.compile()

    # @as_runnable
    def run_agent(self, state: AgentState) -> AgentState:
        # agent_outcome = self.agent_runnable.invoke(state)
        # return {"agent_outcome": agent_outcome}
        try:
            agent_outcome = self.agent_runnable.invoke(state)
            return {"agent_outcome": agent_outcome}
        except OutputParserException as e:
            print(f"Error encountered: {e}. Attempting to continue with the partial output.")
            partial_output = e.llm_output if hasattr(e, 'llm_output') else "Error: Unable to retrieve output."
            return {"agent_outcome": AgentFinish(return_values={'output': partial_output}, log=str(e))}
    
    # @as_runnable
    def execute_tools(self, state: AgentState) -> AgentState:
        last_message = state['agent_outcome']
        tool_name = last_message.tool
        tool_input = last_message.tool_input
        action = ToolInvocation(tool=tool_name, tool_input=tool_input)
        response = self.tool_executor.invoke(action)
        return {"intermediate_steps": [(state['agent_outcome'], response)]}

    # @as_runnable
    def should_continue(self, state: AgentState) -> str:
        last_message = state['agent_outcome']
        if isinstance(last_message, AgentFinish):
            return "end"
        else:
            return "continue"

    def generate_report(self, description: Dict, slow_tools_results: Dict) -> str:
        self.create_tools(slow_tools_results)

        system_message = SystemMessage(content=textwrap.dedent(f"""
        You are an expert data scientist tasked with generating a comprehensive report on dataset changes. Your goal is to produce a report that includes an executive summary, dataset synopsis, detailed tools analysis, and conclusion. Use the following dataset information and the available tools to conduct your analysis:

        Dataset information:
        {escape_curly_braces(description)}
        """))

        human_message = HumanMessage(content="Begin your analysis and report generation.")

        initial_state = AgentState(
            input=human_message.content,
            chat_history=[system_message],
            agent_outcome=None,
            return_direct=False,
            intermediate_steps=[],
            slow_tools_results=slow_tools_results
        )

        final_report = ""
        for event in self.graph.stream(initial_state):
            print(event)
            print("----")
            if isinstance(event, dict) and "agent_outcome" in event:
                outcome = event["agent_outcome"]
                if isinstance(outcome, AgentFinish):
                    final_report = outcome.return_values['output']
                    # break

        return event['agent']['agent_outcome'].return_values['output']
    


# Define the state dictionary for SelfDiscover
class SelfDiscoverState(TypedDict):
    reasoning_modules: str
    task_description: str
    selected_modules: Optional[str]
    adapted_modules: Optional[str]
    reasoning_structure: Optional[str]
    answer: Optional[str]

class SelfDiscoverReportGenerator:
    def __init__(self, llm):
        self.model = llm
        self.select_prompt = hub.pull("hwchase17/self-discovery-select")
        self.adapt_prompt = hub.pull("hwchase17/self-discovery-adapt")
        self.structure_prompt = hub.pull("hwchase17/self-discovery-structure")
        self.reasoning_prompt = hub.pull("hwchase17/self-discovery-reasoning")
        self.graph = self.build_graph()

    
    def select(self, inputs):
        select_chain = self.select_prompt | self.model | StrOutputParser()
        return {"selected_modules": select_chain.invoke(inputs)}

    
    def adapt(self, inputs):
        adapt_chain = self.adapt_prompt | self.model | StrOutputParser()
        return {"adapted_modules": adapt_chain.invoke(inputs)}

    
    def structure(self, inputs):
        structure_chain = self.structure_prompt | self.model | StrOutputParser()
        return {"reasoning_structure": structure_chain.invoke(inputs)}
    
    
    def reason(self, inputs):
        reasoning_chain = self.reasoning_prompt | self.model | StrOutputParser()
        return {"answer": reasoning_chain.invoke(inputs)}

    def build_graph(self) -> StateGraph:
        graph = StateGraph(SelfDiscoverState)
        graph.add_node("select", self.select)
        graph.add_node("adapt", self.adapt)
        graph.add_node("structure", self.structure)
        graph.add_node("reason", self.reason)
        graph.add_edge("select", "adapt")
        graph.add_edge("adapt", "structure")
        graph.add_edge("structure", "reason")
        graph.add_edge("reason", END)
        graph.set_entry_point("select")
        return graph.compile()

    def generate_report(self, task_description: str, reasoning_modules: List[str]) -> str:
        reasoning_modules_str = "\n".join(reasoning_modules)
        initial_state = {
            "task_description": task_description,
            "reasoning_modules": reasoning_modules_str,
            "selected_modules": None,
            "adapted_modules": None,
            "reasoning_structure": None,
            "answer": None
        }
        final_report = ""
        try:
            for event in self.graph.stream(initial_state):
                print(event)
                print("----")
                if isinstance(event, dict) and "answer" in event:
                    final_report = event["answer"]
        except Exception as e:
            print(f"Error encountered: {e}. Returning the partial result.")
            # return event['agent']['past_steps'][-1][0].content # Last plan
            return event['reason']['answer']
        return event['reason']['answer']
    
        # final_report = ""
        # for event in self.graph.stream(initial_state):
        #     print(event)
        #     print("----")
        #     if isinstance(event, dict) and "answer" in event:
        #         final_report = event["answer"]
        #         # break

        # return event['reason']['answer']
    

class PlanExecute(TypedDict):
    input: str
    plan: List[str]
    past_steps: Annotated[List[Tuple], operator.add]
    response: str

class PlanAndExecuteReportGenerator:
    def __init__(self, llm=None):
        self.llm = llm
        self.tools = None  # Will be set in create_tools
        self.tool_executor = None  # Will be set in create_tools
        self.agent_executor = None  # Will be set in create_tools
        self.graph = self.build_graph()

    def create_tools(self, slow_tools_results: Dict) -> List[Tool]:
        self.tools = [
            Tool(
                name="GetDriftReport",
                func=lambda _: str(slow_tools_results['get_drift_report']),
                description="Retrieves the pre-calculated drift report, providing insights into dataset drift changes.",
            ),
            Tool(
                name="GetSHAPValues",
                func=lambda _: str(slow_tools_results['get_shap_values']),
                description="Retrieves the pre-calculated SHAP values, showing feature importance in both datasets.",
            ),
        ]
        self.tool_executor = ToolExecutor(self.tools)
        invocation1 = ToolInvocation(tool="GetDriftReport", tool_input="GetDriftReport")
        result1 = self.tool_executor.invoke(invocation1)
        invocation2 = ToolInvocation(tool="GetSHAPValues", tool_input="GetDriftReport")
        result2 = self.tool_executor.invoke(invocation2)
        # Define the prompt for the agent
        # prompt = hub.pull("wfh/react-agent-executor")

        template = f"""You are an expert data scientist tasked with generating a comprehensive monitoring report on dataset changes. You have access to the following tools results:

        GetDriftReport:
        {escape_curly_braces(result1)}

        GetSHAPValues:
        {escape_curly_braces(result2)}

        """

        prompt = PromptTemplate.from_template(template)
        # from langgraph.prebuilt import create_react_agent
        # from langchain.agents import create_react_agent
        # self.agent_executor = create_react_agent(self.llm, self.tools, messages_modifier=prompt)
        tools_renderer: ToolsRenderer = render_text_description
        # prompt = prompt.partial(
        #     tools=tools_renderer(list(self.tools)),  
        # # tool_names=", ".join([t.name for t in tools]),
        # )
        
        self.agent_executor = prompt | self.llm
        # self.agent_executor = create_react_agent(self.llm, self.tools, prompt=prompt)

        return self.tools

    def build_graph(self) -> StateGraph:
        workflow = StateGraph(PlanExecute)

        # Add the plan node
        workflow.add_node("planner", self.plan_step)

        # Add the execution step
        workflow.add_node("agent", self.execute_step)

        # Add a replan node
        workflow.add_node("replan", self.replan_step)

        workflow.set_entry_point("planner")

        # From plan we go to agent
        workflow.add_edge("planner", "agent")

        # From agent, we replan
        workflow.add_edge("agent", "replan")

        workflow.add_conditional_edges(
            "replan",
            self.should_end,
        )

        return workflow.compile()

    # @as_runnable
    def execute_step(self, state: PlanExecute):
        plan = state["plan"]
        plan_str = "\n".join(f"{i+1}. {step}" for i, step in enumerate(plan))
        task = plan#[0]
        task_formatted = f"""For the following plan:
{plan_str}\n\nYou are tasked with executing step 1, {task}."""
        agent_response = self.agent_executor.invoke(
            {"messages": [("user", task_formatted)]}
        )
        return {
            "past_steps": state["past_steps"] + [(task, agent_response.content)],
        }

    # @as_runnable
    def plan_step(self, state: PlanExecute):
        planner_prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """For the given objective, come up with a simple step by step plan. \
This plan should involve individual tasks, that if executed correctly will yield the correct answer. Do not add any superfluous steps. \
The result of the final step should be the final answer. Make sure that each step has all the information needed - do not skip steps.

Your output should be a list of strings (different steps to follow, should be in sorted order)

""",
                ),
                ("placeholder", "{messages}"),
            ]
        )
        planner = planner_prompt | self.llm#.with_structured_output(Plan)
        plan = planner.invoke({"messages": [("user", state["input"])]})
        return {"plan": plan}

    # @as_runnable
    def replan_step(self, state: PlanExecute):
        replanner_prompt = ChatPromptTemplate.from_template(
            """For the given objective, come up with a simple step by step plan. \
This plan should involve individual tasks, that if executed correctly will yield the correct answer. Do not add any superfluous steps. \
The result of the final step should be the final answer. Make sure that each step has all the information needed - do not skip steps.

Your objective was this:
{input}

Your original plan was this:
{plan}

You have currently done the following steps:
{past_steps}

Update your plan accordingly. If no more steps are needed and you can return to the user, then respond with that. Otherwise, fill out the plan. Only add steps to the plan that still NEED to be done. Do not return previously done steps as part of the plan.

Your output should be a list of strings (different steps to follow, should be in sorted order) OR only one string (a response to the user).


"""
        )

        replanner = replanner_prompt | self.llm#.with_structured_output(Act)
        output = replanner.invoke(state)

        if isinstance(output, str):
            return {"response": output}
        else:
            return {"plan": output}

    
    def should_end(self, state: PlanExecute) -> Literal["agent", "__end__"]:
        if "response" in state and state["response"]:
            return "__end__"
        else:
            return "agent"

    # @as_runnable
    def generate_report(self, description: Dict, slow_tools_results: Dict) -> str:
        self.create_tools(slow_tools_results)

        initial_state = {
            "input": description,
            "plan": [],
            "past_steps": [],
            "response": ""
        }

        # config = {"recursion_limit": 50}
        final_report = ""
        try:
            for event in self.graph.stream(initial_state):
                print(event)
                print("----")
                for k, v in event.items():
                    if k != "__end__":
                        final_report = v
        except Exception as e:
            print(f"Error encountered: {e}. Returning the partial result.")
            # return event['agent']['past_steps'][-1][0].content # Last plan
            return event
        return event
        # return event['agent']['past_steps'][-1][0].content

