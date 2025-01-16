
        # Loan Default Prediction Data - Deep Insight Report

        ## Overview
        Overview report

        ## Details

        ### Label Insight


The label "Loan Default" in the "Loan Default Prediction Data" dataset is a categorical variable that indicates the likelihood of a borrower defaulting on a loan. It takes two possible values: 

* 0, which represents "No default", meaning the borrower is not likely to default on the loan.
* 1, which represents "Default", meaning the borrower is likely to default on the loan.

In other words, a value of 0 indicates a low risk of loan default, while a value of 1 indicates a high risk of loan default. The label is of type integer (int), which is a common representation for categorical variables in machine learning and data analysis.

Based on the available information, there are no apparent issues with the label. The description, possible values, and data type are all clear and consistent, making it easy to understand and work with the label in a predictive modeling context.


            ### Marital Status



**Feature Description**

* **Name:** Marital Status
* **Description:** Marital status, represented as 0 (Single), 1 (Married), 2 (Divorced), or 3 (Widowed)
* **Type:** categorical
* **Possible Values:** {'0': 'Single', '1': 'Married', '2': 'Divorced', '3': 'Widowed'}
* **Data Type:** int

**Tool Results**

**get_drift_report**

The get_drift_report tool was used to analyze the Marital Status feature for data drift between the reference and current datasets. The results are as follows:

* **Column Name:** Marital Status
* **Column Type:** categorical
* **Statistical Test:** Kullback-Leibler divergence
* **Statistical Test Threshold:** 0.1
* **Drift Score:** 5.655843738731566
* **Drift Detected:** True
* **Current Distribution:** {'x': [0, 1, 2, 3], 'y': [2, 1, 0, 197]}
* **Reference Distribution:** {'x': [0, 1, 2, 3], 'y': [20, 538, 237, 5]}

The results indicate that the Marital Status feature has drifted between the reference and current datasets, with a drift score of 5.655843738731566. The distributions of the current and reference datasets are significantly different, suggesting that the model's performance may be affected.

**get_shap_values**

The get_shap_values tool was used to calculate the mean(|SHAP value|) for the Marital Status feature to show its average impact on the model's predictions. The results are as follows:

* **Reference:** {'value': 0.041422401537971096, 'position': 6}
* **Current:** {'value': 0.07354211915327408, 'position': 4}

The results indicate that the Marital Status feature has a higher mean(|SHAP value|) in the current dataset compared to the reference dataset, suggesting that its impact on the model's predictions has increased. The feature's rank position has also changed from 6 to 4, indicating a shift in its importance.

**Overall Feature Analysis**

The analysis of the Marital Status feature using the get_drift_report and get_shap_values tools reveals that the feature has drifted between the reference and current datasets, and its impact on the model's predictions has increased. The drift in the feature's distribution may affect the model's performance, and the change in its importance may require adjustments to the model or feature engineering.

            ### Loan Amount



**Loan Default Prediction Data: Feature Analysis Report**

**Feature Description**

* **Name:** Loan Amount
* **Description:** Loan amount requested by the borrower in dollars, ranging from $1,000 to $50,000.
* **Type:** Numerical
* **Possible Values:** Ranging from $1,000 to $50,000.
* **Data Type:** Float

**Tool Results**

### get_drift_report

The get_drift_report tool was used to analyze the distribution of the Loan Amount feature between the reference and current datasets. The results are as follows:

* **Column Name:** Loan Amount
* **Column Type:** Numerical
* **Statistical Test:** Kullback-Leibler divergence
* **Statistical Test Threshold:** 0.1
* **Drift Score:** 0.06465984187565631
* **Drift Detected:** False

The drift score indicates that there is no significant distribution drift detected in the Loan Amount feature between the reference and current datasets.

### get_shap_values

The get_shap_values tool was used to calculate the mean(|SHAP value|) for the Loan Amount feature to show its average impact on the model's predictions. The results are as follows:

* **Reference:** {'value': 0.03091725874540736, 'position': 7}
* **Current:** {'value': 0.030296443826883252, 'position': 7}

