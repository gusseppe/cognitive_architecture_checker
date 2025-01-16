
        # Chronic Condition Prediction Data - Deep Insight Report

        ## Overview
        **Key Findings:**

* **Age:** No significant drift detected, but mean(|SHAP value|) values decreased in the current dataset.
* **BMI:** Significant drift detected, with a drift score of 0.11257326919665277.
* **Blood Pressure:** Significant drift detected, with a drift score of 0.3295963763250584.
* **Cholesterol:** Significant drift detected, with a drift score of 0.23450676168929094.
* **Physical Activity:** Significant drift detected, with a drift score of 7.48442577690803.
* **Smoking Status:** Significant drift detected, with a drift score of 0.20183373734484897.
* **Diet Quality:** No significant drift detected.
* **Family History:** No significant drift detected.
* **Income:** Significant drift detected, with a drift score of 0.91626108741935.
* **Education Level:** Significant drift detected, with a drift score of 1.6716891527291513.

**Main Points:**

* **Drift Detection:** 7 out of 10 features showed significant drift.
* **Feature Impact:** Mean(|SHAP value|) values decreased for Age and increased for Income.
* **Label:** Binary label indicating likelihood of developing a chronic condition.
* **Recommendations:** Retrain or update models to adapt to new data distribution, investigate causes of drift, and monitor feature attribution drift.

        ## Details

        ### Label Insight
        **Label Explanation: Chronic Condition Prediction Data**

The label in the dataset, "ChronicCondition", is a categorical variable that indicates the likelihood of an individual developing a chronic condition. The label has two possible values: '0' and '1', corresponding to the presence or absence of a chronic condition.

**Label Description:**

- **Value 0**: Represents an individual who is not likely to develop a chronic condition.
- **Value 1**: Represents an individual who is likely to develop a chronic condition.

**Label Type and Data Type:**

- **Type**: Categorical
- **Data Type**: Integer (int)

**Label Values:**

- **'0'**: No chronic condition
- **'1'**: Chronic condition

**Label Interpretation:**

The label is binary, indicating a binary classification problem. The goal of the model is to predict whether an individual is likely to develop a chronic condition (label value: 1) or not (label value: 0) based on the provided attributes.

**Potential Issues with the Label:**

Based on the available information, there are no apparent issues with the label. However, it is essential to note that the label is based on a simulated dataset, and the accuracy of the label values may depend on the simulation methodology used. Additionally, the label values may not accurately reflect real-world data, which could lead to biased model performance.

**Recommendations:**

To ensure accurate model performance, it is crucial to:

1. Verify the label values against real-world data or clinical validation.
2. Assess the balance between the label values (e.g., 0 and 1) to ensure that the model is not biased towards one class.
3. Consider using additional features or data sources to improve the model's accuracy and robustness.


            ### Age

            **Comprehensive Data Science Report**

**Feature Description**

**1. Age**

* Name: Age
* Description: Age of the individual in years, ranging from 18 to 90.
* Type: numerical
* Possible Values: Ranging from 18 to 90 years.
* Data Type: int

**Tool Results**

**1. get_drift_report**

**Detailed Analysis of Results**

The get_drift_report tool was used to generate a data drift report using the reference and current datasets. The report includes a general drift summary and detailed drift analysis per column.

**General Drift Report Summary**

| Key | Value |
| --- | --- |
| drift_share | 0.1 |
| number_of_columns | 10 |
| number_of_drifted_columns | 0 |
| share_of_drifted_columns | 0.0 |
| dataset_drift | False |

The general drift report summary indicates that no drift was detected in the dataset based on the drift share threshold of 0.1.

**Detailed Drift Analysis per Column**

| Column Name | Column Type | Stat Test Name | Stat Test Threshold | Drift Score | Drift Detected |
| --- | --- | --- | --- | --- | --- |
| Age | num | Kullback-Leibler divergence | 0.1 | 0.03778629771302727 | False |

The detailed drift analysis per column shows that the Age column did not exhibit any drift between the reference and current datasets.

**Insights and Interpretations**

The results from the get_drift_report tool indicate that there is no significant change in the distribution of the Age column between the reference and current datasets. This suggests that the model's performance is unlikely to be affected by the changes in the input data distribution.

