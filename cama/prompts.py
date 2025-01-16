from langchain_core.prompts import ChatPromptTemplate
from typing import Dict
from cama.memory import SemanticMemory
from cama.representation import DatasetRepresentation
import textwrap

def escape_curly_braces(description):
    return description.replace("{", "{{").replace("}", "}}")

def generate_dynamic_system_prompt(feature_info: Dict, dataset_info: Dict):
    tool_results = "\n\n".join(
        ["**{tool_name}**:\n{description}\n\nResult: {result}".format(
            tool_name=tool['name'],
            description=escape_curly_braces(tool['description']),
            result=escape_curly_braces(str(tool['result']))
        ) for tool in feature_info['tools_results']]
    )

    # get tools names
    tools_names = [tool['name'] for tool in feature_info['tools_results']]

    system_prompt_template = """
    You are an expert data scientist. Your task is to generate a comprehensive and detailed report for the results in {tools_names} tools using the following information:
    
    **Dataset Information**:
    Title: {dataset_title}
    Description: {dataset_description}
    
    **Feature Information**:
    - **Name**: {name}
    - **Description**: {description}
    - **Type**: {type}
    - **Possible Values**: {possible_values}
    - **Data Type**: {data_type}
    
    **Tool Results**:
    {tool_results}
    
    Use the following structure to write your report:

    # Feature description

    # Tool [put the name here] results
    [put the report here]

    # Tool [put the name here] results
    [put the results here]

    Etc.

    
    
    """
    
    return system_prompt_template.format(
        tools_names=", ".join(tools_names),
        dataset_title=dataset_info['dataset_title'],
        dataset_description=dataset_info['dataset_description'],
        name=feature_info['name'],
        description=feature_info['description'],
        type=feature_info['type'],
        possible_values=escape_curly_braces(str(feature_info['possible_values'])),
        data_type=feature_info['data_type'],
        tool_results=escape_curly_braces(tool_results)
    )

# def generate_dynamic_system_prompt(dataset_description, tools_description):
#     num_samples = dataset_description['NUM_SAMPLES']
#     features = ', '.join(dataset_description['FEATURES'])
#     numerical_features = ', '.join(dataset_description['NUMERICAL_FEATURES'])
#     categorical_features = ', '.join(dataset_description['CATEGORICAL_FEATURES'])
#     label = dataset_description['LABEL']
#     column_types = dataset_description['COLUMN_TYPES']
#     feature_descriptions = dataset_description['FEATURE_DESCRIPTIONS']
#     label_description = dataset_description['LABEL_DESCRIPTION']
#     dataset_title = dataset_description['DATASET_TITLE']
#     dataset_description_text = dataset_description['DATASET_DESCRIPTION']

#     formatted_feature_descriptions = "\n".join([f"- **{feature}**: {desc}" for feature, desc in feature_descriptions.items()])
#     formatted_column_types = "\n".join([f"- **{column}**: {col_type}" for column, col_type in column_types.items()])



#     tool_descriptions = "\n\n".join(
#         ["**{tool_name}**:\n{description}".format(
#             tool_name=tool_name,
#             description=escape_curly_braces(tool_info.description)
#         ) for tool_name, tool_info in tools_description.items()]
#     )

#     # dynamic_tool_instructions = generate_dynamic_tool_instructions(tools_description)

#     system_prompt_template = """
#     You are a highly experienced data scientist. Your task is to generate a comprehensive and detailed feature report
#     that explain the current state of each feature in detail in the **{dataset_title}** dataset. The dataset is described as follows: {dataset_description_text}.
    
#     **Dataset Overview**:
#     - **Number of Samples**: {num_samples}
#     - **All Features**: {features}
#     - **Numerical Features**: {numerical_features}
#     - **Categorical Features**: {categorical_features}
#     - **Label**: {label}
    
#     **Label Description**:
#     {label_description}
    
#     **Feature Descriptions**:
#     {formatted_feature_descriptions}
    
#     **Column Types**:
#     {formatted_column_types}
    
#     Your task is to write comprehensive reports that analyze feature behavior, patterns, and trends using the available tools to provide detailed numerical, statistical, and distributional insights.
    
