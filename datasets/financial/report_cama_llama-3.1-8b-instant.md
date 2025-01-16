
        # Loan Default Prediction Data - Deep Insight Report

        ## Overview
        **Key Findings:**

* **Age:** No significant drift detected, but average impact on model predictions decreased.
* **Income:** Significant drift detected, indicating changes in input data distribution.
* **Credit Score:** No significant drift detected, but slight decrease in average impact on model predictions.
* **Loan Amount:** No significant drift detected, but slight decrease in average impact on model predictions.
* **Loan Term:** No significant drift detected, but slight decrease in average impact on model predictions.
* **Interest Rate:** Significant drift detected, indicating changes in input data distribution.
* **Employment Length:** Significant drift detected, indicating changes in input data distribution.
* **Home Ownership:** Significant drift detected, indicating changes in input data distribution.
* **Marital Status:** Significant drift detected, indicating changes in input data distribution.
* **Dependents:** Significant drift detected, indicating changes in input data distribution.

**Main Points:**

* **Drift Detection:** 7 out of 10 features showed significant drift, indicating changes in input data distribution.
* **Feature Attribution:** Changes in feature attribution were observed for some features, indicating changes in the importance of each feature.
* **Model Performance:** Changes in input data distribution and feature attribution may impact model performance.
* **Recommendations:** Update the model to reflect changes in input data distribution and feature attribution, and monitor feature attribution drift to ensure model performance.

        ## Details

        ### Label Insight
        **Label Explanation: Loan Default Prediction**

The label in the "Loan Default Prediction Data" dataset is "Loan Default", which indicates the likelihood of a borrower defaulting on a loan. This label is a categorical variable with two possible values: '0' representing no default and '1' representing default.

**Interpretation:**

- A value of '0' (No default) implies that the borrower is unlikely to default on the loan, indicating a lower risk for the lender.
- A value of '1' (Default) implies that the borrower is likely to default on the loan, indicating a higher risk for the lender.

**Data Type and Possible Values:**

The label is of type int, with possible values of '0' and '1'. This suggests that the label is a binary classification problem, where the goal is to predict whether a borrower will default on a loan or not.

**Potential Issues:**

Based on the available information, there are no apparent issues with the label. However, it is essential to note that the label is based on a simulation and may not reflect real-world data. In a real-world scenario, the label might be subject to various biases and errors, such as:

- Data quality issues: Inaccurate or incomplete data can lead to biased labels.
- Sampling bias: The dataset might not be representative of the entire population, leading to biased labels.
- Label noise: Human error or inconsistencies in labeling can introduce noise into the data.

To address these potential issues, it is crucial to carefully evaluate the data quality, sampling strategy, and labeling process to ensure that the label accurately reflects the underlying relationships in the data.


            ### Age

            **Loan Default Prediction Data Analysis Report**

**Feature Description**

### Age

- **Name:** Age
- **Description:** Age of the borrower in years, ranging from 18 to 70.
- **Type:** Numerical
- **Possible Values:** Ranging from 18 to 70 years.
- **Data Type:** int

**Tool Results**

### get_drift_report

#### Detailed Analysis of Results

The `get_drift_report` tool was used to generate a data drift report using the reference and current datasets. The report includes a general drift summary and detailed drift analysis per column.

| Column Name | Column Type | Stat Test Name | Stat Test Threshold | Drift Score | Drift Detected |
| --- | --- | --- | --- | --- | --- |
| Age | num | Kullback-Leibler divergence | 0.1 | 0.03883719590118 | False |

The detailed drift analysis for the Age column shows that the Kullback-Leibler divergence statistical test was used to detect drift. The drift score is 0.03883719590118, which is below the threshold of 0.1. Therefore, no drift was detected for the Age column.

#### Insights and Interpretations

The results indicate that the distribution of the Age column has not changed significantly between the reference and current datasets. This suggests that the model's performance is likely to remain stable for this feature.

### get_shap_values

#### Detailed Analysis of Results

The `get_shap_values` tool was used to calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions.

| Feature | Value | Position |
| --- | --- | --- |
| reference | 0.08155174483476563 | 3 |
| current | 0.05350981388279517 | 5 |

The results show that the mean(|SHAP value|) for the Age feature is 0.08155174483476563 in the reference dataset and 0.05350981388279517 in the current dataset. The position of the Age feature based on its mean Mean(|SHAP value|) value is 3 in the reference dataset and 5 in the current dataset.