The mean(|SHAP value|) for the Loan Amount feature is 0.03091725874540736 in the reference dataset and 0.030296443826883252 in the current dataset, indicating a relatively consistent contribution to the model's predictions.

**Overall Feature Analysis**

The analysis of the Loan Amount feature using the get_drift_report and get_shap_values tools reveals that there is no significant distribution drift detected between the reference and current datasets. Additionally, the feature's contribution to the model's predictions remains consistent, with a mean(|SHAP value|) of approximately 0.0309 in both datasets. This suggests that the Loan Amount feature is a stable and important predictor of loan default likelihood.

            ### Age

            **Loan Default Prediction Data: Age Feature Analysis**

**Feature Description**

* **Name:** Age
* **Description:** Age of the borrower in years, ranging from 18 to 70.
* **Type:** numerical
* **Possible Values:** Ranging from 18 to 70 years.
* **Data Type:** int

**Tool Results**

### get_drift_report

The get_drift_report tool was used to generate a data drift report for the Age feature. The results indicate that there is no drift detected for this feature.

* **Column Name:** Age
* **Column Type:** numerical
* **Statistical Test:** Kullback-Leibler divergence
* **Statistical Test Threshold:** 0.1
* **Drift Score:** 0.03883719590118
* **Drift Detected:** False

The distribution information for the current and reference datasets is provided below:

* **Current Dataset:**
	+ Small Distribution: x = [27.0, 31.0, 35.0, 39.0, 43.0, 47.0, 51.0, 55.0, 59.0, 63.0, 67.0]
	y = [0.0025, 0.00375, 0.01625, 0.0175, 0.06125, 0.0575, 0.04125, 0.0325, 0.01125, 0.00625]
* **Reference Dataset:**
	+ Small Distribution: x = [18.0, 23.2, 28.4, 33.6, 38.8, 44.0, 49.2, 54.4, 59.6, 64.80000000000001, 70.0]
	y = [0.00024038461538461543, 0.0007211538461538462, 0.00456730769230769, 0.01418269230769232, 0.036298076923076905, 0.05697115384615382, 0.0432692307692308, 0.023076923076923064, 0.010336538461538442, 0.002644230769230775]

### get_shap_values

The get_shap_values tool was used to calculate the mean(|SHAP value|) for the Age feature to determine its average impact on the model's predictions.

* **Reference Dataset:**
	+ Mean(|SHAP value|): 0.08155174483476563
	+ Position: 3
* **Current Dataset:**
	+ Mean(|SHAP value|): 0.05350981388279517
	+ Position: 5

**Overall Feature Analysis**

Based on the results from the get_drift_report and get_shap_values tools, the following insights can be drawn about the Age feature:

* There is no significant drift detected in the Age feature between the reference and current datasets, indicating that the distribution of Age values has not changed significantly.
* The mean(|SHAP value|) for the Age feature has decreased from 0.0816 in the reference dataset to 0.0535 in the current dataset, suggesting that the feature's impact on the model's predictions has decreased.
* The position of the Age feature in terms of its mean(|SHAP value|) has dropped from 3 to 5, indicating that other features may have become more important in the model's predictions.

These findings suggest that while the Age feature remains an important predictor in the loan default prediction model, its importance has decreased slightly in the current dataset.

            ### Interest Rate

            **Loan Default Prediction Data: Interest Rate Feature Analysis**

**Feature Description**

* **Name:** Interest Rate
* **Description:** Interest rate of the loan in percentage, ranging from 3.5% to 25%.
* **Type:** numerical
* **Possible Values:** Ranging from 3.5% to 25%.
* **Data Type:** float

**Tool Results**

### get_drift_report

The get_drift_report tool was used to analyze the distribution of the Interest Rate feature in the reference and current datasets. The results indicate that drift has been detected in this feature.

* **Drift Summary:**
	+ `drift_detected`: True
	+ `drift_score`: 0.12211093048448328