#     **Available Tools**:
#     {tool_descriptions}


#     """
#     return system_prompt_template.format(
#         dataset_title=dataset_title,
#         dataset_description_text=dataset_description_text,
#         num_samples=num_samples,
#         features=features,
#         numerical_features=numerical_features,
#         categorical_features=categorical_features,
#         label=label,
#         label_description=label_description,
#         formatted_feature_descriptions=formatted_feature_descriptions,
#         formatted_column_types=formatted_column_types,
#         tool_descriptions=tool_descriptions,
#         # dynamic_tool_instructions=dynamic_tool_instructions
#     )

# def generate_dynamic_tool_instructions(tools_description):
#     tool_instructions = []

#     for tool_name, tool_info in tools_description.items():
#         # instruction = """
#         # - **{tool_name}**:
#         #     - **Details**: [Include comprehensive details for {tool_name}.]
#         # """.format(tool_name=tool_name.replace('_', ' ').title())
#         instruction = """
#         - **{tool_name}**:
#             - **Details**: [Include comprehensive details for {tool_name}.]
#         """.format(tool_name=tool_name.replace('_', ' ').title())
#         tool_instructions.append(instruction)

#     return "\n".join(tool_instructions)

# def get_prompt_for_explanation(semantic_memory: SemanticMemory):
#     system_prompt = generate_dynamic_system_prompt(semantic_memory.reference_dataset.description, semantic_memory.tools)
#     final_prompt = ChatPromptTemplate.from_messages(
#         [
#             ("system", system_prompt),
#             # ("human", "Explain the feature '{feature_name}' using the following information:\n{input}\n. Do not write any code only explanations."),
#             ("human", "Explain the feature '{feature_name}' using the following information:\n{input}\n. Do not write any code only explanations. Be concise."),
#         ]
#     )
#     return final_prompt

# def get_prompt_for_explanation(feature_info: Dict, dataset_info: Dict):
#     system_prompt = generate_dynamic_system_prompt(feature_info, dataset_info)
#     final_prompt = ChatPromptTemplate.from_messages(
#         [
#             ("system", system_prompt),
#             ("human", "Explain the details using the provided information. Do not write any code, only explanations. "),
#         ]
#     )
#     return final_prompt


def get_prompt_for_feature_explanation(feature_info: Dict, dataset_info: Dict) -> ChatPromptTemplate:
    system_prompt = textwrap.dedent("""
    You are an expert data scientist tasked with generating a comprehensive and detailed report for a dataset analysis. Use the following COSTAR framework to structure your response:
    Context: You are analyzing a feature within a dataset using various tools. The results from these tools need to be compiled into a cohesive report.
    Objective: Generate a detailed report that describes the feature, presents the results from various analysis tools, and provides insights based on these results within the context of the overall dataset.
    Style: Write in a professional, analytical style typical of data science reports. Be clear, concise, and well-structured with proper headings and subheadings. Include technical details and data-driven insights.
    Tone: Maintain an objective, authoritative, and informative tone throughout the report, reflecting your expertise in data science.
    Audience: Your report is for data scientists, business analysts, and stakeholders interested in the dataset analysis results. Assume the audience has a good understanding of data science concepts and terminology.
    Response Format: Structure your report as follows:
    1. Feature Description
       - Name
       - Description
       - Type
       - Possible Values
       - Data Type
    2. Tool Results (for each tool)
       - Detailed analysis of results
       - Insights and interpretations
    3. Overall Feature Analysis
       - Summary of key findings
                                    
    Do not add more sections. Use the provided information to fill in the details for each section. Ensure that your analysis is thorough and provides valuable analysis for each tool's results.
    """)

    tool_results = "\n".join([
        f"- {tool['name']}:\n  Description: {tool['description']}\n  Result: {tool['result']}"
        for tool in feature_info['tools_results']
    ])

    tools_names = ", ".join([tool['name'] for tool in feature_info['tools_results']])

    human_template = textwrap.dedent("""
    Generate a comprehensive data science report using the following information:
                                     
    Dataset Information:
    Title: {dataset_title}
    Description: {dataset_description}
    Feature Information:
    - Name: {name}
    - Description: {description}
    - Type: {type}
    - Possible Values: {possible_values}
    - Data Type: {data_type}
    Tool Results:
    {tool_results}
    Tools used: {tools_names}
    """)

    human_message = human_template.format(
        dataset_title=dataset_info['dataset_title'],
        dataset_description=dataset_info['dataset_description'],
        name=feature_info['name'],
        description=feature_info['description'],
        type=feature_info['type'],
        possible_values=escape_curly_braces(str(feature_info['possible_values'])),
        data_type=feature_info['data_type'],
        tool_results=escape_curly_braces(tool_results),
        tools_names=tools_names
    )

    final_prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", human_message),
    ])

    return final_prompt