**2. get_shap_values**

**Detailed Analysis of Results**

The get_shap_values tool was used to calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions.

**Feature SHAP Values**

| Feature | Value | Position |
| --- | --- | --- |
| reference | 0.08906002648096621 | 3 |
| current | 0.050937679805919664 | 5 |

The results from the get_shap_values tool show that the mean(|SHAP value|) values for the Age feature are 0.08906002648096621 and 0.050937679805919664 for the reference and current datasets, respectively. The position of the feature based on its mean Mean(|SHAP value|) value is 3 and 5 for the reference and current datasets, respectively.

**Insights and Interpretations**

The results from the get_shap_values tool indicate that the average impact of the Age feature on the model's predictions is lower in the current dataset compared to the reference dataset. This suggests that the input data distribution changes may have affected the feature contributions of the model.

**Overall Feature Analysis**

**Summary of Key Findings**

* The Age column did not exhibit any drift between the reference and current datasets based on the get_drift_report tool.
* The mean(|SHAP value|) values for the Age feature are lower in the current dataset compared to the reference dataset based on the get_shap_values tool.

**Recommendations**

Based on the results from the get_drift_report and get_shap_values tools, it is recommended to:

* Monitor the Age column for any future changes in the input data distribution.
* Investigate the changes in the input data distribution and their impact on the feature contributions of the model.

**Conclusion**

The results from the get_drift_report and get_shap_values tools indicate that the Age column did not exhibit any drift between the reference and current datasets. However, the mean(|SHAP value|) values for the Age feature are lower in the current dataset compared to the reference dataset. These findings suggest that the input data distribution changes may have affected the feature contributions of the model. Further investigation is required to understand the impact of these changes on the model's performance.

            ### BMI

            **Comprehensive Data Science Report**

**Feature Description**

**1. Feature: BMI**

* Name: BMI
* Description: Body Mass Index of the individual, ranging from 18.5 to 40.0.
* Type: numerical
* Possible Values: Ranging from 18.5 to 40.0.
* Data Type: float

**Tool Results**

**1. get_drift_report**

**1.1. General Drift Report Summary**

| Key | Value |
| --- | --- |
| drift_share | 0.2 |
| number_of_columns | 10 |
| number_of_drifted_columns | 2 |
| share_of_drifted_columns | 0.2 |
| dataset_drift | True |

**1.2. Detailed Drift Analysis per Column**

| Column Name | Column Type | Stat Test Name | Stat Test Threshold | Drift Score | Drift Detected |
| --- | --- | --- | --- | --- | --- |
| BMI | num | Kullback-Leibler divergence | 0.1 | 0.11257326919665277 | True |
| ... | ... | ... | ... | ... | ... |

**Insights and Interpretations**

The get_drift_report tool indicates that the dataset has drift, with a drift share of 0.2 and 2 out of 10 columns showing drift. The detailed drift analysis per column reveals that the BMI feature has a drift score of 0.11257326919665277, indicating a significant change in the distribution of the data.

**2. get_shap_values**

**1.1. Feature Attribution Drift Analysis**

| Feature | Value | Position |
| --- | --- | --- |
| reference | 0.14121425129867368 | 1 |
| current | 0.16781096493974235 | 1 |

**Insights and Interpretations**

The get_shap_values tool reveals that the feature attribution drift analysis shows a change in the mean(|SHAP value|) values for the features. The current dataset has a higher mean(|SHAP value|) value for the BMI feature, indicating a change in the feature's contribution to the model's predictions.

**Overall Feature Analysis**

**Summary of Key Findings**

* The BMI feature has a significant change in distribution, as indicated by the get_drift_report tool.
* The get_shap_values tool reveals a change in the feature attribution drift analysis for the BMI feature.
* The dataset has drift, with a drift share of 0.2 and 2 out of 10 columns showing drift.

**Recommendations**

* Further analysis is required to understand the impact of the drift on the model's performance.
* Data preprocessing and feature engineering techniques may be necessary to address the drift.
* Model retraining or updating may be required to adapt to the changes in the data distribution.