* **Detailed Drift Analysis:**
	+ `column_name`: Interest Rate
	+ `column_type`: numerical
	+ `stattest_name`: Kullback-Leibler divergence
	+ `stattest_threshold`: 0.1
	+ `current`: Distribution information of the current dataset, showing a shifted distribution with a higher proportion of higher interest rates.
	+ `reference`: Distribution information of the reference dataset, showing a more even distribution of interest rates.

### get_shap_values

The get_shap_values tool was used to calculate the mean(|SHAP value|) for the Interest Rate feature in both the reference and current datasets. The results indicate a decrease in the average impact of the Interest Rate feature on the model's predictions.

* **Reference:**
	+ `value`: 0.02195194757664086
	+ `position`: 8
* **Current:**
	+ `value`: 0.017982049611167866
	+ `position`: 9

**Overall Feature Analysis**

The Interest Rate feature has undergone significant changes between the reference and current datasets. The get_drift_report results indicate that the distribution of interest rates has shifted, with a higher proportion of higher interest rates in the current dataset. This drift may lead to a decrease in model performance if not addressed.

Furthermore, the get_shap_values results suggest that the average impact of the Interest Rate feature on the model's predictions has decreased, indicating a potential change in the feature's importance in the model. This decrease in importance may be related to the drift detected in the feature's distribution.

Overall, these results highlight the need for further investigation into the Interest Rate feature and its relationship with other features in the dataset. The model may require retraining or updating to accommodate these changes and maintain its predictive performance.

            ### Loan Term

            **Loan Default Prediction Data: Feature Analysis Report**

**Feature Description**

* **Name:** Loan Term
* **Description:** Loan term in months, ranging from 12 to 60.
* **Type:** numerical
* **Possible Values:** Ranging from 12 to 60 months.
* **Data Type:** int

**Tool Results**

### get_drift_report

The get_drift_report tool was used to detect data drift in the Loan Term feature between the reference and current datasets. The results are as follows:

* **Column Name:** Loan Term
* **Column Type:** numerical
* **Statistical Test:** Kullback-Leibler divergence
* **Statistical Test Threshold:** 0.1
* **Drift Score:** 0.06991922445224397
* **Drift Detected:** False

The drift report indicates that no significant drift was detected in the Loan Term feature between the reference and current datasets. The distribution of the Loan Term feature in the current dataset is similar to that of the reference dataset.

### get_shap_values

The get_shap_values tool was used to calculate the mean(|SHAP value|) for the Loan Term feature to show its average impact on the model's predictions. The results are as follows:

* **Reference:** {'value': 0.10786701225337081, 'position': 2}
* **Current:** {'value': 0.08865791016936486, 'position': 2}

The SHAP values indicate that the Loan Term feature has a moderate impact on the model's predictions, ranking second in terms of feature importance. The mean(|SHAP value|) for the Loan Term feature has decreased slightly from the reference dataset to the current dataset, suggesting a possible change in the feature's contribution to the model's predictions.

**Overall Feature Analysis**

The analysis of the Loan Term feature using the get_drift_report and get_shap_values tools provides the following insights:

* No significant drift was detected in the Loan Term feature between the reference and current datasets, indicating that the distribution of the feature has remained relatively stable.
* The Loan Term feature has a moderate impact on the model's predictions, ranking second in terms of feature importance.
* The mean(|SHAP value|) for the Loan Term feature has decreased slightly from the reference dataset to the current dataset, suggesting a possible change in the feature's contribution to the model's predictions.

These insights suggest that the Loan Term feature is an important predictor of loan default, but its contribution to the model's predictions may have changed slightly between the reference and current datasets. Further analysis is recommended to investigate the reasons behind this change and to assess its impact on the overall model performance.

            ### Credit Score

            **Loan Default Prediction Data: Credit Score Feature Analysis Report**

**Feature Description**

* **Name:** Credit Score
* **Description:** Credit score of the borrower, ranging from 300 to 850.
* **Type:** numerical
* **Possible Values:** Ranging from 300 to 850.
* **Data Type:** int

