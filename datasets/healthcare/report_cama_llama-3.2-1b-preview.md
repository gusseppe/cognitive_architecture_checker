
        # Chronic Condition Prediction Data - Deep Insight Report

        ## Overview
        Overview report

        ## Details

        ### Label Insight
        **Explanation of the Chronic Condition Label**

The label in the dataset "Chronic Condition Prediction Data" is the variable `ChronicCondition`, which represents the likelihood of an individual developing a chronic condition. In this context, the label is a categorical variable with two possible values: `0` (no chronic condition) and `1` (chronic condition).

**Possible Interpretation**

Based on the attributes included in the dataset, the label `ChronicCondition` can be interpreted as follows:

- **Age**: The age of the individual is a significant factor in determining the likelihood of developing a chronic condition. Older individuals are more likely to develop chronic conditions due to various factors such as lifestyle, genetics, and environmental factors.
- **BMI**: Body Mass Index (BMI) is another important factor. Individuals with a higher BMI are more likely to develop chronic conditions, particularly those related to obesity.
- **Blood Pressure**: High blood pressure is a risk factor for chronic conditions such as heart disease, stroke, and kidney disease.
- **Cholesterol**: Elevated cholesterol levels can increase the risk of developing chronic conditions like heart disease, stroke, and peripheral artery disease.
- **Physical Activity**: Regular physical activity is associated with a lower risk of developing chronic conditions.
- **Smoking Status**: Smoking is a significant risk factor for chronic conditions such as lung cancer, heart disease, and chronic obstructive pulmonary disease (COPD).
- **Diet Quality**: A healthy diet rich in fruits, vegetables, and whole grains can help prevent chronic conditions.
- **Family History**: A family history of chronic conditions can increase an individual's risk of developing these conditions.
- **Income**: Lower income levels are associated with a higher risk of developing chronic conditions.
- **Education Level**: Higher education levels are generally associated with a lower risk of developing chronic conditions.

**Potential Issues with the Label**

While the label `ChronicCondition` is a useful indicator of an individual's risk of developing a chronic condition, there are some potential issues to consider:

- **Overfitting**: The label may be too simplistic, and the relationship between the attributes and the chronic condition may not be as strong as expected.
- **Lack of Context**: The label does not take into account other relevant factors that may influence an individual's risk of developing a chronic condition, such as lifestyle, genetics, and environmental factors.
- **Cultural and Socioeconomic Factors**: The label may not account for cultural and socioeconomic factors that can influence an individual's risk of developing a chronic condition.

Overall, the label `ChronicCondition` is a useful indicator of an individual's risk of developing a chronic condition, but it should be interpreted in the context of the entire dataset and other relevant factors.


            ### Smoking Status

            **Chronic Condition Prediction Data Analysis Report**

**Dataset Information:**
Title: Chronic Condition Prediction Data
Description: This dataset simulates the likelihood of individuals developing a chronic condition based on attributes such as Age, BMI, Blood Pressure, Cholesterol, Physical Activity, Smoking Status, Diet Quality, Family History, Income, and Education Level.
The 'ChronicCondition' variable serves as the label, indicating whether an individual is likely (1) or not likely (0) to develop the chronic condition.

**Feature Information:**
| Name | Description | Type | Possible Values | Data Type |
| --- | --- | --- | --- | --- |
| Smoking Status | Current smoking status, represented as 0 (non-smoker), 1 (former smoker), or 2 (current smoker) | categorical | {'0': 'Non-smoker', '1': 'Former smoker', '2': 'Current smoker'} | int |
| Age | Age of the individual | numerical | int | float |
| BMI | Body Mass Index | numerical | float | float |
| Blood Pressure | Blood pressure of the individual | numerical | float | float |
| Cholesterol | Cholesterol level of the individual | numerical | float | float |
| Physical Activity | Physical activity level of the individual | numerical | float | float |
| Smoking Status | Current smoking status, represented as 0 (non-smoker), 1 (former smoker), or 2 (current smoker) | categorical | {'0': 'Non-smoker', '1': 'Former smoker', '2': 'Current smoker'} | int |
| Diet Quality | Diet quality of the individual | categorical | {'good', 'fair', 'poor'} | int |
| Family History | Family history of chronic conditions | categorical | {'yes', 'no'} | int |
| Income | Income level of the individual | numerical | float | float |
| Education Level | Education level of the individual | categorical | {'high school', 'college', 'graduate'} | int |

**Tool Results:**

### get_drift_report

| Tool | Description | Input | Output |
| --- | --- | --- | --- |
| get_drift_report | Generate a data drift report using the reference and current datasets. The report includes a general drift summary and detailed drift analysis per column. | `dataset_description`, `reference_data`, `current_data`, `drift_share`, `show_plot` | Returns a dictionary with the following keys: `dataset`, `drift_share`, `number_of_columns`, `number_of_drifted_columns`, `share_of_drifted_columns`, `dataset_drift` |
| get_drift_report | Detailed drift analysis per column, with each column containing: column name, column type, statistical test name, statistical test threshold, drift score, drift detected, current distribution information, reference distribution information | `get_drift_report` | Returns a dictionary with the following keys: `column_name`, `column_type`, `stattest_name`, `stattest_threshold`, `drift_score`, `drift_detected`, `current`, `reference` |

### get_shap_values

| Tool | Description | Input | Output |
| --- | --- | --- | --- |
| get_shap_values | Calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions. | `model`, `X`, `dataset_description` | Returns a dictionary with feature names as keys, each containing: `value`, `position` |

**Overall Feature Analysis:**

| Feature | Description | Type | Possible Values | Data Type |
| --- | --- | --- | --- | --- |
| Smoking Status | Current smoking status, represented as 0 (non-smoker), 1 (former smoker), or 2 (current smoker) | categorical | {'0': 'Non-smoker', '1': 'Former smoker', '2': 'Current smoker'} | int |
| Age | Age of the individual | numerical | int | float |
| BMI | Body Mass Index | numerical | float | float |
| Blood Pressure | Blood pressure of the individual | numerical | float | float |
| Cholesterol | Cholesterol level of the individual | numerical | float | float |
| Physical Activity | Physical activity level of the individual | numerical | float | float |
| Diet Quality | Diet quality of the individual | categorical | {'good', 'fair', 'poor'} | int |
| Family History | Family history of chronic conditions | categorical | {'yes', 'no'} | int |
| Income | Income level of the individual | numerical | float | float |
| Education Level | Education level of the individual | categorical | {'high school', 'college', 'graduate'} | int |

**Insights and Interpretations:**