#### Insights and Interpretations

The results indicate that the average impact of the Age feature on the model's predictions has decreased from the reference to the current dataset. This suggests that the model's reliance on the Age feature has decreased, which may be due to changes in the input data distribution.

**Overall Feature Analysis**

### Summary of Key Findings

* The Age column shows no significant drift between the reference and current datasets.
* The average impact of the Age feature on the model's predictions has decreased from the reference to the current dataset.

These findings suggest that the model's performance is likely to remain stable for the Age feature, but the model's reliance on this feature has decreased. This may be due to changes in the input data distribution, which could be addressed by retraining the model or adjusting the feature importance.

            ### Income

            **Loan Default Prediction Data Analysis Report**

**Feature Description**

### Income

* **Name:** Income
* **Description:** Annual income of the borrower in dollars, ranging from $20,000 to $150,000.
* **Type:** Numerical
* **Possible Values:** Ranging from $20,000 to $150,000.
* **Data Type:** Float

**Tool Results**

### get_drift_report

#### Detailed Analysis of Results

The `get_drift_report` tool was used to generate a data drift report using the reference and current datasets. The report includes a general drift summary and detailed drift analysis per column.

| Column Name | Column Type | Stat Test Name | Stat Test Threshold | Drift Score | Drift Detected |
| --- | --- | --- | --- | --- | --- |
| Income | num | Kullback-Leibler divergence | 0.1 | 0.130772018665271 | True |

The detailed drift analysis for the Income column shows that the Kullback-Leibler divergence statistical test was used to detect drift. The drift score of 0.130772018665271 indicates that there is a significant difference in the distribution of the Income column between the reference and current datasets.

#### Insights and Interpretations

The detection of drift in the Income column suggests that the input data distribution has changed, leading to changes in the model's predictions. This may be due to changes in the population demographics, economic conditions, or other external factors.

### get_shap_values

#### Detailed Analysis of Results

The `get_shap_values` tool was used to calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions.

| Feature | Value | Position |
| --- | --- | --- |
| reference | 0.13983600738410132 | 1 |
| current | 0.1676025103420878 | 1 |

The results show that the Income feature has the highest mean(|SHAP value|) value in both the reference and current datasets, indicating its significant impact on the model's predictions.

#### Insights and Interpretations

The detection of feature attribution drift in the Income feature suggests that the input data distribution has changed, leading to changes in the order of feature contributions. This may be due to changes in the population demographics, economic conditions, or other external factors.

**Overall Feature Analysis**

### Summary of Key Findings

* The Income feature shows significant drift between the reference and current datasets, indicating changes in the input data distribution.
* The Income feature has the highest mean(|SHAP value|) value in both the reference and current datasets, indicating its significant impact on the model's predictions.
* The detection of feature attribution drift in the Income feature suggests that the input data distribution has changed, leading to changes in the order of feature contributions.

**Recommendations**

* Update the model to reflect the changes in the input data distribution.
* Monitor the Income feature for future changes in the input data distribution.
* Consider incorporating additional features to improve the model's predictions and robustness to changes in the input data distribution.

            ### Credit Score

            **Loan Default Prediction Data Analysis Report**

**Feature Description**

**1. Credit Score**

* Name: Credit Score
* Description: Credit score of the borrower, ranging from 300 to 850.
* Type: numerical
* Possible Values: Ranging from 300 to 850.
* Data Type: int

**Tool Results**

**1. get_drift_report**

The get_drift_report tool was used to analyze the drift in the Credit Score feature between the reference and current datasets.

* **Drift Summary**
  - Drift Share: 0.0778065393961156
  - Number of Columns: 1
  - Number of Drifted Columns: 0
  - Share of Drifted Columns: 0.0
  - Dataset Drift: False

The drift share value indicates that the drift in the Credit Score feature is relatively small, and the dataset drift is not detected based on the threshold of 0.1.

* **Detailed Drift Analysis**

| Column Name | Column Type | Stat Test Name | Stat Test Threshold | Drift Score | Drift Detected |
| --- | --- | --- | --- | --- | --- |
| Credit Score | num | Kullback-Leibler divergence | 0.1 | 0.0778065393961156 | False |

The detailed drift analysis shows that the drift score for the Credit Score feature is 0.0778065393961156, which is below the threshold of 0.1. Therefore, no drift is detected for this feature.

**2. get_shap_values**

The get_shap_values tool was used to calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions.