**Tool Results**

### get_drift_report

The get_drift_report tool was used to analyze the distribution of the Credit Score feature between the reference and current datasets. The results indicate that:

* **Drift Detected:** False
* **Drift Score:** 0.0778065393961156
* **Statistical Test:** Kullback-Leibler divergence
* **Threshold:** 0.1

The detailed drift analysis per column shows that the distribution of the Credit Score feature has not significantly changed between the reference and current datasets. The drift score of 0.0778065393961156 is below the threshold of 0.1, indicating no drift.

### get_shap_values

The get_shap_values tool was used to calculate the mean(|SHAP value|) for the Credit Score feature in both the reference and current datasets. The results indicate that:

* **Reference:** Mean(|SHAP value|) = 0.057266813197127224, Position = 5
* **Current:** Mean(|SHAP value|) = 0.05259014360839969, Position = 6

The mean(|SHAP value|) for the Credit Score feature has decreased slightly from 0.057266813197127224 in the reference dataset to 0.05259014360839969 in the current dataset. The position of the feature has also changed from 5 to 6, indicating a slight shift in its importance in the model's predictions.

**Overall Feature Analysis**

The analysis of the Credit Score feature using the get_drift_report and get_shap_values tools provides valuable insights into its distribution and importance in the model's predictions.

* The get_drift_report results indicate that the distribution of the Credit Score feature has not significantly changed between the reference and current datasets, suggesting that the model's performance is not likely to be affected by data drift.
* The get_shap_values results show that the Credit Score feature is an important contributor to the model's predictions, but its importance has decreased slightly in the current dataset.

These insights can be used to inform model updates and improvements, ensuring that the Credit Score feature is properly accounted for in the loan default prediction model.

            ### Home Ownership

            **Loan Default Prediction Data: Feature Analysis Report**

**Feature Description**

* **Name:** Home Ownership
* **Description:** Home ownership status, represented as 0 (Rent), 1 (Own), or 2 (Mortgage)
* **Type:** categorical
* **Possible Values:** {'0': 'Rent', '1': 'Own', '2': 'Mortgage'}
* **Data Type:** int

**Tool Results**

### get_drift_report

* **General Drift Report Summary:**
	+ The dataset exhibits drift, with a drift share of 0.18557356469873026, indicating a significant change in the distribution of the Home Ownership feature between the reference and current datasets.
	+ A total of 1 out of 10 columns (10%) show drift.
* **Detailed Drift Analysis per Column:**
	+ **Column Name:** Home Ownership
	+ **Column Type:** categorical
	+ **Statistical Test:** Kullback-Leibler divergence
	+ **Statistical Test Threshold:** 0.1
	+ **Drift Score:** 0.18557356469873026
	+ **Drift Detected:** True
	+ **Current Distribution:** {'small_distribution': {'x': [0, 1, 2], 'y': [16, 184, 0]}}
	+ **Reference Distribution:** {'small_distribution': {'x': [0, 1, 2], 'y': [62, 708, 30]}}

The drift report indicates that the distribution of the Home Ownership feature has changed significantly between the reference and current datasets, which may lead to a decrease in model performance.

### get_shap_values

* **Feature Attribution:**
	+ **Reference:** Mean(|SHAP value|) = 0.003640297286226866, Position = 10
	+ **Current:** Mean(|SHAP value|) = 0.003270709366873879, Position = 10

The SHAP values suggest that the Home Ownership feature has a relatively low impact on the model's predictions, ranking 10th in both the reference and current datasets. However, there is a slight decrease in the mean absolute SHAP value from the reference to the current dataset, indicating a potential change in the feature's contribution to the model's predictions.

**Overall Feature Analysis**

The analysis reveals that the Home Ownership feature exhibits drift between the reference and current datasets, which may impact model performance. Additionally, the SHAP values indicate a slight change in the feature's contribution to the model's predictions. These findings suggest that the Home Ownership feature should be further investigated and potentially re-engineered to ensure that the model remains robust and accurate in the face of changing data distributions.

            ### Employment Length

            **Loan Default Prediction Data: Employment Length Feature Analysis**