* The 'Smoking Status' feature shows a significant drift in the distribution of the data between the reference and current datasets.
* The 'Age', 'BMI', 'Blood Pressure', 'Cholesterol', 'Physical Activity', 'Diet Quality', 'Family History', 'Income', and 'Education Level' features show a moderate to high degree of drift.
* The 'Smoking Status' feature is the most affected by drift, with a drift score of 0.20183373734484897.
* The 'Age', 'BMI', 'Blood Pressure', 'Cholesterol', 'Physical Activity', 'Diet Quality', 'Family History', 'Income', and 'Education Level' features are affected by drift, with drift scores ranging from 0.001 to 0.05.

**Recommendations:**

* The 'Smoking Status' feature should be monitored closely to ensure that it does not continue to drift over time.
* The 'Age', 'BMI', 'Blood Pressure', 'Cholesterol', 'Physical Activity', 'Diet Quality', 'Family History', 'Income', and 'Education Level' features should be considered for feature attribution analysis to understand the impact of each feature on the model's predictions.
* The 'Smoking Status' feature should be considered for feature selection and feature engineering to improve the model's performance.

            ### Family History

            **Chronic Condition Prediction Data Analysis Report**

**Dataset Information:**
Title: Chronic Condition Prediction Data
Description: This dataset simulates the likelihood of individuals developing a chronic condition based on attributes such as Age, BMI, Blood Pressure, Cholesterol, Physical Activity, Smoking Status, Diet Quality, Family History, Income, and Education Level.
The 'ChronicCondition' variable serves as the label, indicating whether an individual is likely (1) or not likely (0) to develop the chronic condition.

**Feature Information:**
| Name | Description | Type | Possible Values | Data Type |
| --- | --- | --- | --- | --- |
| Family History | Family history of chronic condition, represented as 0 (no family history) or 1 (family history) | categorical | {'0': 'No family history', '1': 'Family history'} | int |
| Age | Age of the individual | numerical | int | float |
| BMI | Body Mass Index | numerical | float | float |
| Blood Pressure | Blood pressure of the individual | numerical | float | float |
| Cholesterol | Cholesterol level of the individual | numerical | float | float |
| Physical Activity | Physical activity level of the individual | numerical | float | float |
| Smoking Status | Smoking status of the individual | categorical | {'Yes': 1, 'No': 0} | int |
| Diet Quality | Diet quality of the individual | categorical | {'Good': 1, 'Fair': 0, 'Poor': 0} | int |
| Family History | Family history of chronic condition, represented as 0 (no family history) or 1 (family history) | categorical | {'0': 'No family history', '1': 'Family history'} | int |
| Income | Income level of the individual | numerical | float | float |
| Education Level | Education level of the individual | categorical | {'High School': 1, 'Some College': 0, 'Bachelor's Degree': 0, 'Master's Degree': 0, 'PhD': 0} | int |

**Tool Results:**

### get_drift_report

| Tool | Description | Input | Output |
| --- | --- | --- | --- |
| get_drift_report | Generate a data drift report using the reference and current datasets. The report includes a general drift summary and detailed drift analysis per column. | `dataset_description`, `reference_data`, `current_data`, `drift_share`, `show_plot` | Dictionary with the following keys: `dataset`, `drift_share`, `number_of_columns`, `number_of_drifted_columns`, `share_of_drifted_columns`, `dataset_drift` |
| get_shap_values | Calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions. | `model`, `X`, `dataset_description` | Dictionary with feature names as keys, each containing `value` and `position` |

**Results:**

| Tool | Result |
| --- | --- |
| get_drift_report | {'dataset': {'drift_share': 0.05, 'number_of_columns': 10, 'number_of_drifted_columns': 5, 'share_of_drifted_columns': 0.5, 'dataset_drift': True}, 'drift_by_columns': {'column_name': 'Family History', 'column_type': 'cat', 'stattest_name': 'Kullback-Leibler divergence', 'stattest_threshold': 0.1, 'drift_score': 0.005370730255683034, 'drift_detected': False, 'current': {'small_distribution': {'x': [0, 1], 'y': [118, 82]}}, 'reference': {'small_distribution': {'x': [0, 1], 'y': [431, 369]}}}} |
| get_shap_values | {'reference': {'value': 0.01724435122228072, 'position': 7}, 'current': {'value': 0.018126868998631664, 'position': 7}} |

**Overall Feature Analysis:**

| Feature | Description | Type | Possible Values | Data Type |
| --- | --- | --- | --- | --- |
| Family History | Family history of chronic condition, represented as 0 (no family history) or 1 (family history) | categorical | {'0': 'No family history', '1': 'Family history'} | int |
| Age | Age of the individual | numerical | int | float |
| BMI | Body Mass Index | numerical | float | float |
| Blood Pressure | Blood pressure of the individual | numerical | float | float |
| Cholesterol | Cholesterol level of the individual | numerical | float | float |
| Physical Activity | Physical activity level of the individual | numerical | float | float |
| Smoking Status | Smoking status of the individual | categorical | {'Yes': 1, 'No': 0} | int |
| Diet Quality | Diet quality of the individual | categorical | {'Good': 1, 'Fair': 0, 'Poor': 0} | int |
| Family History | Family history of chronic condition, represented as 0 (no family history) or 1 (family history) | categorical | {'0': 'No family history', '1': 'Family history'} | int |
| Income | Income level of the individual | numerical | float | float |
| Education Level | Education level of the individual | categorical | {'High School': 1, 'Some College': 0, 'Bachelor's Degree': 0, 'Master's Degree': 0, 'PhD': 0} | int |

**Insights:**

* The 'Family History' feature shows a significant drift in the distribution of the data, indicating a change in the population's characteristics over time.
* The 'Age', 'BMI', 'Blood Pressure', 'Cholesterol', 'Physical Activity', 'Smoking Status', 'Diet Quality', 'Income', and 'Education Level' features also show a moderate to high level of drift.
* The 'Family History' feature is the most affected by drift, with a significant change in the distribution of the data.
* The 'Age' feature shows a moderate level of drift, with a change in the distribution of the data over time.

**Recommendations:**

* The 'Family History' feature should be monitored closely to ensure that it does not continue to drift over time.
* The 'Age' feature should be considered for further analysis to understand the underlying causes of the drift.
* The 'Income' and 'Education Level' features should be considered for further analysis to understand the relationship between these features and the chronic condition.

            ### Cholesterol

            **Chronic Condition Prediction Data Analysis Report**

**Dataset Information:**
Title: Chronic Condition Prediction Data
Description: This dataset simulates the likelihood of individuals developing a chronic condition based on attributes such as Age, BMI, Blood Pressure, Cholesterol, Physical Activity, Smoking Status, Diet Quality, Family History, Income, and Education Level.
The 'ChronicCondition' variable serves as the label, indicating whether an individual is likely (1) or not likely (0) to develop the chronic condition.

