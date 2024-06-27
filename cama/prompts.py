from langchain_core.prompts import ChatPromptTemplate
from typing import Dict
from cama.memory import SemanticMemory
from cama.representation import DatasetRepresentation
import textwrap

def escape_curly_braces(description):
    return description.replace("{", "{{").replace("}", "}}")

def generate_dynamic_system_prompt(dataset_description, tools_description):
    num_samples = dataset_description['NUM_SAMPLES']
    features = ', '.join(dataset_description['FEATURES'])
    numerical_features = ', '.join(dataset_description['NUMERICAL_FEATURES'])
    categorical_features = ', '.join(dataset_description['CATEGORICAL_FEATURES'])
    label = dataset_description['LABEL']
    column_types = dataset_description['COLUMN_TYPES']
    feature_descriptions = dataset_description['FEATURE_DESCRIPTIONS']
    label_description = dataset_description['LABEL_DESCRIPTION']
    dataset_title = dataset_description['DATASET_TITLE']
    dataset_description_text = dataset_description['DATASET_DESCRIPTION']

    formatted_feature_descriptions = "\n".join([f"- **{feature}**: {desc}" for feature, desc in feature_descriptions.items()])
    formatted_column_types = "\n".join([f"- **{column}**: {col_type}" for column, col_type in column_types.items()])



    tool_descriptions = "\n\n".join(
        ["**{tool_name}**:\n{description}".format(
            tool_name=tool_name,
            description=escape_curly_braces(tool_info.description)
        ) for tool_name, tool_info in tools_description.items()]
    )

    dynamic_tool_instructions = generate_dynamic_tool_instructions(tools_description)

    system_prompt_template = """
    You are a highly experienced data scientist. Your task is to generate a comprehensive and detailed feature report
    that explain the current state of each feature in detail in the **{dataset_title}** dataset. The dataset is described as follows: {dataset_description_text}.
    
    **Dataset Overview**:
    - **Number of Samples**: {num_samples}
    - **All Features**: {features}
    - **Numerical Features**: {numerical_features}
    - **Categorical Features**: {categorical_features}
    - **Label**: {label}
    
    **Label Description**:
    {label_description}
    
    **Feature Descriptions**:
    {formatted_feature_descriptions}
    
    **Column Types**:
    {formatted_column_types}
    
    Your task is to write comprehensive reports that analyze feature behavior, patterns, and trends using the available tools to provide detailed numerical, statistical, and distributional insights.
    
    **Available Tools**:
    {tool_descriptions}
    
    **Instructions**:
    - Provide a verbose and detailed analysis of each feature in the dataset.
    {dynamic_tool_instructions}


    Think step by step to solve your task.

    """
    return system_prompt_template.format(
        dataset_title=dataset_title,
        dataset_description_text=dataset_description_text,
        num_samples=num_samples,
        features=features,
        numerical_features=numerical_features,
        categorical_features=categorical_features,
        label=label,
        label_description=label_description,
        formatted_feature_descriptions=formatted_feature_descriptions,
        formatted_column_types=formatted_column_types,
        tool_descriptions=tool_descriptions,
        dynamic_tool_instructions=dynamic_tool_instructions
    )

def generate_dynamic_tool_instructions(tools_description):
    tool_instructions = []

    for tool_name, tool_info in tools_description.items():
        # instruction = """
        # - **{tool_name}**:
        #     - **Details**: [Include comprehensive details for {tool_name}.]
        # """.format(tool_name=tool_name.replace('_', ' ').title())
        instruction = """
        - **{tool_name}**:
            - **Details**: [Include comprehensive details for {tool_name}. Think step by step to solve your task.]
        """.format(tool_name=tool_name.replace('_', ' ').title())
        tool_instructions.append(instruction)

    return "\n".join(tool_instructions)

def get_prompt_for_explanation(semantic_memory: SemanticMemory):
    system_prompt = generate_dynamic_system_prompt(semantic_memory.reference_dataset.description, semantic_memory.tools)
    final_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            # ("human", "Explain the feature '{feature_name}' using the following information:\n{input}\n. Do not write any code only explanations."),
            ("human", "Explain the feature '{feature_name}' using the following information:\n{input}\n. Do not write any code only explanations. Think step by step to solve your task"),
        ]
    )
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
            # ("human", "Generate both a summary and a conclusion based on the given information. "),
            ("human", "Generate both a summary and a conclusion based on the given information. Think step by step to solve your task."),
        ]
    )
    return final_prompt

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
    You are a data scientist tasked with generating a concise overview based on the provided dataset information. The overview should be verbose enough.

    ### Dataset Overview:
    - **Title**: {dataset_title}
    - **Description**: {dataset_description}
    - **Number of Features**: {num_features}
    - **Label**: {label_name} - {label_description}

    ### Feature Reports:
    {escape_curly_braces(feature_reports_section)}

    ### Label Report:
    {escape_curly_braces(label_report)}

    Remember that summary and conclusion definitions are as follows:

    - **Summary**: Provide a brief, easy-to-read overview of the key findings and main points from the feature reports.
    - **Conclusion**: Offer clear interpretations of the results, implications, and any actionable recommendations based on the analysis.

    The output should be formatted in markdown as follows:

    ## Summary
    -
    -
    
    ## Conclusion

    """)
    return system_prompt

def get_prompt_for_label_explanation(semantic_memory: SemanticMemory):
    system_prompt = generate_dynamic_label_prompt(semantic_memory.reference_dataset.description, semantic_memory.tools)
    final_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "Explain the label '{label_name}' using the following information:\n{input}\n. Think step by step to solve your task"),
        ]
    )
    return final_prompt

def generate_dynamic_label_prompt(dataset_description, tools_description):
    label_name = dataset_description['LABEL']
    label_description = dataset_description['LABEL_DESCRIPTION']
    tool_descriptions = "\n\n".join(
        ["**{tool_name}**:\n{description}".format(
            tool_name=tool_name,
            description=escape_curly_braces(tool_info.description)
        ) for tool_name, tool_info in tools_description.items()]
    )

    system_prompt_template = """
    You are a highly experienced data scientist. Your task is to generate a concise and detailed explanation
    for the label in the **{dataset_title}** dataset. The dataset is described as follows: {dataset_description_text}.
    
    **Label**: {label_name}
    
    **Label Description**:
    {label_description}
    
    **Available Tools**:
    {tool_descriptions}
    
    **Instructions**:
    - Provide a concise and detailed explanation for the label in the dataset.
    - Indicate if there are any problems or issues with the label based on the available information.


    Think step by step to solve your task.
    """
    return system_prompt_template.format(
        dataset_title=dataset_description['DATASET_TITLE'],
        dataset_description_text=dataset_description['DATASET_DESCRIPTION'],
        label_name=label_name,
        label_description=label_description,
        tool_descriptions=tool_descriptions
    )