**Conclusion**

This comprehensive data science report highlights the changes in the distribution of the data and the feature attribution drift analysis for the BMI feature. The results indicate a significant change in the distribution of the data and a change in the feature's contribution to the model's predictions. Further analysis and recommendations are provided to address the drift and improve the model's performance.

            ### Blood Pressure

            **Comprehensive Data Science Report**

**Feature Description**

**1. Blood Pressure**

* Name: Blood Pressure
* Description: Systolic blood pressure of the individual in mmHg, ranging from 80 to 180.
* Type: numerical
* Possible Values: Ranging from 80 to 180 mmHg.
* Data Type: int

**Tool Results**

**1. get_drift_report**

**Detailed Analysis of Results**

The get_drift_report tool was used to generate a data drift report using the reference and current datasets. The report includes a general drift summary and detailed drift analysis per column.

**Insights and Interpretations**

The drift report summary indicates that the dataset has drift, with a drift share of 0.25 (25% of the columns show drift). The number of drifted columns is 3 out of 12 columns, which is a significant proportion. The drift share threshold is set to 0.2, which means that if more than 20% of the columns show drift, the dataset is considered to have drift.

The detailed drift analysis per column shows that the Blood Pressure column has a drift score of 0.3295963763250584, which is above the threshold of 0.1. This indicates that the distribution of the Blood Pressure values has changed significantly between the reference and current datasets.

**Drift Analysis for Blood Pressure**

| Column Name | Column Type | Stat Test Name | Stat Test Threshold | Drift Score | Drift Detected |
| --- | --- | --- | --- | --- | --- |
| Blood Pressure | num | Kullback-Leibler divergence | 0.1 | 0.3295963763250584 | True |

**Distribution Information for Blood Pressure**

**Current Distribution**

* small_distribution: {'x': [77.42647761458834, 93.60024655055858, 109.77401548652881, 125.94778442249904, 142.12155335846927, 158.29532229443953, 174.46909123040976, 190.64286016638, 206.81662910235025, 222.99039803832045, 239.1641669742907], 'y': [0.0015457126968347085, 0.0021639977755685937, 0.008346848562907433, 0.009892561259742144, 0.014838841889613187, 0.01112913141720991, 0.008965133641641317, 0.003400567933036356, 0.0012365701574677701, 0.0003091425393669414]}

**Reference Distribution**

* small_distribution: {'x': [80.0, 90.0, 100.0, 110.0, 120.0, 130.0, 140.0, 150.0, 160.0, 170.0, 180.0], 'y': [0.000125, 0.001875, 0.003, 0.00875, 0.018500000000000003, 0.025625, 0.020125, 0.014125, 0.006, 0.001875]}

**2. get_shap_values**

**Detailed Analysis of Results**

The get_shap_values tool was used to calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions.

**Insights and Interpretations**

The results show that the mean(|SHAP value|) for the Blood Pressure feature is 0.053554968593565636, which is lower than the mean(|SHAP value|) for the reference dataset (0.07114418923716576). This indicates that the impact of the Blood Pressure feature on the model's predictions has decreased in the current dataset.

**SHAP Values for Blood Pressure**

| Feature Name | Value | Position |
| --- | --- | --- |
| Blood Pressure | 0.053554968593565636 | 4 |

**Overall Feature Analysis**

**Summary of Key Findings**

* The dataset has drift, with a drift share of 0.25 (25% of the columns show drift).
* The Blood Pressure column has a drift score of 0.3295963763250584, which is above the threshold of 0.1.
* The impact of the Blood Pressure feature on the model's predictions has decreased in the current dataset.

**Recommendations**

* Further analysis is needed to understand the causes of the drift in the dataset.
* The model should be re-trained on the current dataset to ensure that it is accurate and reliable.
* The Blood Pressure feature should be monitored closely to ensure that its impact on the model's predictions does not continue to decrease.

            ### Cholesterol

            **Comprehensive Data Science Report**

**Feature Description**

**Name:** Cholesterol
**Description:** Total cholesterol level of the individual in mg/dL, ranging from 150 to 300.
**Type:** numerical
**Possible Values:** Ranging from 150 to 300 mg/dL.
**Data Type:** int

