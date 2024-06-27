from typing import Dict, Any, List, Callable
import pandas as pd
from evidently import ColumnMapping
from evidently.report import report
from evidently.metric_preset import DataDriftPreset
from IPython.display import display
from alibi.explainers import TreeShap
from docarray import BaseDoc
import inspect


def get_drift_report(
    dataset_description: Dict,
    reference_data: pd.DataFrame,
    current_data: pd.DataFrame,
    drift_share: float,
    show_plot: bool = False
) -> Dict:
    """
    Generate a data drift report using the reference and current datasets. The report includes a general drift summary and detailed drift analysis per column.
    If drift is found it means that the distribution of the data has changed significantly between the reference and current datasets that leads to a decrease in model performance.

    # Input
    - `dataset_description` (dict): A dictionary describing the dataset, including label, numerical and categorical features.
    - `reference_data` (pd.DataFrame): The reference dataset used for training.
    - `current_data` (pd.DataFrame): The new dataset used for inference.
    - `drift_share` (float): The threshold proportion of drifted features to determine if the dataset has drift.
    - `show_plot` (bool): A flag to indicate if the drift report plot should be displayed.

    # Output
    Returns a dictionary with two keys:
    - `dataset` (dict): General drift report summary with the following keys:
        - `drift_share` (float): The calculated drift share.
        - `number_of_columns` (int): Total number of columns analyzed.
        - `number_of_drifted_columns` (int): The number of columns that show drift.
        - `share_of_drifted_columns` (float): The proportion of drifted columns out of the total number of columns.
        - `dataset_drift` (bool): Indicates if dataset drift is detected based on the `drift_share` threshold.
    - `drift_by_columns` (dict): Detailed drift analysis per column, with each column containing:
        - `column_name` (str): Name of the column.
        - `column_type` (str): Type of the column (numerical or categorical).
        - `stattest_name` (str): Name of the statistical test used to detect drift.
        - `stattest_threshold` (float): The statistical test threshold.
        - `drift_score` (float): The calculated drift score.
        - `drift_detected` (bool): Indicates if drift is detected for this column.
        - `current` (dict): Distribution information of the current dataset.
        - `reference` (dict): Distribution information of the reference dataset.


    """
    # Generate column mapping
    column_mapping = ColumnMapping()
    column_mapping.label = dataset_description['LABEL']
    column_mapping.prediction = None
    column_mapping.numerical_features = dataset_description['NUMERICAL_FEATURES']
    column_mapping.categorical_features = dataset_description['CATEGORICAL_FEATURES']

    # Generate drift report
    drift_report = report.Report(metrics=[DataDriftPreset(drift_share=drift_share, stattest='kl_div', stattest_threshold=0.1)])
    drift_report.run(reference_data=reference_data, current_data=current_data, column_mapping=column_mapping)
    if show_plot:
        display(drift_report.show())

    # Extract results
    drift_report_output = {
        'dataset': drift_report.as_dict()['metrics'][0]['result'],
        'drift_by_columns': drift_report.as_dict()['metrics'][1]['result']['drift_by_columns']
    }

    return drift_report_output

def get_shap_values(model: Any, X: pd.DataFrame, dataset_description: Dict) -> Dict[str, float]:
    """
    Calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions.
    This helps detect feature attribution drift if the input data distribution changes, leading to changes in the order of feature contributions.

    # Inputs
    - `model` (Any): The machine learning model to explain (typically a tree-based model like XGBoost, LightGBM, etc.).
    - `X` (pd.DataFrame): A DataFrame containing the input features for which to calculate SHAP values.
    - `dataset_description` (Dict): A dictionary that includes:
        - `CATEGORICAL_FEATURES` (list): List of names of categorical features.

    # Output
    Returns a dictionary with feature names as keys, each containing:
    - `value` (float): Mean(|SHAP value|) for the feature.
    - `position` (int): Rank position of the feature based on its mean Mean(|SHAP value|) value.


    ```
    """
    # Create Tree SHAP explainer
    path_dependent_explainer = TreeShap(
        predictor=model, 
        model_output='raw',
        categorical_names=dataset_description['CATEGORICAL_FEATURES'], 
        task='classification',
        feature_names=X.columns.tolist()
    )
    
    # Fit the explainer
    path_dependent_explainer.fit()
    
    # Get SHAP explanation
    path_dependent_explanation = path_dependent_explainer.explain(X)
    
    # Extract and map feature importances
    raw_importances = path_dependent_explanation.raw['importances']['0']
    shap_values_dict = dict(zip(raw_importances['names'], raw_importances['ranked_effect']))
    shap_values_dict = {k: {'value': v, 'position': i+1} for i, (k, v) in enumerate(shap_values_dict.items())}
    
    return shap_values_dict

class Tool(BaseDoc):
    name: str
    function: Any
    description: str

def get_tools(functions: List[Callable[..., Any]]) -> Dict[str, Tool]:
    tools = {}
    for func in functions:
        tool = Tool(name=func.__name__, function=func, description=inspect.getdoc(func))
        tools[func.__name__] = tool
    return tools