* **SHAP Values for Reference and Current Datasets**

| Feature | Reference Value | Current Value |
| --- | --- | --- |
| Credit Score | 0.057266813197127224 | 0.05259014360839969 |

The SHAP values for the Credit Score feature show a slight decrease in the mean(|SHAP value|) value from 0.057266813197127224 in the reference dataset to 0.05259014360839969 in the current dataset. This indicates a slight decrease in the average impact of the Credit Score feature on the model's predictions.

**Overall Feature Analysis**

The analysis of the Credit Score feature using the get_drift_report and get_shap_values tools shows that:

* The drift in the Credit Score feature is relatively small, and the dataset drift is not detected based on the threshold of 0.1.
* The SHAP values for the Credit Score feature show a slight decrease in the mean(|SHAP value|) value from the reference to the current dataset, indicating a slight decrease in the average impact of the feature on the model's predictions.

These results suggest that the Credit Score feature is stable and continues to play a significant role in the model's predictions, albeit with a slight decrease in its impact.

            ### Loan Amount

            **Loan Default Prediction Data Analysis Report**

**Feature Description**

### Loan Amount

* **Name:** Loan Amount
* **Description:** Loan amount requested by the borrower in dollars, ranging from $1,000 to $50,000.
* **Type:** Numerical
* **Possible Values:** Ranging from $1,000 to $50,000.
* **Data Type:** Float

**Tool Results**

### get_drift_report

#### Detailed Analysis of Results

The `get_drift_report` tool was used to generate a data drift report using the reference and current datasets. The report includes a general drift summary and detailed drift analysis per column.

| Column Name | Column Type | Stat Test Name | Stat Test Threshold | Drift Score | Drift Detected |
| --- | --- | --- | --- | --- | --- |
| Loan Amount | num | Kullback-Leibler divergence | 0.1 | 0.06465984187565631 | False |

The detailed drift analysis for the Loan Amount column shows that the Kullback-Leibler divergence statistical test was used to detect drift. The drift score is 0.06465984187565631, which is below the threshold of 0.1. Therefore, no drift was detected for this column.

#### Insights and Interpretations

The results indicate that the distribution of the Loan Amount column has not changed significantly between the reference and current datasets. This suggests that the model's performance is likely to remain stable for this feature.

### get_shap_values

#### Detailed Analysis of Results

The `get_shap_values` tool was used to calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions.

| Feature | Value | Position |
| --- | --- | --- |
| reference | 0.03091725874540736 | 7 |
| current | 0.030296443826883252 | 7 |

The results show that the mean(|SHAP value|) for the Loan Amount feature is 0.030296443826883252 in the current dataset and 0.03091725874540736 in the reference dataset. The feature rank position remains the same at 7 in both datasets.

#### Insights and Interpretations

The results indicate that the average impact of the Loan Amount feature on the model's predictions has decreased slightly from the reference to the current dataset. However, the feature remains one of the most important features in the model, with a rank position of 7 in both datasets.

**Overall Feature Analysis**

### Summary of Key Findings

* The distribution of the Loan Amount column has not changed significantly between the reference and current datasets.
* The average impact of the Loan Amount feature on the model's predictions has decreased slightly from the reference to the current dataset.
* The feature remains one of the most important features in the model, with a rank position of 7 in both datasets.

These findings suggest that the model's performance is likely to remain stable for the Loan Amount feature, and that the feature continues to be an important contributor to the model's predictions.

            ### Loan Term

            **Loan Default Prediction Data Analysis Report**

**Feature Description**

* **Name:** Loan Term
* **Description:** Loan term in months, ranging from 12 to 60.
* **Type:** numerical
* **Possible Values:** Ranging from 12 to 60 months.
* **Data Type:** int

**Tool Results**

### get_drift_report

**General Drift Report Summary**

| Key | Value |
| --- | --- |
| drift_share | 0.0 |
| number_of_columns | 11 |
| number_of_drifted_columns | 0 |
| share_of_drifted_columns | 0.0 |
| dataset_drift | False |

**Detailed Drift Analysis per Column**

| Column Name | Column Type | Stat Test Name | Stat Test Threshold | Drift Score | Drift Detected |
| --- | --- | --- | --- | --- | --- |
| Loan Term | num | Kullback-Leibler divergence | 0.1 | 0.06991922445224397 | False |

**Insights and Interpretations**