**Feature Description**

* **Name:** Employment Length
* **Description:** Number of years the borrower has been employed, ranging from 0 to 40.
* **Type:** Numerical
* **Possible Values:** Ranging from 0 to 40 years.
* **Data Type:** int

**Tool Results**

### get_drift_report

The get_drift_report tool was used to analyze the distribution of the Employment Length feature in the reference and current datasets. The results indicate that drift has been detected in this feature.

* **Column Name:** Employment Length
* **Column Type:** Numerical
* **Statistical Test:** Kullback-Leibler divergence
* **Statistical Test Threshold:** 0.1
* **Drift Score:** 0.10422809774139326
* **Drift Detected:** True

The drift report shows that the distribution of the Employment Length feature has changed significantly between the reference and current datasets. The Kullback-Leibler divergence test detected a drift score of 0.10422809774139326, which exceeds the threshold of 0.1, indicating drift.

The distribution plots for the current and reference datasets are shown below:

**Current Dataset:**

* **x:** [0.0, 4.0, 8.0, 12.0, 16.0, 20.0, 24.0, 28.0, 32.0, 36.0, 40.0]
* **y:** [0.0025, 0.00375, 0.03, 0.0525, 0.06375, 0.04375, 0.03125, 0.0175, 0.00375, 0.00125]

**Reference Dataset:**

* **x:** [1.0, 4.9, 8.8, 12.7, 16.6, 20.5, 24.4, 28.3, 32.2, 36.1, 40.0]
* **y:** [0.0016025641025641025, 0.004807692307692307, 0.014102564102564108, 0.038141025641025623, 0.07211538461538464, 0.06730769230769233, 0.038141025641025623, 0.014102564102564094, 0.00480769230769231, 0.0012820512820512825]

### get_shap_values

The get_shap_values tool was used to calculate the mean(|SHAP value|) for the Employment Length feature in the reference and current datasets.

* **Reference:** {'value': 0.07748587080834744, 'position': 4}
* **Current:** {'value': 0.07723764793746474, 'position': 3}

The results show that the mean(|SHAP value|) for the Employment Length feature has changed slightly between the reference and current datasets. The feature's position in the ranking of feature contributions has also changed from 4 to 3.

**Overall Feature Analysis**

The results from the get_drift_report and get_shap_values tools indicate that the Employment Length feature has undergone significant changes between the reference and current datasets. The drift detected in the feature's distribution may lead to a decrease in model performance if not addressed. The change in the feature's contribution to the model's predictions, as indicated by the SHAP values, may also impact the model's accuracy.

In conclusion, the Employment Length feature requires further investigation and potentially, adjustments to the model to ensure that it remains accurate and reliable in predicting loan defaults.

            ### Income

            **Loan Default Prediction Data: Feature Analysis Report**

**Feature Description**

* **Name:** Income
* **Description:** Annual income of the borrower in dollars, ranging from $20,000 to $150,000.
* **Type:** numerical
* **Possible Values:** Ranging from $20,000 to $150,000.
* **Data Type:** float

**Tool Results**

### get_drift_report

The get_drift_report tool was used to analyze the distributional drift of the Income feature between the reference and current datasets.

* **Drift Detected:** True
* **Drift Score:** 0.130772018665271
* **Statistical Test:** Kullback-Leibler divergence
* **Statistical Test Threshold:** 0.1

The drift report indicates that the distribution of the Income feature has changed significantly between the reference and current datasets, with a drift score of 0.130772. This suggests that the model's performance may be affected by this drift.

The detailed drift analysis per column is presented below:

| Column Name | Column Type | Drift Detected | Drift Score | Current Distribution | Reference Distribution |
| --- | --- | --- | --- | --- | --- |
| Income | numerical | True | 0.130772 | {'x': [25501.46, 37951.31, 50401.16, 62851.02, 75300.87, 87750.73, 100200.58, 112650.44, 125100.29, 137550.15, 150000.0], 'y': [8.03e-07, 6.02e-06, 6.02e-06, 1.81e-05, 1.41e-05, 1.04e-05, 9.64e-06, 6.83e-06, 4.02e-06, 4.42e-06]} | {'x': [20000.0, 32745.3, 45490.6, 58235.9, 70981.2, 83726.5, 96471.8, 109217.1, 121962.4, 134707.7, 147453.0], 'y': [3.92e-07, 1.96e-06, 7.94e-06, 1.48e-05, 1.94e-05, 1.94e-05, 9.42e-06, 3.73e-06, 1.18e-06, 1.96e-07]} |

### get_shap_values

The get_shap_values tool was used to calculate the mean(|SHAP value|) for the Income feature to show its average impact on the model's predictions.

* **Reference:** {'value': 0.13983600738410132, 'position': 1}
* **Current:** {'value': 0.1676025103420878, 'position': 1}

The SHAP values indicate that the Income feature has a significant impact on the model's predictions, with a mean(|SHAP value|) of 0.1398 in the reference dataset and 0.1676 in the current dataset. The position of the feature remains the same, indicating that the Income feature is still the most important feature in the current dataset.

**Overall Feature Analysis**

The analysis of the Income feature using the get_drift_report and get_shap_values tools suggests that:

* The distribution of the Income feature has changed significantly between the reference and current datasets, which may affect the model's performance.
* The Income feature has a significant impact on the model's predictions, and its importance has increased in the current dataset.

These findings highlight the need to retrain the model using the current dataset and to monitor the distributional drift of the Income feature to ensure that the model remains accurate and reliable.

            ### Dependents

            **Loan Default Prediction Data: Feature Analysis Report**

**Feature Description**

* **Name:** Dependents
* **Description:** Number of dependents, ranging from 0 to 5
* **Type:** Categorical
* **Possible Values:** Ranging from 0 to 5
* **Data Type:** int

**Tool Results**

### get_drift_report

The get_drift_report tool was used to generate a data drift report for the Dependents feature. The results are as follows:

* **Drift Detected:** True
* **Drift Score:** 0.1290888567959812
* **Statistical Test:** Kullback-Leibler divergence
* **Statistical Test Threshold:** 0.1
* **Current Distribution:** {'small_distribution': {'x': [0, 1, 2, 3, 4, 5], 'y': [0, 2, 29, 78, 69, 22]}}
* **Reference Distribution:** {'small_distribution': {'x': [0, 1, 2, 3, 4, 5], 'y': [2, 20, 178, 385, 207, 8]}}

The drift report indicates that the distribution of the Dependents feature has changed significantly between the reference and current datasets, with a drift score of 0.1290888567959812. This suggests that the model's performance may be affected by this change.

### get_shap_values

The get_shap_values tool was used to calculate the mean(|SHAP value|) for the Dependents feature to show the average impact of this feature on the model's predictions. The results are as follows:

* **Reference:** {'value': 0.02095623100403098, 'position': 9}
* **Current:** {'value': 0.01848637683404379, 'position': 8}

The SHAP values indicate that the Dependents feature has a relatively low impact on the model's predictions, with a mean(|SHAP value|) of 0.02095623100403098 in the reference dataset and 0.01848637683404379 in the current dataset. The feature's position in terms of importance has also changed from 9 to 8 between the reference and current datasets.

**Overall Feature Analysis**

The analysis of the Dependents feature using the get_drift_report and get_shap_values tools reveals that:

* The distribution of the Dependents feature has changed significantly between the reference and current datasets, indicating data drift.
* The feature has a relatively low impact on the model's predictions, but its importance has changed between the reference and current datasets.

These findings suggest that the model's performance may be affected by the changes in the Dependents feature, and that retraining the model with the current dataset may be necessary to maintain its accuracy. Additionally, the Dependents feature may not be as important as other features in the dataset, but its contribution to the model's predictions should still be considered.