**Tool Results**

**1. get_drift_report**

**Detailed Analysis of Results:**

The get_drift_report tool was used to analyze the drift in the Cholesterol feature between the reference and current datasets. The results are as follows:

* **Drift Share:** 0.23450676168929094
* **Number of Columns:** 1
* **Number of Drifted Columns:** 1
* **Share of Drifted Columns:** 100.0%
* **Dataset Drift:** True

The drift score for the Cholesterol feature is 0.23450676168929094, indicating a significant change in the distribution of the data. The drift is detected based on the Kullback-Leibler divergence statistical test with a threshold of 0.1.

**Insights and Interpretations:**

The results indicate that there is a significant drift in the Cholesterol feature between the reference and current datasets. This could be due to changes in the population demographics, lifestyle, or environmental factors. The drift in the Cholesterol feature could impact the performance of the model, as it may not be able to accurately predict the likelihood of developing a chronic condition based on the updated data.

**2. get_shap_values**

**Detailed Analysis of Results:**

The get_shap_values tool was used to calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions. The results are as follows:

* **Reference:** {'value': 0.03926329553692529, 'position': 6}
* **Current:** {'value': 0.04945714499086426, 'position': 6}

The mean(|SHAP value|) for the Cholesterol feature is 0.03926329553692529 in the reference dataset and 0.04945714499086426 in the current dataset. The feature position is 6 in both datasets.

**Insights and Interpretations:**

The results indicate that the Cholesterol feature has a relatively low impact on the model's predictions in both the reference and current datasets. The mean(|SHAP value|) values are relatively small, indicating that the feature does not have a significant impact on the model's predictions. However, the slight increase in the mean(|SHAP value|) value in the current dataset could indicate a slight change in the feature's impact on the model's predictions.

**Overall Feature Analysis**

**Summary of Key Findings:**

* The Cholesterol feature has a significant drift between the reference and current datasets, indicating a change in the distribution of the data.
* The drift in the Cholesterol feature could impact the performance of the model, as it may not be able to accurately predict the likelihood of developing a chronic condition based on the updated data.
* The Cholesterol feature has a relatively low impact on the model's predictions in both the reference and current datasets.

**Recommendations:**

* Update the model to incorporate the updated data and retrain the model to ensure accurate predictions.
* Monitor the Cholesterol feature for further changes in the distribution of the data to ensure that the model remains accurate.
* Consider incorporating additional features or modifying the existing features to improve the model's performance.

            ### Physical Activity

            **Comprehensive Data Science Report**

**Feature Description: Physical Activity**

* **Name:** Physical Activity
* **Description:** Number of days per week the individual engages in physical activity, ranging from 0 to 7.
* **Type:** Numerical
* **Possible Values:** Ranging from 0 to 7 days per week.
* **Data Type:** int

**Tool Results: get_drift_report**

### Detailed Analysis of Results

The `get_drift_report` tool generates a data drift report using the reference and current datasets. The report includes a general drift summary and detailed drift analysis per column.

#### General Drift Summary

| Key | Value |
| --- | --- |
| `drift_share` | 0.14285714285714285 |
| `number_of_columns` | 10 |
| `number_of_drifted_columns` | 1 |
| `share_of_drifted_columns` | 0.1 |
| `dataset_drift` | True |

The general drift summary indicates that there is a significant drift in the dataset, with 1 out of 10 columns showing drift.

#### Detailed Drift Analysis per Column

| Column Name | Column Type | Stat Test Name | Stat Test Threshold | Drift Score | Drift Detected |
| --- | --- | --- | --- | --- | --- |
| Physical Activity | num | Kullback-Leibler divergence | 0.1 | 7.48442577690803 | True |

The detailed drift analysis per column shows that the Physical Activity feature has a drift score of 7.48442577690803, indicating a significant drift in the distribution of this feature between the reference and current datasets.

### Insights and Interpretations

The results from the `get_drift_report` tool indicate that there is a significant drift in the dataset, with the Physical Activity feature showing the most significant drift. This suggests that the input data distribution has changed, leading to changes in the model's predictions. The drift in the Physical Activity feature may be due to changes in the population's physical activity levels or changes in the way physical activity is measured.