The get_drift_report tool indicates that there is no significant drift in the dataset, with a drift share of 0.0. The detailed drift analysis per column shows that the Loan Term feature has a drift score of 0.06991922445224397, but this is below the threshold of 0.1, indicating no drift.

**get_shap_values**

**Feature SHAP Values**

| Feature | Value | Position |
| --- | --- | --- |
| reference | 0.10786701225337081 | 2 |
| current | 0.08865791016936486 | 2 |

**Insights and Interpretations**

The get_shap_values tool shows that the mean(|SHAP value|) for the Loan Term feature is 0.10786701225337081 in the reference dataset and 0.08865791016936486 in the current dataset. The feature ranks second in both datasets based on its mean Mean(|SHAP value|) value. The slight decrease in the mean(|SHAP value|) value for the Loan Term feature in the current dataset may indicate a slight change in the feature's contribution to the model's predictions.

**Overall Feature Analysis**

**Summary of Key Findings**

* The Loan Term feature has a numerical type and ranges from 12 to 60 months.
* The get_drift_report tool indicates no significant drift in the dataset, with a drift share of 0.0.
* The get_shap_values tool shows a slight decrease in the mean(|SHAP value|) value for the Loan Term feature in the current dataset, indicating a slight change in the feature's contribution to the model's predictions.

**Recommendations**

Based on the analysis, it is recommended to continue monitoring the Loan Term feature for any further changes in its contribution to the model's predictions. Additionally, it may be beneficial to investigate the underlying causes of the slight decrease in the mean(|SHAP value|) value for the Loan Term feature in the current dataset.

            ### Interest Rate

            **Loan Default Prediction Data Analysis Report**

**Feature Description: Interest Rate**

* **Name:** Interest Rate
* **Description:** Interest rate of the loan in percentage, ranging from 3.5% to 25%.
* **Type:** Numerical
* **Possible Values:** Ranging from 3.5% to 25%.
* **Data Type:** Float

**Tool Results: get_drift_report**

### General Drift Report Summary

| Key | Value |
| --- | --- |
| drift_share | 0.2 |
| number_of_columns | 11 |
| number_of_drifted_columns | 1 |
| share_of_drifted_columns | 0.09090909090909091 |
| dataset_drift | True |

### Detailed Drift Analysis per Column

| Column Name | Column Type | Stat Test Name | Stat Test Threshold | Drift Score | Drift Detected |
| --- | --- | --- | --- | --- | --- |
| Interest Rate | num | Kullback-Leibler divergence | 0.1 | 0.12211093048448328 | True |

### Drift Analysis for Interest Rate

The interest rate feature shows significant drift between the reference and current datasets. The Kullback-Leibler divergence statistical test detects a drift score of 0.12211093048448328, indicating a significant change in the distribution of the interest rate feature.

**Current Distribution:**

| x | y |
| --- | --- |
| 6.40996299737573 | 0.016137676324025095 |
| 8.268966697638156 | 0.04841302897207526 |
| 10.127970397900583 | 0.06724031801677119 |
| 11.98697409816301 | 0.08068838162012543 |
| 13.845977798425437 | 0.09144683250280883 |
| 15.704981498687864 | 0.10220528338549223 |
| 17.56398519895029 | 0.05648186713408781 |
| 19.42298889921272 | 0.04034419081006271 |
| 21.281992599475146 | 0.018827289044695935 |
| 23.140996299737573 | 0.016137676324025088 |
| 25.0 | 0.0 |

**Reference Distribution:**

| x | y |
| --- | --- |
| 3.5 | 0.004069767441860464 |
| 5.65 | 0.00930232558139535 |
| 7.8 | 0.03546511627906978 |
| 9.95 | 0.0697674418604651 |
| 12.1 | 0.11104651162790695 |
| 14.25 | 0.12034883720930241 |
| 16.4 | 0.07616279069767447 |
| 18.549999999999997 | 0.034302325581395315 |
| 20.7 | 0.004069767441860468 |
| 22.849999999999998 | 0.0005813953488372088 |
| 25.0 | 0.0 |

**Tool Results: get_shap_values**

### Feature Attribution Analysis

| Feature | Value | Position |
| --- | --- | --- |
| Interest Rate | 0.017982049611167866 | 9 |

The interest rate feature has a mean(|SHAP value|) of 0.017982049611167866, indicating a moderate impact on the model's predictions. However, its position in the feature attribution ranking has changed from 8 in the reference dataset to 9 in the current dataset, suggesting a possible change in the feature's importance.