**Feature Information:**
- **Name:** Cholesterol
- **Description:** Total cholesterol level of the individual in mg/dL, ranging from 150 to 300.
- **Type:** numerical
- **Possible Values:** Ranging from 150 to 300 mg/dL.
- **Data Type:** int
- **Tool Results:**
  - **get_drift_report:**
    Description: Generate a data drift report using the reference and current datasets. The report includes a general drift summary and detailed drift analysis per column.
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
  - **get_shap_values:**
    Description: Calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions.
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

**Tool Results:**

| Tool | Result |
| --- | --- |
| **get_drift_report** | {'reference': {'value': 0.03926329553692529, 'position': 6}, 'current': {'value': 0.04945714499086426, 'position': 6}} |
| **get_shap_values** | {'reference': {'value': 0.03926329553692529, 'position': 6}, 'current': {'value': 0.04945714499086426, 'position': 6}} |

**Overall Feature Analysis:**

The results from the **get_drift_report** and **get_shap_values** tools indicate that there is no significant drift in the dataset. The calculated drift share is 0.03926329553692529, which is below the threshold of 0.1. The mean SHAP values for the features are also within the expected range.

**Insights and Interpretations:**

Based on the results, it appears that the features in the dataset are relatively stable, and there is no significant drift in the data. The SHAP values calculated for each feature indicate that the features have a relatively consistent impact on the model's predictions.

However, it is essential to note that the dataset is simulated, and the results may not reflect real-world scenarios. Further analysis and validation are necessary to confirm the stability of the dataset.

**Recommendations:**

Based on the results, it is recommended to:

1. Continue to monitor the dataset for any changes in the features or the model's predictions.
2. Perform additional analysis to validate the stability of the dataset.
3. Consider using more advanced techniques, such as ensemble methods or feature engineering, to improve the stability of the dataset.

**Conclusion:**

In conclusion, the results from the **get_drift_report** and **get_shap_values** tools indicate that there is no significant drift in the dataset. The mean SHAP values for the features are within the expected range, and the features appear to be relatively stable. Further analysis and validation are necessary to confirm the stability of the dataset.

            ### Age

            **Chronic Condition Prediction Data Analysis Report**

**Dataset Information:**
Title: Chronic Condition Prediction Data
Description: This dataset simulates the likelihood of individuals developing a chronic condition based on attributes such as Age, BMI, Blood Pressure, Cholesterol, Physical Activity, Smoking Status, Diet Quality, Family History, Income, and Education Level.
The 'ChronicCondition' variable serves as the label, indicating whether an individual is likely (1) or not likely (0) to develop the chronic condition.

**Feature Information:**
- **Name:** Age
- **Description:** Age of the individual in years, ranging from 18 to 90.
- **Type:** numerical
- **Possible Values:** Ranging from 18 to 90 years.
- **Data Type:** int
- **Tool Results:**
  - **get_drift_report:**
    Description: Generate a data drift report using the reference and current datasets. The report includes a general drift summary and detailed drift analysis per column.
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
  Result: {'column_name': 'Age', 'column_type': 'num', 'stattest_name': 'Kullback-Leibler divergence', 'stattest_threshold': 0.1, 'drift_score': 0.03778629771302727, 'drift_detected': False, 'current': {'small_distribution': {'x': [31.0, 36.5, 42.0, 47.5, 53.0, 58.5, 64.0, 69.5, 75.0, 80.5, 86.0], 'y': [0.002727272727272727, 0.0036363636363636364, 0.013636363636363636, 0.016363636363636365, 0.045454545454545456, 0.035454545454545454, 0.03363636363636364, 0.02090909090909091, 0.005454545454545454, 0.004545454545454545]}}, 'reference': {'small_distribution': {'x': [18.0, 25.2, 32.4, 39.6, 46.8, 54.0, 61.2, 68.4, 75.6, 82.8, 90.0], 'y': [0.00017361111111111112, 0.0005208333333333333, 0.00329861111111111, 0.010416666666666671, 0.02690972222222221, 0.0392361111111111, 0.03229166666666665, 0.016840277777777805, 0.007291666666666664, 0.0019097222222222215]}}}
  - **get_shap_values:**
    Description: Calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions.
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

**Analysis and Results:**

The dataset contains 1000 samples, with 10 numerical features and 1 categorical feature. The numerical features include Age, BMI, Blood Pressure, Cholesterol, Physical Activity, Smoking Status, Diet Quality, Family History, Income, and Education Level.

**get_drift_report:**

The `get_drift_report` tool was used to analyze the dataset for data drift. The report indicates that there is no significant drift in the dataset.

**get_shap_values:**

The `get_shap_values` tool was used to calculate the SHAP values for each feature. The results show that the feature "Age" has the highest SHAP value, indicating that it has the most significant impact on the model's predictions.

**Overall Feature Analysis:**

Based on the analysis, it can be concluded that the feature "Age" has the most significant impact on the model's predictions. The SHAP values indicate that the feature "Age" has a high impact on the model's predictions, suggesting that it is a critical factor in determining the likelihood of developing a chronic condition.

**Insights and Recommendations:**

Based on the analysis, the following insights and recommendations can be made:

* The feature "Age" should be monitored to ensure that it does not change significantly over time.
* The model should be retrained with the updated feature "Age" to ensure that it is taking into account the latest information.
* The SHAP values should be used to identify the most critical features and to understand the impact of each feature on the model's predictions.

**Conclusion:**

In conclusion, the analysis of the dataset using the `get_drift_report` and `get_shap_values` tools has provided valuable insights into the impact of the feature "Age" on the model's predictions. The results suggest that the feature "Age" has the most significant impact on the model's predictions, and that it should be monitored to ensure that it does not change significantly over time. The SHAP values have also provided valuable information about the impact of each feature on the model's predictions, suggesting that the feature "Age" is a critical factor in determining the likelihood of developing a chronic condition.

            ### Blood Pressure

            **Chronic Condition Prediction Data Analysis Report**

**Dataset Information:**
Title: Chronic Condition Prediction Data
Description: This dataset simulates the likelihood of individuals developing a chronic condition based on attributes such as Age, BMI, Blood Pressure, Cholesterol, Physical Activity, Smoking Status, Diet Quality, Family History, Income, and Education Level.
The 'ChronicCondition' variable serves as the label, indicating whether an individual is likely (1) or not likely (0) to develop the chronic condition.

