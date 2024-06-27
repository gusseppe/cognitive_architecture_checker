from docarray import BaseDoc, DocList
from typing import Any, Dict, List, Callable
from cama.tools import Tool
import inspect


class ColumnRepresentation(BaseDoc):
    name: str = None
    description: str = None
    type: str = None
    possible_values: Any = None
    data_type: str = None

    def as_dict(self):
        return {
            'name': self.name,
            'description': self.description,
            'type': self.type,
            'possible_values': self.possible_values,
            'data_type': self.data_type,
        }

class ToolRepresentation(BaseDoc):
    name: str = None
    description: str = None
    result: Any = None

    def as_dict(self):
        return {
            'name': self.name,
            'description': self.description,
            'result': self.result
        }

class FeatureRepresentation(ColumnRepresentation):
    tools_results: DocList[ToolRepresentation]

    def as_dict(self):
        column_metadata = super().as_dict()
        column_metadata['tools_results'] = [tool.as_dict() for tool in self.tools_results]
        return column_metadata

class DatasetRepresentation(BaseDoc):
    name: str = None
    description: str = None
    features: DocList[FeatureRepresentation] = None
    label: ColumnRepresentation = None

    def as_dict(self):
        return {
            'name': self.name,
            'description': self.description,
            'features': [feature.as_dict() for feature in self.features],
            'label': self.label.as_dict()
        }

def get_dataset_representation(semantic_memory, tools_results) -> DatasetRepresentation:
    features_representations = []
    dataset_description = semantic_memory.reference_dataset.description

    for feature_name in dataset_description['FEATURES']:
        type_feature = 'categorical' if feature_name in dataset_description['CATEGORICAL_FEATURES'] else 'numerical'
        tools_results_ = list()
        for tool_name, tool_result in tools_results.items():
            tool_description = semantic_memory.tools[tool_name].description
            tools_results_.append(ToolRepresentation(name=tool_name, description=tool_description, result=tool_result[feature_name]))

        feature = FeatureRepresentation(
            name=feature_name, 
            description=dataset_description['FEATURE_DESCRIPTIONS'][feature_name],
            type=type_feature,
            possible_values=dataset_description['COLUMN_VALUES'][feature_name],
            data_type=dataset_description['COLUMN_TYPES'][feature_name],
            tools_results=DocList[ToolRepresentation](tools_results_)
        )
        features_representations.append(feature)

    label = ColumnRepresentation(
        name=dataset_description['LABEL'],
        description=dataset_description['LABEL_DESCRIPTION'],
        type='categorical',
        possible_values=dataset_description['COLUMN_VALUES'][dataset_description['LABEL']],
        data_type=dataset_description['COLUMN_TYPES'][dataset_description['LABEL']]
    )

    dataset_representation = DatasetRepresentation(
        name=dataset_description['DATASET_TITLE'],
        description=dataset_description['DATASET_DESCRIPTION'],
        features=DocList[FeatureRepresentation](features_representations),
        label=label
    )
    
    return dataset_representation