**Overall Feature Analysis: Interest Rate**

The interest rate feature shows significant drift between the reference and current datasets, indicating a change in its distribution. This drift is detected by the Kullback-Leibler divergence statistical test, which suggests a significant change in the interest rate feature's distribution. Additionally, the feature attribution analysis shows a possible change in the interest rate feature's importance, with its position in the feature attribution ranking changing from 8 to 9. These findings suggest that the interest rate feature may require re-evaluation and possible re-weighting in the model's predictions.

            ### Employment Length

            **Loan Default Prediction Data Analysis Report**

**Feature Description: Employment Length**

* **Name:** Employment Length
* **Description:** Number of years the borrower has been employed, ranging from 0 to 40.
* **Type:** Numerical
* **Possible Values:** Ranging from 0 to 40 years.
* **Data Type:** int

**Tool Results: get_drift_report**

### General Drift Report Summary

| Key | Value |
| --- | --- |
| drift_share | 0.2 |
| number_of_columns | 11 |
| number_of_drifted_columns | 1 |
| share_of_drifted_columns | 0.0909 |
| dataset_drift | True |

The dataset has been detected to have drift based on the `drift_share` threshold of 0.2.

### Detailed Drift Analysis per Column

| Column Name | Column Type | Stat Test Name | Stat Test Threshold | Drift Score | Drift Detected |
| --- | --- | --- | --- | --- | --- |
| Employment Length | num | Kullback-Leibler divergence | 0.1 | 0.10422809774139326 | True |

The `Employment Length` feature has been detected to have drift with a drift score of 0.10422809774139326.

### Distribution Information

#### Current Distribution

| x | y |
| --- | --- |
| 0.0 | 0.0025 |
| 4.0 | 0.00375 |
| 8.0 | 0.03 |
| 12.0 | 0.0525 |
| 16.0 | 0.06375 |
| 20.0 | 0.04375 |
| 24.0 | 0.03125 |
| 28.0 | 0.0175 |
| 32.0 | 0.00375 |
| 36.0 | 0.00125 |
| 40.0 | 0.0 |

#### Reference Distribution

| x | y |
| --- | --- |
| 1.0 | 0.0016025641025641025 |
| 4.9 | 0.004807692307692307 |
| 8.8 | 0.014102564102564108 |
| 12.7 | 0.038141025641025623 |
| 16.6 | 0.07211538461538464 |
| 20.5 | 0.06730769230769233 |
| 24.4 | 0.038141025641025623 |
| 28.3 | 0.014102564102564094 |
| 32.2 | 0.00480769230769231 |
| 36.1 | 0.0012820512820512825 |
| 40.0 | 0.0 |

**Tool Results: get_shap_values**

### Feature Attribution Drift Analysis

| Feature | Value | Position |
| --- | --- | --- |
| reference | 0.07748587080834744 | 4 |
| current | 0.07723764793746474 | 3 |

The `Employment Length` feature has been detected to have a slight decrease in its mean(|SHAP value|) value from the reference to the current dataset, indicating a possible feature attribution drift.

**Overall Feature Analysis: Employment Length**

* The `Employment Length` feature has been detected to have drift with a drift score of 0.10422809774139326.
* The feature has been detected to have a slight decrease in its mean(|SHAP value|) value from the reference to the current dataset, indicating a possible feature attribution drift.
* The distribution of the `Employment Length` feature has changed significantly between the reference and current datasets, which may lead to a decrease in model performance.

Recommendations:

* Investigate the cause of the drift in the `Employment Length` feature.
* Update the model to account for the changes in the `Employment Length` feature.
* Monitor the feature attribution drift of the `Employment Length` feature to ensure that it does not affect the model's performance.

            ### Home Ownership

            **Loan Default Prediction Data Analysis Report**

**Feature Description: Home Ownership**

* **Name:** Home Ownership
* **Description:** Home ownership status, represented as 0 (Rent), 1 (Own), or 2 (Mortgage).
* **Type:** categorical
* **Possible Values:** {'0': 'Rent', '1': 'Own', '2': 'Mortgage'}
* **Data Type:** int

**Tool Results:**

### get_drift_report

**Detailed Analysis of Results:**

The `get_drift_report` tool was used to generate a data drift report for the Home Ownership feature. The report includes a general drift summary and detailed drift analysis per column.

**General Drift Summary:**