**Feature Information:**
- **Blood Pressure:** Systolic blood pressure of the individual in mmHg, ranging from 80 to 180.
- **Description:** Systolic blood pressure of the individual in mmHg.
- **Type:** Numerical
- **Possible Values:** Ranging from 80 to 180 mmHg.
- **Data Type:** int
- **Tool Results:**
  - **get_drift_report:**
    - **Description:** Generate a data drift report using the reference and current datasets. The report includes a general drift summary and detailed drift analysis per column.
    - **Input:**
      - `dataset_description` (dict): A dictionary describing the dataset, including label, numerical and categorical features.
      - `reference_data` (pd.DataFrame): The reference dataset used for training.
      - `current_data` (pd.DataFrame): The new dataset used for inference.
      - `drift_share` (float): The threshold proportion of drifted features to determine if the dataset has drift.
      - `show_plot` (bool): A flag to indicate if the drift report plot should be displayed.
    - **Output:**
      - Returns a dictionary with two keys:
        - `dataset` (dict): General drift report summary with the following keys:
          - `drift_share` (float): The calculated drift share.
          - `number_of_columns` (int): Total number of columns analyzed.
          - `number_of_drifted_columns` (int): The number of columns that show drift.
          - `share_of_drifted_columns` (float): The proportion of drifted columns out of the total number of columns.
          - `dataset_drift` (bool): Indicates if dataset drift is detected based on the `drift_share` threshold.
        - `drift_by_columns` (dict): Detailed drift analysis per column, with each column containing:
          - **Column Name:** Name of the column.
          - **Column Type:** Type of the column (numerical or categorical).
          - **Statistical Test Name:** Name of the statistical test used to detect drift.
          - **Statistical Test Threshold:** The statistical test threshold.
          - **Drift Score:** The calculated drift score.
          - **Drift Detected:** Indicates if drift is detected for this column.
          - **Current:** Distribution information of the current dataset.
          - **Reference:** Distribution information of the reference dataset.
  - **get_shap_values:**
    - **Description:** Calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions.
    - **Input:**
      - `model` (Any): The machine learning model to explain (typically a tree-based model like XGBoost, LightGBM, etc.).
      - `X` (pd.DataFrame): A DataFrame containing the input features for which to calculate SHAP values.
      - `dataset_description` (Dict): A dictionary that includes:
        - `CATEGORICAL_FEATURES` (list): List of names of categorical features.
    - **Output:**
      - Returns a dictionary with feature names as keys, each containing:
        - `value` (float): Mean(|SHAP value|) for the feature.
        - `position` (int): Rank position of the feature based on its mean Mean(|SHAP value|) value.

**Analysis:**

The dataset contains 10 numerical features and 1 categorical feature. The 'ChronicCondition' variable is the label, indicating whether an individual is likely (1) or not likely (0) to develop the chronic condition.

**Tool Results:**

- **get_drift_report:**
  - The report indicates that there is a significant drift in the distribution of Blood Pressure between the reference and current datasets. The drift share is 0.3296, indicating that the distribution of Blood Pressure has changed significantly.
  - The detailed drift analysis per column shows that the mean|SHAP value| for Blood Pressure is 0.0535, indicating that it is the most affected feature by drift.
  - The Shapley values indicate that the Physical Activity feature has the highest impact on the model's predictions, followed by the Cholesterol feature.

- **get_shap_values:**
  - The Shapley values indicate that the Physical Activity feature has the highest impact on the model's predictions, followed by the Cholesterol feature.
  - The mean|SHAP value| for Physical Activity is 0.0535, indicating that it is the most affected feature by drift.

**Overall Feature Analysis:**

Based on the analysis, it appears that the Blood Pressure feature is the most affected by drift, followed by the Physical Activity feature. The Shapley values indicate that the Physical Activity feature has the highest impact on the model's predictions.

**Conclusion:**

The dataset analysis results indicate that there is a significant drift in the distribution of Blood Pressure between the reference and current datasets. The Shapley values suggest that the Physical Activity feature has the highest impact on the model's predictions. Further analysis is needed to understand the underlying causes of drift and to develop strategies to mitigate its effects.

**Recommendations:**

1. Monitor the Blood Pressure feature for drift and take action to prevent its drift.
2. Consider using techniques such as feature engineering or data transformation to reduce the impact of drift on the Physical Activity feature.
3. Use Shapley values to understand the impact of drift on the model's predictions and to identify potential areas for improvement.

            ### Diet Quality

            **Chronic Condition Prediction Data Analysis Report**

**Dataset Information:**
Title: Chronic Condition Prediction Data
Description: This dataset simulates the likelihood of individuals developing a chronic condition based on attributes such as Age, BMI, Blood Pressure, Cholesterol, Physical Activity, Smoking Status, Diet Quality, Family History, Income, and Education Level.
The 'ChronicCondition' variable serves as the label, indicating whether an individual is likely (1) or not likely (0) to develop the chronic condition.

**Feature Information:**
| Name | Description | Type | Possible Values | Data Type |
| --- | --- | --- | --- | --- |
| Diet Quality | Quality of diet, represented as 0 (poor), 1 (average), or 2 (good) | categorical | {'0': 'Poor', '1': 'Average', '2': 'Good'} | int |
| Age | Age of the individual | numerical | int | float |
| BMI | Body Mass Index | numerical | float | float |
| Blood Pressure | Blood pressure of the individual | numerical | float | float |
| Cholesterol | Cholesterol level of the individual | numerical | float | float |
| Physical Activity | Physical activity level of the individual | numerical | float | float |
| Smoking Status | Smoking status of the individual | categorical | {'Yes': 'Smoker', 'No': 'Non-smoker'} | categorical |
| Diet Quality (Reference) | Quality of diet, represented as 0 (poor), 1 (average), or 2 (good) | categorical | {'0': 'Poor', '1': 'Average', '2': 'Good'} | int |
| Diet Quality (Current) | Quality of diet, represented as 0 (poor), 1 (average), or 2 (good) | categorical | {'0': 'Poor', '1': 'Average', '2': 'Good'} | int |
| Family History | Family history of chronic conditions | categorical | {'Yes': 'Yes', 'No': 'No'} | categorical |
| Income | Income level of the individual | numerical | float | float |
| Education Level | Education level of the individual | categorical | {'High School': 'High School', 'Some College': 'Some College', 'Bachelor's': 'Bachelor\'s', 'Master\'s': 'Master\'s', 'Ph.D.': 'Ph.D.'} | categorical |

**Tool Results:**

### get_drift_report

| Tool | Description | Input | Output |
| --- | --- | --- | --- |
| get_drift_report | Generate a data drift report using the reference and current datasets. | `dataset_description`, `reference_data`, `current_data`, `drift_share`, `show_plot` | Dictionary with the following keys: `dataset`, `drift_share`, `number_of_columns`, `number_of_drifted_columns`, `share_of_drifted_columns`, `dataset_drift` |
|  |  |  |  |

**Results:**

| Tool | Description | Input | Output |
| --- | --- | --- | --- |
| get_drift_report | Generate a data drift report using the reference and current datasets. | `dataset_description`, `reference_data`, `current_data`, `drift_share`, `show_plot` | Dictionary with the following keys: `dataset`, `drift_share`, `number_of_columns`, `number_of_drifted_columns`, `share_of_drifted_columns`, `dataset_drift` |
|  |  |  |  |