**Tool Results: get_shap_values**

### Detailed Analysis of Results

The `get_shap_values` tool calculates the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions.

#### Feature Attribution Drift

| Feature | Value | Position |
| --- | --- | --- |
| reference | 0.09817662833236682 | 2 |
| current | 0.07730394004727022 | 3 |

The results from the `get_shap_values` tool show that the Physical Activity feature has a lower mean(|SHAP value|) in the current dataset compared to the reference dataset, indicating a decrease in its contribution to the model's predictions.

### Insights and Interpretations

The results from the `get_shap_values` tool indicate that the Physical Activity feature has a lower impact on the model's predictions in the current dataset compared to the reference dataset. This suggests that the input data distribution has changed, leading to changes in the feature attribution. The decrease in the Physical Activity feature's contribution to the model's predictions may be due to changes in the population's physical activity levels or changes in the way physical activity is measured.

**Overall Feature Analysis: Physical Activity**

### Summary of Key Findings

The analysis of the Physical Activity feature using the `get_drift_report` and `get_shap_values` tools indicates that there is a significant drift in the dataset, with the Physical Activity feature showing the most significant drift. The results also show that the Physical Activity feature has a lower impact on the model's predictions in the current dataset compared to the reference dataset. These findings suggest that the input data distribution has changed, leading to changes in the model's predictions and feature attribution.

            ### Smoking Status

            **Comprehensive Data Science Report**

**Feature Description: Smoking Status**

* **Name:** Smoking Status
* **Description:** Current smoking status, represented as 0 (non-smoker), 1 (former smoker), or 2 (current smoker).
* **Type:** categorical
* **Possible Values:** {'0': 'Non-smoker', '1': 'Former smoker', '2': 'Current smoker'}
* **Data Type:** int

**Tool Results: get_drift_report**

### Detailed Analysis of Results

The `get_drift_report` tool generates a data drift report using the reference and current datasets. The report includes a general drift summary and detailed drift analysis per column.

#### General Drift Summary

| Metric | Value |
| --- | --- |
| Drift Share | 0.25 |
| Number of Columns | 10 |
| Number of Drifted Columns | 2 |
| Share of Drifted Columns | 0.2 |
| Dataset Drift | True |

The general drift summary indicates that 20% of the columns show drift, and the dataset drift is detected based on the `drift_share` threshold.

#### Detailed Drift Analysis per Column

| Column Name | Column Type | Stat Test Name | Stat Test Threshold | Drift Score | Drift Detected |
| --- | --- | --- | --- | --- | --- |
| Smoking Status | cat | Kullback-Leibler divergence | 0.1 | 0.20183373734484897 | True |

The detailed drift analysis per column shows that the `Smoking Status` column has a drift score of 0.20183373734484897, indicating that the distribution of this column has changed significantly between the reference and current datasets.

### Insights and Interpretations

The `get_drift_report` tool indicates that the `Smoking Status` column has drifted, which may lead to a decrease in model performance. This suggests that the input data distribution has changed, and the model may need to be retrained or updated to adapt to the new data.

**Tool Results: get_shap_values**

### Detailed Analysis of Results

The `get_shap_values` tool calculates the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions.

#### Feature Attribution Drift

| Feature | Value | Position |
| --- | --- | --- |
| reference | 0.006457749486556214 | 10 |
| current | 0.004061665409373835 | 10 |

The feature attribution drift analysis shows that the `Smoking Status` feature has a mean(|SHAP value|) value of 0.004061665409373835 in the current dataset, which is lower than the value of 0.006457749486556214 in the reference dataset. This suggests that the `Smoking Status` feature has a lower impact on the model's predictions in the current dataset.

### Insights and Interpretations

The `get_shap_values` tool indicates that the `Smoking Status` feature has a lower impact on the model's predictions in the current dataset, which may be due to the drift in the `Smoking Status` column. This suggests that the model may need to be retrained or updated to adapt to the new data and to ensure that the feature attribution is accurate.

**Overall Feature Analysis**

### Summary of Key Findings