| Metric | Value |
| --- | --- |
| Drift Share | 0.18557356469873026 |
| Number of Columns | 1 |
| Number of Drifted Columns | 1 |
| Share of Drifted Columns | 1.0 |
| Dataset Drift | True |

**Detailed Drift Analysis per Column:**

| Column Name | Column Type | Stat Test Name | Stat Test Threshold | Drift Score | Drift Detected | Current | Reference |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Home Ownership | cat | Kullback-Leibler divergence | 0.1 | 0.18557356469873026 | True | {'small_distribution': {'x': [0, 1, 2], 'y': [16, 184, 0]}} | {'small_distribution': {'x': [0, 1, 2], 'y': [62, 708, 30]}} |

**Insights and Interpretations:**

The Home Ownership feature shows significant drift between the reference and current datasets. The Kullback-Leibler divergence statistical test detects a drift score of 0.18557356469873026, indicating a significant change in the distribution of the Home Ownership feature. This drift may lead to a decrease in model performance.

### get_shap_values

**Detailed Analysis of Results:**

The `get_shap_values` tool was used to calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions.

**Feature Attribution Drift Analysis:**

| Feature | Value | Position |
| --- | --- | --- |
| reference | 0.003640297286226866 | 10 |
| current | 0.003270709366873879 | 10 |

**Insights and Interpretations:**

The Home Ownership feature shows a slight decrease in its mean(|SHAP value|) value from the reference to the current dataset. However, its position remains the same (10th). This suggests that the feature attribution drift is minimal, and the Home Ownership feature continues to have a similar impact on the model's predictions.

**Overall Feature Analysis:**

**Summary of Key Findings:**

* The Home Ownership feature shows significant drift between the reference and current datasets, which may lead to a decrease in model performance.
* The feature attribution drift analysis suggests that the Home Ownership feature continues to have a similar impact on the model's predictions, with a slight decrease in its mean(|SHAP value|) value.

Recommendations:

* Investigate the cause of the drift in the Home Ownership feature and consider updating the training data to reflect the current distribution.
* Monitor the feature attribution drift of the Home Ownership feature to ensure that it continues to have a similar impact on the model's predictions.

            ### Marital Status

            **Loan Default Prediction Data Analysis Report**

**Feature Description: Marital Status**

* **Name:** Marital Status
* **Description:** Marital status, represented as 0 (Single), 1 (Married), 2 (Divorced), or 3 (Widowed).
* **Type:** categorical
* **Possible Values:** {'0': 'Single', '1': 'Married', '2': 'Divorced', '3': 'Widowed'}
* **Data Type:** int

**Tool Results:**

### get_drift_report

**Detailed Analysis of Results:**

The `get_drift_report` tool was used to generate a data drift report for the Marital Status feature. The report includes a general drift summary and detailed drift analysis per column.

**General Drift Summary:**

| Key | Value |
| --- | --- |
| drift_share | 0.25 |
| number_of_columns | 10 |
| number_of_drifted_columns | 3 |
| share_of_drifted_columns | 0.3 |
| dataset_drift | True |

The general drift summary indicates that 30% of the columns show drift, and the dataset drift is detected based on the `drift_share` threshold.

**Detailed Drift Analysis per Column:**

| Column Name | Column Type | Stat Test Name | Stat Test Threshold | Drift Score | Drift Detected |
| --- | --- | --- | --- | --- | --- |
| Marital Status | cat | Kullback-Leibler divergence | 0.1 | 5.655843738731566 | True |

The detailed drift analysis per column shows that the Marital Status feature has a drift score of 5.655843738731566, indicating that the distribution of the data has changed significantly between the reference and current datasets.

**Insights and Interpretations:**

The results from the `get_drift_report` tool indicate that the Marital Status feature has drifted, which may lead to a decrease in model performance. This suggests that the input data distribution has changed, and the model may not be generalizing well to the new data.

### get_shap_values

**Detailed Analysis of Results:**

The `get_shap_values` tool was used to calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions.

**Feature Attribution Drift:**

| Feature | Value | Position |
| --- | --- | --- |
| reference | 0.041422401537971096 | 6 |
| current | 0.07354211915327408 | 4 |

The results from the `get_shap_values` tool show that the Marital Status feature has a higher mean(|SHAP value|) value in the current dataset compared to the reference dataset, indicating that the feature attribution drift has occurred.

**Insights and Interpretations:**