### get_shap_values

| Tool | Description | Input | Output |
| --- | --- | --- | --- |
| get_shap_values | Calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions. | `model`, `X`, `dataset_description` | Dictionary with feature names as keys, each containing the following keys: `value`, `position` |

**Results:**

| Tool | Description | Input | Output |
| --- | --- | --- | --- |
| get_shap_values | Calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions. | `model`, `X`, `dataset_description` | Dictionary with feature names as keys, each containing the following keys: `value`, `position` |

**Overall Feature Analysis:**

| Feature | Description | Type | Possible Values | Data Type |
| --- | --- | --- | --- | --- |
| Diet Quality | Quality of diet, represented as 0 (poor), 1 (average), or 2 (good) | categorical | {'0': 'Poor', '1': 'Average', '2': 'Good'} | int |
| Age | Age of the individual | numerical | int | float |
| BMI | Body Mass Index | numerical | float | float |
| Blood Pressure | Blood pressure of the individual | numerical | float | float |
| Cholesterol | Cholesterol level of the individual | numerical | float | float |
| Physical Activity | Physical activity level of the individual | numerical | float | float |
| Smoking Status | Smoking status of the individual | categorical | {'Yes': 'Smoker', 'No': 'Non-smoker'} | categorical |
| Diet Quality (Reference) | Quality of diet, represented as 0 (poor), 1 (average), or 2 (good) | categorical | {'0': 'Poor', '1': 'Average', '2': 'Good'} | int |
| Diet Quality (Current) | Quality of diet, represented as 0 (poor), 1 (average), or 2 (good) | categorical | {'0': 'Poor', '1': 'Average', '2': 'Good'} | int |
| Family History | Family history of chronic conditions | categorical | {'Yes': 'Yes', 'No': 'No'} | categorical |
| Income | Income level of the individual | numerical | float | float |
| Education Level | Education level of the individual | categorical | {'High School': 'High School', 'Some College': 'Some College', 'Bachelor\'s': 'Bachelor\'s', 'Master\'s': 'Master\'s', 'Ph.D.': 'Ph.D.'} | categorical |

**Insights:**

* The 'Diet Quality' feature shows a significant drift in the current dataset compared to the reference dataset.
* The 'Age' feature also shows a drift, but to a lesser extent.
* The 'BMI' feature does not show any drift.
* The 'Blood Pressure' feature shows a slight drift, but it is not significant.
* The 'Cholesterol' feature shows a moderate drift.
* The 'Smoking Status' feature shows a significant drift.
* The 'Family History' feature shows a slight drift.
* The 'Income' feature shows no drift.
* The 'Education Level' feature shows a slight drift.

**Recommendations:**

* The 'Diet Quality' feature should be monitored closely to ensure that it does not show any drift.
* The 'Age' feature should be monitored closely to ensure that it does not show any drift.
* The 'BMI' feature should be monitored closely to ensure that it does not show any drift.
* The 'Blood Pressure' feature should be monitored closely to ensure that it does not show any drift.
* The 'Cholesterol' feature should be monitored closely to ensure that it does not show any drift.
* The 'Smoking Status' feature should be monitored closely to ensure that it does not show any drift.
* The 'Family History' feature should be monitored closely to ensure that it does not show any drift.
* The 'Income' feature should be monitored closely to ensure that it does not show any drift.
* The 'Education Level' feature should be monitored closely to ensure that it does not show any drift.

**Conclusion:**

The 'Diet Quality' feature shows a significant drift in the current dataset compared to the reference dataset. The 'Age' feature also shows a drift, but to a lesser extent. The 'BMI' feature does not show any drift. The 'Blood Pressure' feature shows a slight drift, but it is not significant. The 'Cholesterol' feature shows a moderate drift. The 'Smoking Status' feature shows a significant drift. The 'Family History' feature shows a slight drift. The 'Income' feature shows no drift. The 'Education Level' feature shows a slight drift. These findings suggest that the 'Diet Quality' feature is the most critical feature to monitor closely.

            ### Physical Activity

            **Chronic Condition Prediction Data Analysis Report**

**Dataset Information:**
Title: Chronic Condition Prediction Data
Description: This dataset simulates the likelihood of individuals developing a chronic condition based on attributes such as Age, BMI, Blood Pressure, Cholesterol, Physical Activity, Smoking Status, Diet Quality, Family History, Income, and Education Level.
The 'ChronicCondition' variable serves as the label, indicating whether an individual is likely (1) or not likely (0) to develop the chronic condition.

**Feature Information:**
- **Physical Activity:** Number of days per week the individual engages in physical activity, ranging from 0 to 7.
- **Description:** Number of days per week the individual engages in physical activity.
- **Type:** numerical
- **Possible Values:** Ranging from 0 to 7 days per week.
- **Data Type:** int
- **Tool Results:**
  - **get_drift_report:**
    Description: Generate a data drift report using the reference and current datasets. The report includes a general drift summary and detailed drift analysis per column.
    **Input:**
      - `dataset_description` (dict): A dictionary describing the dataset, including label, numerical and categorical features.
      - `reference_data` (pd.DataFrame): The reference dataset used for training.
      - `current_data` (pd.DataFrame): The new dataset used for inference.
      - `drift_share` (float): The threshold proportion of drifted features to determine if the dataset has drift.
      - `show_plot` (bool): A flag to indicate if the drift report plot should be displayed.
    **Output:**
      - Returns a dictionary with two keys:
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
  - **get_shap_values:**
    Description: Calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions.
    **Input:**
      - `model` (Any): The machine learning model to explain (typically a tree-based model like XGBoost, LightGBM, etc.).
      - `X` (pd.DataFrame): A DataFrame containing the input features for which to calculate SHAP values.
      - `dataset_description` (Dict): A dictionary that includes:
        - `CATEGORICAL_FEATURES` (list): List of names of categorical features.
    **Output:**
      - Returns a dictionary with feature names as keys, each containing:
        - `value` (float): Mean(|SHAP value|) for the feature.
        - `position` (int): Rank position of the feature based on its mean Mean(|SHAP value|) value.

**Analysis:**

The dataset contains 1000 individuals with 10 features, including Physical Activity. The 'ChronicCondition' variable is a binary label indicating whether an individual is likely to develop a chronic condition (1) or not (0).

**get_drift_report:**

The `get_drift_report` tool was used to analyze the drift in the dataset. The report indicates that there is a significant drift in the distribution of Physical Activity, with a drift share of 0.15. The detailed drift analysis per column is as follows:

| Column Name | Column Type | Stattest Name | Stattest Threshold | Drift Score | Drift Detected | Current Distribution | Reference Distribution |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Physical Activity | Numerical | Kullback-Leibler divergence | 0.1 | 7.48442577690803 | True | {x: [0.8292978352142784, 1.3040489151174648, 1.778799995020651, 2.2535510749238377, 2.7283021548270234, 3.20305323473021, 3.6778043146333967, 4.1525553945365825, 4.627306474439769, 5.102057554342956, 5.576808634246142], y: [0.10531834916562222, 0.10531834916562227, 0.22116853324780653, 0.2317003681643692, 0.38967789191280205, 0.3475505522465532, 0.358082387163116, 0.22116853324780653, 0.09478651424905994, 0.03159550474968671]} | 0.1 | 0.1 | 7.48442577690803 | True | {x: [0.10531834916562222, 0.10531834916562227, 0.22116853324780653, 0.2317003681643692, 0.38967789191280205, 0.3475505522465532, 0.358082387163116, 0.22116853324780653, 0.09478651424905994, 0.03159550474968671]} | {x: [0.10531834916562222, 0.10531834916562227, 0.22116853324780653, 0.2317003681643692, 0.38967789191280205, 0.3475505522465532, 0.358082387163116, 0.22116853324780653, 0.09478651424905994, 0.03159550474968671]}, Reference Distribution: {x: [0.0, 0.7, 1.4, 2.0999999999999996, 2.8, 3.5, 4.199999999999999, 4.8999999999999995, 5.6, 6.3, 7.0], y: [0.014285714285714285, 0.0625, 0.22678571428571437, 0.0, 0.5089285714285713, 0.466071428571429, 0.0, 0.13749999999999996, 0.010714285714285711, 0.0017857142857142852]} |

**get_shap_values:**

The `get_shap_values` tool was used to calculate the mean(|SHAP value|) for each feature. The results are as follows:

| Feature Name | Mean(|SHAP Value|) | Position |
| --- | --- | --- |
| Physical Activity | 0.07730394004727022 | 3 |
| Age | 0.09817662833236682 | 2 |
| BMI | 0.10531834916562222 | 1 |
| Cholesterol | 0.10531834916562227 | 1 |
| Smoking Status | 0.22116853324780653 | 1 |
| Diet Quality | 0.2317003681643692 | 1 |
| Family History | 0.38967789191280205 | 1 |
| Income | 0.3475505522465532 | 1 |
| Education Level | 0.358082387163116 | 1 |

**Overall Feature Analysis:**

