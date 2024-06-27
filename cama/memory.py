from docarray import BaseDoc, DocList
from typing import Optional, Dict, Any, TypedDict
from cama.insight import QuickInsight, DeepInsight
import pandas as pd
from cama.representation import DatasetRepresentation
from cama.tools import Tool

class CurrentDataset(BaseDoc):
    X: pd.DataFrame
    y: Optional[pd.DataFrame]
    description: dict = None

class EpisodicMemory(BaseDoc):
    current_dataset: CurrentDataset
    quick_insight: Optional[QuickInsight] = None
    deep_insight: Optional[DeepInsight] = None
    task: int = None


class ReferenceDataset(BaseDoc):
    X_train: pd.DataFrame
    X_test: pd.DataFrame
    y_train: pd.Series
    y_test: pd.Series
    description: dict

class SemanticMemory(BaseDoc):
    reference_dataset: ReferenceDataset
    tools: Dict[str, Tool]
    model: Any

class WorkingMemory(TypedDict):
    episodic_memory: DocList[EpisodicMemory]
    semantic_memory: Optional[SemanticMemory]
    found_insight: Optional[bool]
    threshold: float
    slow_tools_results: dict
    fast_tools_results: dict
    generations: Dict[str, Any]
    dataset_representation: DatasetRepresentation