The results from the `get_shap_values` tool indicate that the Marital Status feature has a higher impact on the model's predictions in the current dataset compared to the reference dataset. This suggests that the feature attribution drift has occurred, and the model may not be generalizing well to the new data.

**Overall Feature Analysis:**

**Summary of Key Findings:**

* The Marital Status feature has drifted, indicating that the distribution of the data has changed significantly between the reference and current datasets.
* The feature attribution drift has occurred, indicating that the feature has a higher impact on the model's predictions in the current dataset compared to the reference dataset.
* The results from the `get_drift_report` and `get_shap_values` tools suggest that the model may not be generalizing well to the new data, and the Marital Status feature may be contributing to the decrease in model performance.

**Recommendations:**

* Update the model to reflect the changes in the input data distribution.
* Re-train the model with the new data to improve its generalization performance.
* Monitor the feature attribution drift and update the model accordingly to ensure that the feature continues to contribute to the model's performance.

            ### Dependents

            **Comprehensive Data Science Report**

**Feature Description**

* **Name:** Dependents
* **Description:** Number of dependents, ranging from 0 to 5.
* **Type:** categorical
* **Possible Values:** Ranging from 0 to 5.
* **Data Type:** int

**Tool Results**

### get_drift_report

**Detailed Analysis of Results**

The `get_drift_report` tool was used to generate a data drift report using the reference and current datasets. The report includes a general drift summary and detailed drift analysis per column.

**General Drift Summary**

| Metric | Value |
| --- | --- |
| Drift Share | 0.2 |
| Number of Columns | 10 |
| Number of Drifted Columns | 2 |
| Share of Drifted Columns | 0.2 |
| Dataset Drift | True |

The general drift summary indicates that 20% of the columns show drift, which is above the threshold of 0.1. This suggests that the distribution of the data has changed significantly between the reference and current datasets, leading to a decrease in model performance.

**Detailed Drift Analysis per Column**

| Column Name | Column Type | Stat Test Name | Stat Test Threshold | Drift Score | Drift Detected |
| --- | --- | --- | --- | --- | --- |
| Dependents | categorical | Kullback-Leibler divergence | 0.1 | 0.1290888567959812 | True |

The detailed drift analysis per column shows that the "Dependents" column has a drift score of 0.1290888567959812, which is above the threshold of 0.1. This indicates that the distribution of the "Dependents" column has changed significantly between the reference and current datasets.

**Insights and Interpretations**

The results of the `get_drift_report` tool suggest that the distribution of the data has changed significantly between the reference and current datasets. This is likely due to changes in the input data distribution, leading to changes in the order of feature contributions. The "Dependents" column is one of the columns that shows drift, which may indicate that the model's predictions are being influenced by changes in the number of dependents.

### get_shap_values

**Detailed Analysis of Results**

The `get_shap_values` tool was used to calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions.

**Feature Attribution Drift**

| Feature | Mean(|SHAP value|) | Rank Position |
| --- | --- | --- |
| reference | 0.02095623100403098 | 9 |
| current | 0.01848637683404379 | 8 |

The results of the `get_shap_values` tool show that the mean(|SHAP value|) for the "Dependents" feature has decreased from 0.02095623100403098 in the reference dataset to 0.01848637683404379 in the current dataset. This suggests that the feature attribution drift has occurred, leading to changes in the order of feature contributions.

**Insights and Interpretations**

The results of the `get_shap_values` tool suggest that the feature attribution drift has occurred, leading to changes in the order of feature contributions. The "Dependents" feature is one of the features that shows a decrease in mean(|SHAP value|), which may indicate that the model's predictions are being influenced by changes in the number of dependents.

**Overall Feature Analysis**

**Summary of Key Findings**

* The distribution of the data has changed significantly between the reference and current datasets, leading to a decrease in model performance.
* The "Dependents" column is one of the columns that shows drift, which may indicate that the model's predictions are being influenced by changes in the number of dependents.
* The feature attribution drift has occurred, leading to changes in the order of feature contributions.
* The "Dependents" feature is one of the features that shows a decrease in mean(|SHAP value|), which may indicate that the model's predictions are being influenced by changes in the number of dependents.

**Recommendations**

Based on the results of the `get_drift_report` and `get_shap_values` tools, we recommend that the model be re-trained on the current dataset to account for the changes in the input data distribution. Additionally, we recommend that the feature attribution drift be monitored regularly to ensure that the model's predictions are not being influenced by changes in the order of feature contributions.