def get_overview_report_prompt(dataset_representation: DatasetRepresentation, feature_outputs, label_report: str):
    feature_reports = {
        d['feature']: f"{d['report']}"
        for d in feature_outputs
    }
    final_prompt_str = generate_overview_report_prompt(dataset_representation, feature_reports, label_report)
    final_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", final_prompt_str),
            ("human", "Provide a brief, easy-to-read overview of the key findings and main points. Use only bullets "),
            # ("human", "Generate both a summary and a conclusion based on the given information."),
        ]
    )
    return final_prompt

# def get_summary_report_prompt():
#     return ChatPromptTemplate.from_messages([
#         ("system", """You are an AI assistant tasked with summarizing feature reports for a dataset. 
#         Your goal is to extract the most important information and key insights from each feature report.
#         Provide a concise summary in 3-5 bullet points."""),
#         ("human", "Summarize the following feature report:\n\n{feature_report}")
#     ])

# def get_overview_report_prompt():
#     return ChatPromptTemplate.from_messages([
#         ("system", """You are a data scientist tasked with generating a concise overview based on the provided dataset information.
#         The input is a JSON string containing summarized information about the dataset, its features, and label.
#         Your task is to analyze this information and generate a summary and conclusion.

#         Based on the input, generate a summary and conclusion. The output should be formatted in markdown as follows:

#         ## Summary
#         - [Key point 1]
#         - [Key point 2]
#         ...

#         ## Conclusion
#         [Your conclusion here]

#         Remember:
#         - The summary should provide a brief, easy-to-read overview of the key findings and main points.
#         - The conclusion should offer clear interpretations of the results, implications, and any actionable recommendations based on the analysis."""),
#         ("human", "Generate both a summary and a conclusion based on the following information:\n\n{dataset_info}")
#     ])

# def summarize_feature_report(feature_name: str, report: str, llm):
#     summary_prompt = get_summary_report_prompt()
#     chain = summary_prompt | llm
#     summary_output = chain.invoke({"feature_report": report})
#     return {
#         "name": feature_name,
#         "summary": summary_output.content
#     }

def generate_overview_report_prompt(dataset_representation: DatasetRepresentation, feature_reports: Dict[str, str], label_report: str) -> str:
    dataset_title = dataset_representation.name
    dataset_description = dataset_representation.description
    num_features = len(dataset_representation.features)
    label_name = dataset_representation.label.name
    label_description = dataset_representation.label.description

    feature_reports_section = "\n\n".join(
        [f"### {feature_name}\n\n{report}" for feature_name, report in feature_reports.items()]
    )

    system_prompt = textwrap.dedent(f"""
    You are a data scientist tasked with generating a concise summary based on the provided dataset information. Be concise, make it short and to the point.

    ### Dataset Overview:
    - **Title**: {dataset_title}
    - **Description**: {dataset_description}
    - **Number of Features**: {num_features}
    - **Label**: {label_name} - {label_description}

    ### Feature Reports:
    {escape_curly_braces(feature_reports_section)}

    ### Label Report:
    {escape_curly_braces(label_report)}


    """)
    return system_prompt

# def generate_overview_report_prompt(dataset_representation: DatasetRepresentation, feature_reports: Dict[str, str], label_report: str) -> str:
#     dataset_title = dataset_representation.name
#     dataset_description = dataset_representation.description
#     num_features = len(dataset_representation.features)
#     label_name = dataset_representation.label.name
#     label_description = dataset_representation.label.description