* The `Smoking Status` column has drifted, indicating that the distribution of this column has changed significantly between the reference and current datasets.
* The `Smoking Status` feature has a lower impact on the model's predictions in the current dataset, which may be due to the drift in the `Smoking Status` column.
* The model may need to be retrained or updated to adapt to the new data and to ensure that the feature attribution is accurate.

Recommendations:

* Retrain the model using the current dataset to ensure that the model is accurate and reliable.
* Update the model to adapt to the new data and to ensure that the feature attribution is accurate.
* Monitor the `Smoking Status` column and the `Smoking Status` feature to ensure that they do not drift again in the future.

            ### Diet Quality

            **Comprehensive Data Science Report**

**Feature Description**

### Diet Quality

* **Name:** Diet Quality
* **Description:** Quality of diet, represented as 0 (poor), 1 (average), or 2 (good).
* **Type:** categorical
* **Possible Values:** {'0': 'Poor', '1': 'Average', '2': 'Good'}
* **Data Type:** int

**Tool Results**

### get_drift_report

#### Detailed Analysis of Results

The `get_drift_report` tool was used to generate a data drift report using the reference and current datasets. The report includes a general drift summary and detailed drift analysis per column.

| Column Name | Column Type | Stat Test Name | Stat Test Threshold | Drift Score | Drift Detected |
| --- | --- | --- | --- | --- | --- |
| Diet Quality | cat | Kullback-Leibler divergence | 0.1 | 0.0018915553873695345 | False |

The detailed drift analysis for the 'Diet Quality' column shows that the Kullback-Leibler divergence statistical test was used to detect drift. The drift score is 0.0018915553873695345, which is below the threshold of 0.1. Therefore, no drift was detected for this column.

#### Insights and Interpretations

The results indicate that the distribution of the 'Diet Quality' column has not changed significantly between the reference and current datasets. This suggests that the model's performance is unlikely to be affected by changes in the input data distribution for this feature.

### get_shap_values

#### Detailed Analysis of Results

The `get_shap_values` tool was used to calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions.

| Feature Name | Value | Position |
| --- | --- | --- |
| reference | 0.013835053054035294 | 9 |
| current | 0.011401517327642103 | 9 |

The results show that the mean(|SHAP value|) for the 'Diet Quality' feature is 0.013835053054035294 in the reference dataset and 0.011401517327642103 in the current dataset. The feature position remains the same at 9 in both datasets.

#### Insights and Interpretations

The results indicate that the average impact of the 'Diet Quality' feature on the model's predictions has decreased slightly from the reference to the current dataset. However, the feature position remains the same, suggesting that the feature's contribution to the model's predictions has not changed significantly.

**Overall Feature Analysis**

### Summary of Key Findings

* The distribution of the 'Diet Quality' column has not changed significantly between the reference and current datasets.
* The average impact of the 'Diet Quality' feature on the model's predictions has decreased slightly from the reference to the current dataset.
* The feature position remains the same at 9 in both datasets.

These findings suggest that the 'Diet Quality' feature is stable and its contribution to the model's predictions has not changed significantly between the reference and current datasets.

            ### Family History

            **Comprehensive Data Science Report**

**Feature Description**

**Name:** Family History
**Description:** Family history of chronic condition, represented as 0 (no family history) or 1 (family history).
**Type:** categorical
**Possible Values:** {'0': 'No family history', '1': 'Family history'}
**Data Type:** int

**Tool Results**

**1. get_drift_report**

**Detailed Analysis of Results:**

The get_drift_report tool was used to generate a data drift report for the Family History feature. The report includes a general drift summary and detailed drift analysis per column.

**Insights and Interpretations:**

The drift report summary indicates that the dataset has a drift share of 0.0, which means that no columns show a significant drift. However, the detailed drift analysis for the Family History feature shows a drift score of 0.005370730255683034, which is below the threshold of 0.1. This suggests that the distribution of the Family History feature has not changed significantly between the reference and current datasets.

**Drift Report Summary:**

| Key | Value |
| --- | --- |
| drift_share | 0.0 |
| number_of_columns | 10 |
| number_of_drifted_columns | 0 |
| share_of_drifted_columns | 0.0 |
| dataset_drift | False |