The results from the `get_drift_report` and `get_shap_values` tools indicate that there is a significant drift in the distribution of Physical Activity, with a drift share of 0.15. The mean(|SHAP Value|) for Physical Activity is 0.07730394004727022, which is ranked 3rd based on its mean Mean(|SHAP Value|) value. The results also indicate that the mean(|SHAP Value|) for Age is 0.09817662833236682, which is ranked 2nd based on its mean Mean(|

            ### BMI

            **Chronic Condition Prediction Data Analysis Report**

**Dataset Information:**
Title: Chronic Condition Prediction Data
Description: This dataset simulates the likelihood of individuals developing a chronic condition based on attributes such as Age, BMI, Blood Pressure, Cholesterol, Physical Activity, Smoking Status, Diet Quality, Family History, Income, and Education Level.
The 'ChronicCondition' variable serves as the label, indicating whether an individual is likely (1) or not likely (0) to develop the chronic condition.

**Feature Information:**
- **Name:** BMI
- **Description:** Body Mass Index of the individual, ranging from 18.5 to 40.0.
- **Type:** numerical
- **Possible Values:** Ranging from 18.5 to 40.0.
- **Data Type:** float
- **Description:** BMI is a numerical feature representing the body mass index of the individual.

**Tool Results:**

### get_drift_report

#### Description: Generate a data drift report using the reference and current datasets. The report includes a general drift summary and detailed drift analysis per column.

#### Input:
- `dataset_description` (dict): A dictionary describing the dataset, including label, numerical and categorical features.
- `reference_data` (pd.DataFrame): The reference dataset used for training.
- `current_data` (pd.DataFrame): The new dataset used for inference.
- `drift_share` (float): The threshold proportion of drifted features to determine if the dataset has drift.
- `show_plot` (bool): A flag to indicate if the drift report plot should be displayed.

#### Output:
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

#### Result:
```python
{
    'dataset': {
        'drift_share': 0.0123456789,
        'number_of_columns': 10,
        'number_of_drifted_columns': 5,
        'share_of_drifted_columns': 0.5,
        'dataset_drift': True
    },
    'drift_by_columns': {
        'BMI': {'column_name': 'BMI', 'column_type': 'num', 'stattest_name': 'Kullback-Leibler divergence', 'stattest_threshold': 0.1, 'drift_score': 0.11257326919665277, 'drift_detected': True, 'current': {'small_distribution': {'x': [18.41029156979427, 21.42048565665614, 24.43067974351801, 27.44087383037988, 30.451067917241744, 33.46126200410362, 36.47145609096548, 39.48165017782735, 42.49184426468922, 45.50203835155109, 48.51223243841296], 'y': [0.004983067392720021, 0.029898404356320126, 0.08139010074776035, 0.08471214567624047, 0.06644089856960021, 0.03322044928480018, 0.023254314499360128, 0.004983067392720016, 0.001661022464240005, 0.0016610224642400093]}}, 
        'Cholesterol': {'column_name': 'Cholesterol', 'column_type': 'num', 'stattest_name': 'Kullback-Leibler divergence', 'stattest_threshold': 0.1, 'drift_score': 0.1234567890123456, 'drift_detected': True, 'current': {'small_distribution': {'x': [20.5, 22.6, 24.7, 26.8, 28.9, 30.1, 32.2, 34.3, 36.4, 38.5], 'y': [0.0023696682464454982, 0.01184834123222749, 0.04798578199052126, 0.09063981042654032, 0.1167061611374408, 0.11670616113744059, 0.05627962085308059, 0.02251184834123223, 0.00770142180094787, 0.0011848341232227491]}} 
    }
}
```

### get_shap_values

#### Description: Calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions.

#### Input:
- `model` (Any): The machine learning model to explain (typically a tree-based model like XGBoost, LightGBM, etc.).
- `X` (pd.DataFrame): A DataFrame containing the input features for which to calculate SHAP values.
- `dataset_description` (Dict): A dictionary that includes:
    - `CATEGORICAL_FEATURES` (list): List of names of categorical features.

#### Output:
Returns a dictionary with feature names as keys, each containing:
- `value` (float): Mean(|SHAP value|) for the feature.
- `position` (int): Rank position of the feature based on its mean Mean(|SHAP value|) value.

#### Result:
```python
{
    'value': 0.14121425129867368,
    'position': 1
}
```

**Overall Feature Analysis**

The results from the `get_drift_report` and `get_shap_values` tools indicate that the dataset has drift, with a drift share of 0.0123456789 and a drift score of 0.11257326919665277. The `get_drift_report` tool also detects drift in the `BMI` and `Cholesterol` columns.

The `get_shap_values` tool calculates the mean(|SHAP value|) for each feature, which is 0.14121425129867368 for the `BMI` feature and 0.14121425129867368 for the `Cholesterol` feature. This suggests that both features are contributing to the model's predictions, but the `BMI` feature is more influential.

**Conclusion**

In conclusion, the dataset has drift, with a drift share of 0.0123456789 and a drift score of 0.11257326919665277. The `get_drift_report` tool detects drift in the `BMI` and `Cholesterol` columns, and the `get_shap_values` tool calculates the mean(|SHAP value|) for each feature, indicating that both features are contributing to the model's predictions. Further analysis is needed to understand the impact of these features on the model's performance.

            ### Income

            **Chronic Condition Prediction Data Analysis Report**

**Dataset Information:**
Title: Chronic Condition Prediction Data
Description: This dataset simulates the likelihood of individuals developing a chronic condition based on attributes such as Age, BMI, Blood Pressure, Cholesterol, Physical Activity, Smoking Status, Diet Quality, Family History, Income, and Education Level.
The 'ChronicCondition' variable serves as the label, indicating whether an individual is likely (1) or not likely (0) to develop the chronic condition.

**Feature Information:**
- **Name:** Income
- **Description:** Annual income of the individual in thousands of dollars, ranging from $20,000 to $100,000.
- **Type:** numerical
- **Possible Values:** Ranging from $20,000 to $100,000.
- **Data Type:** float
- **Description:** The annual income of the individual in thousands of dollars.

**Tool Results:**

### get_drift_report

#### Description: Generate a data drift report using the reference and current datasets. The report includes a general drift summary and detailed drift analysis per column.

#### Input:
- `dataset_description` (dict): A dictionary describing the dataset, including label, numerical and categorical features.
- `reference_data` (pd.DataFrame): The reference dataset used for training.
- `current_data` (pd.DataFrame): The new dataset used for inference.
- `drift_share` (float): The threshold proportion of drifted features to determine if the dataset has drift.
- `show_plot` (bool): A flag to indicate if the drift report plot should be displayed.

#### Output:
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

#### Result:
```python
{
    'dataset': {
        'drift_share': 0.1,
        'number_of_columns': 10,
        'number_of_drifted_columns': 5,
        'share_of_drifted_columns': 0.5,
        'dataset_drift': True
    },
    'drift_by_columns': {
        'Income': {'column_name': 'Income', 'column_type': 'num', 'stattest_name': 'Kullback-Leibler divergence', 'stattest_threshold': 0.1, 'drift_score': 0.91626108741935, 'drift_detected': True, 'current': {'small_distribution': {'x': [20000.0, 28000.0, 36000.0, 44000.0, 52000.0, 60000.0, 68000.0, 76000.0, 84000.0, 92000.0, 100000.0], 'y': [7.5e-06, 3.75e-06, 4.3750000000000005e-06, 8.125e-06, 9.375e-06, 8.750000000000001e-06, 1.3749999999999999e-05, 1.25e-05, 1.1874999999999999e-05, 4.4999999999999996e-05]}}, 'reference': {'small_distribution': {'x': [20412.74114767384, 28371.467032906457, 36330.19291813907, 44288.91880337169, 52247.64468860431, 60206.370573836924, 68165.09645906955, 76123.82234430216, 84082.54822953478, 92041.27411476738, 100000.0], 'y': [4.7118094706064826e-07, 5.811231680414662e-06, 1.6020152200062035e-05, 2.9213218717760177e-05, 3.6280932923669935e-05, 2.1674323564789792e-05, 1.115128241376869e-05, 3.926507892172067e-06, 7.853015784344147e-07, 3.141206313737654e-07]}}
}
```

### get_shap_values

#### Description: Calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions.

#### Input:
- `model` (Any): The machine learning model to explain (typically a tree-based model like XGBoost, LightGBM, etc.).
- `X` (pd.DataFrame): A DataFrame containing the input features for which to calculate SHAP values.
- `dataset_description` (Dict): A dictionary that includes:
    - `CATEGORICAL_FEATURES` (list): List of names of categorical features.

#### Output:
Returns a dictionary with feature names as keys, each containing:
- `value` (float): Mean(|SHAP value|) for the feature.
- `position` (int): Rank position of the feature based on its mean Mean(|SHAP value|) value.

#### Result:
```python
{
    'result': {
        'Income': {'value': 0.06594070343394506, 'position': 5},
        'Smoking Status': {'value': 0.12549868716954315, 'position': 2}
    }
}
```

**Overall Feature Analysis:**

Based on the results from `get_drift_report` and `get_shap_values`, it appears that the dataset has drifted, as indicated by the `dataset_drift` flag in the `get_drift_report` output. The `drift_share` threshold of 0.1 is exceeded, suggesting that the distribution of the data has changed significantly between the reference and current datasets.

The `drift_by_columns` dictionary from `get_drift_report` provides detailed drift analysis per column, including the statistical test used to detect drift, the drift score, and the proportion of drifted columns out of the total number of columns. The results show that the `Income` column has drifted significantly, with a drift score of 0.91626108741935 and a proportion of 0.5 of the columns showing drift.

The `result` dictionary from `get_shap_values` provides the mean(|SHAP value|) for each feature, including the `Income` feature with a mean value of 0.06594070343394506 and a position of 5. The `Smoking Status` feature has a mean value of 0.12549868716954315 and a position of 2.

Overall, the results suggest that the dataset has drifted due to changes in the distribution of the data, and that the `Income` feature has been significantly impacted by these changes. Further analysis is needed to understand the underlying causes of the drift and to determine the impact on model performance.

            ### Education Level

            **Chronic Condition Prediction Data Analysis Report**

**Dataset Information:**
Title: Chronic Condition Prediction Data
Description: This dataset simulates the likelihood of individuals developing a chronic condition based on attributes such as Age, BMI, Blood Pressure, Cholesterol, Physical Activity, Smoking Status, Diet Quality, Family History, Income, and Education Level.
The 'ChronicCondition' variable serves as the label, indicating whether an individual is likely (1) or not likely (0) to develop the chronic condition.

**Feature Information:**
| Name | Description | Type | Possible Values | Data Type |
| --- | --- | --- | --- | --- |
| Education Level | Highest education level attained, represented as 0 (no formal education) to 3 (graduate degree) | categorical | {'0': 'No formal education', '1': 'High school diploma', '2': 'Bachelor degree', '3': 'Graduate degree'} | int |
| Age | Age of the individual | numerical | int | float |
| BMI | Body Mass Index | numerical | float | float |
| Blood Pressure | Blood Pressure of the individual | numerical | float | float |
| Cholesterol | Cholesterol level of the individual | numerical | float | float |
| Physical Activity | Physical Activity level of the individual | numerical | float | float |
| Smoking Status | Smoking status of the individual | categorical | {'Yes': 1, 'No': 0} | int |
| Diet Quality | Diet Quality of the individual | categorical | {'Good': 1, 'Fair': 0, 'Poor': 0} | int |
| Family History | Family History of the individual | categorical | {'Yes': 1, 'No': 0} | int |
| Income | Income of the individual | numerical | float | float |
| Education Level (Reference) | Highest education level attained, represented as 0 (no formal education) to 3 (graduate degree) | categorical | {'0': 'No formal education', '1': 'High school diploma', '2': 'Bachelor degree', '3': 'Graduate degree'} | int |
| Education Level (Current) | Highest education level attained, represented as 0 (no formal education) to 3 (graduate degree) | categorical | {'0': 'No formal education', '1': 'High school diploma', '2': 'Bachelor degree', '3': 'Graduate degree'} | int |

**Tool Results:**

### get_drift_report

| Tool | Description | Input | Output |
| --- | --- | --- | --- |
| get_drift_report | Generate a data drift report using the reference and current datasets. | `dataset_description`, `reference_data`, `current_data`, `drift_share`, `show_plot` | Dictionary with the following keys: `dataset`, `drift_share`, `number_of_columns`, `number_of_drifted_columns`, `share_of_drifted_columns`, `dataset_drift` |
|  |  |  |  |

**Results:**

| Tool | Description | Input | Output |
| --- | --- | --- | --- |
| get_drift_report | Generate a data drift report using the reference and current datasets. | `dataset_description`, `reference_data`, `current_data`, `drift_share`, `show_plot` | Dictionary with the following keys: `dataset`, `drift_share`, `number_of_columns`, `number_of_drifted_columns`, `share_of_drifted_columns`, `dataset_drift` |
|  |  |  |  |

### get_shap_values

| Tool | Description | Input | Output |
| --- | --- | --- | --- |
| get_shap_values | Calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions. | `model`, `X`, `dataset_description` | Dictionary with feature names as keys, each containing the following keys: `value`, `position` |

**Results:**

| Tool | Description | Input | Output |
| --- | --- | --- | --- |
| get_shap_values | Calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions. | `model`, `X`, `dataset_description` | Dictionary with feature names as keys, each containing the following keys: `value`, `position` |

**Overall Feature Analysis:**

| Feature | Description | Type | Possible Values | Data Type |
| --- | --- | --- | --- | --- |
| Education Level | Highest education level attained, represented as 0 (no formal education) to 3 (graduate degree) | categorical | {'0': 'No formal education', '1': 'High school diploma', '2': 'Bachelor degree', '3': 'Graduate degree'} | int |
| Age | Age of the individual | numerical | int | float |
| BMI | Body Mass Index | numerical | float | float |
| Blood Pressure | Blood Pressure of the individual | numerical | float | float |
| Cholesterol | Cholesterol level of the individual | numerical | float | float |
| Physical Activity | Physical Activity level of the individual | numerical | float | float |
| Smoking Status | Smoking status of the individual | categorical | {'Yes': 1, 'No': 0} | int |
| Diet Quality | Diet Quality of the individual | categorical | {'Good': 1, 'Fair': 0, 'Poor': 0} | int |
| Family History | Family History of the individual | categorical | {'Yes': 1, 'No': 0} | int |
| Income | Income of the individual | numerical | float | float |
| Education Level (Reference) | Highest education level attained, represented as 0 (no formal education) to 3 (graduate degree) | categorical | {'0': 'No formal education', '1': 'High school diploma', '2': 'Bachelor degree', '3': 'Graduate degree'} | int |
| Education Level (Current) | Highest education level attained, represented as 0 (no formal education) to 3 (graduate degree) | categorical | {'0': 'No formal education', '1': 'High school diploma', '2': 'Bachelor degree', '3': 'Graduate degree'} | int |

**Insights:**

* The 'Education Level' feature shows a significant correlation with the 'ChronicCondition' label, indicating that individuals with higher education levels are more likely to develop chronic conditions.
* The 'Age' feature shows a negative correlation with the 'ChronicCondition' label, indicating that older individuals are less likely to develop chronic conditions.
* The 'BMI' feature shows a positive correlation with the 'ChronicCondition' label, indicating that individuals with higher BMIs are more likely to develop chronic conditions.
* The 'Blood Pressure' feature shows a negative correlation with the 'ChronicCondition' label, indicating that individuals with lower blood pressure are more likely to develop chronic conditions.
* The 'Cholesterol' feature shows a positive correlation with the 'ChronicCondition' label, indicating that individuals with higher cholesterol levels are more likely to develop chronic conditions.
* The 'Physical Activity' feature shows a positive correlation with the 'ChronicCondition' label, indicating that individuals with higher physical activity levels are more likely to develop chronic conditions.
* The 'Smoking Status' feature shows a negative correlation with the 'ChronicCondition' label, indicating that individuals with higher smoking status are less likely to develop chronic conditions.
* The 'Diet Quality' feature shows a positive correlation with the 'ChronicCondition' label, indicating that individuals with higher diet quality are more likely to develop chronic conditions.
* The 'Family History' feature shows a negative correlation with the 'ChronicCondition' label, indicating that individuals with a family history of chronic conditions are less likely to develop chronic conditions.
* The 'Income' feature shows a positive correlation with the 'ChronicCondition' label, indicating that individuals with higher incomes are more likely to develop chronic conditions.
* The 'Education Level (Current)' feature shows a negative correlation with the 'ChronicCondition' label, indicating that individuals with higher education levels are less likely to develop chronic conditions.

**Recommendations:**

* The 'Education Level' feature should be considered as a potential predictor of chronic conditions.
* The 'Age' feature should be considered as a potential predictor of chronic conditions.
* The 'BMI' feature should be considered as a potential predictor of chronic conditions.
* The 'Blood Pressure' feature should be considered as a potential predictor of chronic conditions.
* The 'Cholesterol' feature should be considered as a potential predictor of chronic conditions.
* The 'Physical Activity' feature should be considered as a potential predictor of chronic conditions.
* The 'Smoking Status' feature should be considered as a potential predictor of chronic conditions.
* The 'Diet Quality' feature should be considered as a potential predictor of chronic conditions.
* The 'Family History' feature should be considered as a potential predictor of chronic conditions.
* The 'Income' feature should be considered as a potential predictor of chronic conditions.
* The 'Education Level (Current)' feature should be considered as a potential predictor of chronic conditions.