#     feature_reports_section = "\n\n".join(
#         [f"### {feature_name}\n\n{report}" for feature_name, report in feature_reports.items()]
#     )

#     system_prompt = textwrap.dedent(f"""
#     You are a data scientist tasked with generating a concise overview based on the provided dataset information. The overview should be verbose enough.

#     ### Dataset Overview:
#     - **Title**: {dataset_title}
#     - **Description**: {dataset_description}
#     - **Number of Features**: {num_features}
#     - **Label**: {label_name} - {label_description}

#     ### Feature Reports:
#     {escape_curly_braces(feature_reports_section)}

#     ### Label Report:
#     {escape_curly_braces(label_report)}

#     Remember that summary and conclusion definitions are as follows:

#     - **Summary**: Provide a brief, easy-to-read overview of the key findings and main points from the feature reports.
#     - **Conclusion**: Offer clear interpretations of the results, implications, and any actionable recommendations based on the analysis.

#     The output should be formatted in markdown as follows:

#     ## Summary
#     -
#     -
    
#     ## Conclusion

#     """)
#     return system_prompt

# def get_prompt_for_label_explanation(semantic_memory: SemanticMemory):
#     system_prompt = generate_dynamic_label_prompt(semantic_memory.reference_dataset.description, semantic_memory.tools)
#     final_prompt = ChatPromptTemplate.from_messages(
#         [
#             ("system", system_prompt),
#             ("human", "Explain the label '{label_name}' using the following information:\n{input}\n. Think step by step to solve your task"),
#         ]
#     )
#     return final_prompt

def get_prompt_for_label_explanation(label_info: Dict, dataset_info: Dict):
    system_prompt = generate_dynamic_label_prompt(label_info, dataset_info)
    final_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "Explain the label using the provided information."),
        ]
    )
    return final_prompt



def generate_dynamic_label_prompt(label_info: Dict, dataset_info: Dict):
    system_prompt_template = """
    You are a highly experienced data scientist. Your task is to generate a concise and detailed explanation
    for the label in the dataset "{dataset_title}".
    
    **Dataset Information**:
    Title: {dataset_title}
    Description: {dataset_description}
    
    **Label Information**:
    - **Name**: {name}
    - **Description**: {description}
    - **Type**: {type}
    - **Possible Values**: {possible_values}
    - **Data Type**: {data_type}
    
    **Instructions**:
     - Provide a concise and detailed explanation for the label in the dataset.
     - Indicate if there are any problems or issues with the label based on the available information.

    """
    
    return system_prompt_template.format(
        dataset_title=dataset_info['dataset_title'],
        dataset_description=dataset_info['dataset_description'],
        name=label_info['name'],
        description=label_info['description'],
        type=label_info['type'],
        possible_values=escape_curly_braces(str(label_info['possible_values'])),
        data_type=label_info['data_type']
    )


# def generate_dynamic_label_prompt(dataset_description, tools_description):
#     label_name = dataset_description['LABEL']
#     label_description = dataset_description['LABEL_DESCRIPTION']
#     tool_descriptions = "\n\n".join(
#         ["**{tool_name}**:\n{description}".format(
#             tool_name=tool_name,
#             description=escape_curly_braces(tool_info.description)
#         ) for tool_name, tool_info in tools_description.items()]
#     )

#     system_prompt_template = """
#     You are a highly experienced data scientist. Your task is to generate a concise and detailed explanation
#     for the label in the **{dataset_title}** dataset. The dataset is described as follows: {dataset_description_text}.
    
#     **Label**: {label_name}
    
#     **Label Description**:
#     {label_description}
    
#     **Available Tools**:
#     {tool_descriptions}
    
#     **Instructions**:
#     - Provide a concise and detailed explanation for the label in the dataset.
#     - Indicate if there are any problems or issues with the label based on the available information.


#     """
#     return system_prompt_template.format(
#         dataset_title=dataset_description['DATASET_TITLE'],
#         dataset_description_text=dataset_description['DATASET_DESCRIPTION'],
#         label_name=label_name,
#         label_description=label_description,
#         tool_descriptions=tool_descriptions
#     )