**Detailed Drift Analysis for Family History Feature:**

| Key | Value |
| --- | --- |
| column_name | Family History |
| column_type | cat |
| stattest_name | Kullback-Leibler divergence |
| stattest_threshold | 0.1 |
| drift_score | 0.005370730255683034 |
| drift_detected | False |
| current | {'small_distribution': {'x': [0, 1], 'y': [118, 82]}} |
| reference | {'small_distribution': {'x': [0, 1], 'y': [431, 369]}} |

**2. get_shap_values**

**Detailed Analysis of Results:**

The get_shap_values tool was used to calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions.

**Insights and Interpretations:**

The results of the get_shap_values tool show that the mean(|SHAP value|) for the Family History feature is 0.01724435122228072 in the reference dataset and 0.018126868998631664 in the current dataset. The rank position of the feature based on its mean Mean(|SHAP value|) value is 7 in both datasets.

**SHAP Values Results:**

| Key | Value |
| --- | --- |
| reference | {'value': 0.01724435122228072, 'position': 7} |
| current | {'value': 0.018126868998631664, 'position': 7} |

**Overall Feature Analysis**

**Summary of Key Findings:**

Based on the results of the get_drift_report and get_shap_values tools, the following key findings can be summarized:

* The distribution of the Family History feature has not changed significantly between the reference and current datasets, as indicated by the drift score of 0.005370730255683034.
* The mean(|SHAP value|) for the Family History feature is slightly higher in the current dataset compared to the reference dataset, indicating a slight increase in the average impact of the feature on the model's predictions.

**Recommendations:**

Based on the results of the analysis, it is recommended to:

* Continue monitoring the distribution of the Family History feature to ensure that it remains stable over time.
* Investigate the reasons behind the slight increase in the mean(|SHAP value|) for the Family History feature in the current dataset.

**Conclusion:**

The analysis of the Family History feature using the get_drift_report and get_shap_values tools has provided valuable insights into the stability of the feature over time. The results indicate that the distribution of the feature has not changed significantly, but there is a slight increase in the average impact of the feature on the model's predictions. Further investigation is recommended to understand the reasons behind this increase.

            ### Income

            **Comprehensive Data Science Report**

**Feature Description**

### Income

* **Name:** Income
* **Description:** Annual income of the individual in thousands of dollars, ranging from 20k to 100k.
* **Type:** Numerical
* **Possible Values:** Ranging from $20,000 to $100,000.
* **Data Type:** Float

**Tool Results**

### get_drift_report

#### Detailed Analysis of Results

The `get_drift_report` tool generates a data drift report using the reference and current datasets. The report includes a general drift summary and detailed drift analysis per column.

| Column Name | Column Type | Stat Test Name | Stat Test Threshold | Drift Score | Drift Detected |
| --- | --- | --- | --- | --- | --- |
| Income | num | Kullback-Leibler divergence | 0.1 | 0.91626108741935 | True |

The detailed drift analysis for the Income column shows that the Kullback-Leibler divergence statistical test detected a drift score of 0.91626108741935, indicating that the distribution of the Income column has changed significantly between the reference and current datasets.

#### Insights and Interpretations

The detection of drift in the Income column suggests that the input data distribution has changed, leading to a decrease in model performance. This may be due to changes in the population demographics, economic conditions, or other factors that affect income levels.

### get_shap_values

#### Detailed Analysis of Results

The `get_shap_values` tool calculates the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions.

| Feature Name | Value | Position |
| --- | --- | --- |
| reference | 0.06594070343394506 | 5 |
| current | 0.12549868716954315 | 2 |

The results show that the mean(|SHAP value|) for the Income feature is higher in the current dataset (0.12549868716954315) compared to the reference dataset (0.06594070343394506). This indicates that the Income feature has a greater impact on the model's predictions in the current dataset.

#### Insights and Interpretations

The increase in the mean(|SHAP value|) for the Income feature in the current dataset suggests that the model is placing more emphasis on income levels when making predictions. This may be due to changes in the population demographics, economic conditions, or other factors that affect income levels.

**Overall Feature Analysis**

### Summary of Key Findings

* The Income feature has been detected as drifted using the `get_drift_report` tool, indicating that the distribution of income levels has changed significantly between the reference and current datasets.
* The `get_shap_values` tool shows that the mean(|SHAP value|) for the Income feature is higher in the current dataset, indicating that the model is placing more emphasis on income levels when making predictions.

**Recommendations**

* Investigate the causes of the drift in the Income feature, such as changes in population demographics, economic conditions, or other factors that affect income levels.
* Update the model to account for the changes in the input data distribution, such as by retraining the model with the current dataset or by incorporating additional features that capture the changes in income levels.

**Conclusion**

The analysis of the Income feature using the `get_drift_report` and `get_shap_values` tools has revealed significant changes in the distribution of income levels between the reference and current datasets. These changes have resulted in a greater emphasis on income levels when making predictions, as indicated by the increase in the mean(|SHAP value|) for the Income feature. Further investigation is required to understand the causes of these changes and to update the model to account for the changes in the input data distribution.

            ### Education Level

            **Comprehensive Data Science Report**

**Feature Description: Education Level**

* **Name:** Education Level
* **Description:** Highest education level attained, represented as 0 (no formal education) to 3 (graduate degree).
* **Type:** categorical
* **Possible Values:** {'0': 'No formal education', '1': 'High school diploma', '2': 'Bachelor degree', '3': 'Graduate degree'}
* **Data Type:** int

**Tool Results: get_drift_report**

### Detailed Analysis of Results

The `get_drift_report` tool was used to generate a data drift report using the reference and current datasets. The report includes a general drift summary and detailed drift analysis per column.

#### General Drift Summary

| Metric | Value |
| --- | --- |
| Drift Share | 0.25 |
| Number of Columns | 10 |
| Number of Drifted Columns | 2 |
| Share of Drifted Columns | 0.2 |
| Dataset Drift | True |

The general drift summary indicates that 20% of the columns show drift, and the dataset drift is detected based on the `drift_share` threshold of 0.25.

#### Detailed Drift Analysis per Column

| Column Name | Column Type | Stat Test Name | Stat Test Threshold | Drift Score | Drift Detected |
| --- | --- | --- | --- | --- | --- |
| Education Level | cat | Kullback-Leibler divergence | 0.1 | 1.6716891527291513 | True |

The detailed drift analysis per column shows that the `Education Level` column has a drift score of 1.6716891527291513, indicating that the distribution of this column has changed significantly between the reference and current datasets.

### Insights and Interpretations

The `get_drift_report` tool indicates that the `Education Level` column has drifted, which may lead to a decrease in model performance. This suggests that the input data distribution has changed, and the model may need to be retrained or updated to adapt to the new data.

**Tool Results: get_shap_values**

### Detailed Analysis of Results

The `get_shap_values` tool was used to calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions.

#### Feature Attribution Drift

| Feature | Value | Position |
| --- | --- | --- |
| reference | 0.016434074575538762 | 8 |
| current | 0.01641983309158441 | 8 |

The `get_shap_values` tool indicates that the feature attribution drift is minimal, with a difference of 0.000014243 in the mean(|SHAP value|) value between the reference and current datasets. This suggests that the input data distribution has not changed significantly, and the model's feature contributions remain relatively stable.

### Insights and Interpretations

The `get_shap_values` tool indicates that the feature attribution drift is minimal, suggesting that the input data distribution has not changed significantly. This is consistent with the `get_drift_report` tool's indication of minimal drift in the `Education Level` column.

**Overall Feature Analysis**

### Summary of Key Findings

* The `Education Level` column has drifted, indicating that the distribution of this column has changed significantly between the reference and current datasets.
* The feature attribution drift is minimal, suggesting that the input data distribution has not changed significantly.
* The dataset drift is detected based on the `drift_share` threshold of 0.25.

### Recommendations

* Retrain or update the model to adapt to the new data distribution.
* Investigate the cause of the drift in the `Education Level` column and take corrective action to prevent future drift.
* Monitor the feature attribution drift to ensure that the model's feature contributions remain stable.
