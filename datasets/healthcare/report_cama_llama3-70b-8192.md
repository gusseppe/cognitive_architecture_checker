
        # Chronic Condition Prediction Data - Deep Insight Report

        ## Overview
        Overview report

        ## Details

        ### Label Insight


The label "ChronicCondition" in the Chronic Condition Prediction Data dataset is a categorical variable that indicates the likelihood of an individual developing a chronic condition. It has two possible values: '0' and '1'.

A value of '0' represents "No chronic condition", indicating that the individual is not likely to develop a chronic condition. On the other hand, a value of '1' represents "Chronic condition", indicating that the individual is likely to develop a chronic condition.

The label is of type integer (int), which is suitable for a categorical variable with two distinct classes. The label serves as the target variable in the dataset, and the goal is to predict the likelihood of an individual developing a chronic condition based on the provided attributes such as Age, BMI, Blood Pressure, and others.

Based on the available information, there are no apparent issues with the label. The description is clear, and the possible values are well-defined. However, it would be beneficial to have more information about the specific chronic condition being predicted, as well as the criteria used to determine the likelihood of developing it.


            ### Age



**Chronic Condition Prediction Data: Feature Analysis Report**

**Feature Description**

* **Name:** Age
* **Description:** Age of the individual in years, ranging from 18 to 90.
* **Type:** Numerical
* **Possible Values:** Ranging from 18 to 90 years.
* **Data Type:** int

**Tool Results**

### get_drift_report

The get_drift_report tool is used to detect data drift between the reference and current datasets. The results indicate that the Age feature does not show drift, with a drift score of 0.03778629771302727, which is below the threshold of 0.1.

* **Drift Detected:** False
* **Drift Score:** 0.03778629771302727
* **Statistical Test:** Kullback-Leibler divergence
* **Statistical Test Threshold:** 0.1
* **Current Distribution:** The distribution of the current dataset shows a peak around 53 years, with a range of values from 31 to 86 years.
* **Reference Distribution:** The distribution of the reference dataset shows a peak around 46.8 years, with a range of values from 18 to 90 years.

### get_shap_values

The get_shap_values tool is used to calculate the mean(|SHAP value|) for each feature, which represents the average impact of each feature on the model's predictions. The results indicate that the Age feature has a mean(|SHAP value|) of 0.08906002648096621 in the reference dataset and 0.050937679805919664 in the current dataset, ranking 3rd and 5th, respectively, in terms of feature importance.

* **Reference:** Mean(|SHAP value|) = 0.08906002648096621, Rank = 3
* **Current:** Mean(|SHAP value|) = 0.050937679805919664, Rank = 5

**Overall Feature Analysis**

The Age feature does not show drift between the reference and current datasets, indicating that the distribution of Age values has remained relatively consistent. However, the feature's importance in the model's predictions has decreased, as shown by the lower mean(|SHAP value|) in the current dataset. This suggests that other features may have become more influential in the model's predictions.

**Key Findings:**

* The Age feature does not show drift between the reference and current datasets.
* The Age feature's importance in the model's predictions has decreased in the current dataset.
* The distribution of Age values in the current dataset shows a peak around 53 years, with a range of values from 31 to 86 years.

These findings provide insights into the Age feature's behavior and importance in the Chronic Condition Prediction Data. The absence of drift suggests that the Age feature remains a stable and consistent predictor, while the decrease in importance may indicate changes in the relationships between features or the underlying data distribution.

            ### Diet Quality



**Chronic Condition Prediction Data: Feature Analysis Report**

**Feature Description**

* **Name:** Diet Quality
* **Description:** Quality of diet, represented as 0 (poor), 1 (average), or 2 (good).
* **Type:** categorical
* **Possible Values:** {'0': 'Poor', '1': 'Average', '2': 'Good'}
* **Data Type:** int

**Tool Results**

### get_drift_report

The get_drift_report tool was used to analyze the distribution of the Diet Quality feature in both the reference and current datasets. The results are as follows:

* **Column Name:** Diet Quality
* **Column Type:** categorical
* **Statistical Test:** Kullback-Leibler divergence
* **Statistical Test Threshold:** 0.1
* **Drift Score:** 0.0018915553873695345
* **Drift Detected:** False
* **Current Distribution:** {'x': [0, 1, 2], 'y': [10, 180, 10]}
* **Reference Distribution:** {'x': [0, 1, 2], 'y': [30, 727, 43]}

The results indicate that there is no significant drift detected in the Diet Quality feature between the reference and current datasets.

### get_shap_values

The get_shap_values tool was used to calculate the mean(|SHAP value|) for the Diet Quality feature in both the reference and current datasets. The results are as follows:

* **Reference:** {'value': 0.013835053054035294, 'position': 9}
* **Current:** {'value': 0.011401517327642103, 'position': 9}

The results indicate that the Diet Quality feature has a similar ranking position in both datasets, with a slight decrease in its mean(|SHAP value|) in the current dataset.

**Overall Feature Analysis**

The analysis of the Diet Quality feature using the get_drift_report and get_shap_values tools reveals that:

* There is no significant drift detected in the Diet Quality feature between the reference and current datasets, indicating that the distribution of the feature has not changed significantly.
* The Diet Quality feature has a similar ranking position in both datasets, with a slight decrease in its mean(|SHAP value|) in the current dataset, indicating that its contribution to the model's predictions has not changed significantly.

These findings suggest that the Diet Quality feature is relatively stable and consistent across both datasets, and its contribution to the model's predictions is consistent with the overall dataset characteristics.

            ### Physical Activity



**Chronic Condition Prediction Data: Feature Analysis Report**

**Feature Description**

* **Name:** Physical Activity
* **Description:** Number of days per week the individual engages in physical activity, ranging from 0 to 7.
* **Type:** numerical
* **Possible Values:** Ranging from 0 to 7 days per week.
* **Data Type:** int

**Tool Results**

### get_drift_report

The get_drift_report tool was used to analyze the distribution of the Physical Activity feature in the reference and current datasets. The results indicate that drift is detected in this feature.

* **Column Name:** Physical Activity
* **Column Type:** num
* **Statistical Test Name:** Kullback-Leibler divergence
* **Statistical Test Threshold:** 0.1
* **Drift Score:** 7.48442577690803
* **Drift Detected:** True
* **Current Distribution:** The distribution of Physical Activity in the current dataset is skewed to the right, with a peak at 0.8292978352142784 days per week.
* **Reference Distribution:** The distribution of Physical Activity in the reference dataset is skewed to the left, with a peak at 0.0 days per week.

The drift detected in the Physical Activity feature suggests that the distribution of this feature has changed significantly between the reference and current datasets, which may lead to a decrease in model performance.

### get_shap_values

The get_shap_values tool was used to calculate the mean(|SHAP value|) for the Physical Activity feature in the reference and current datasets. The results indicate the average impact of this feature on the model's predictions.

* **Reference:** The mean(|SHAP value|) for Physical Activity in the reference dataset is 0.09817662833236682, ranking 2nd in terms of feature importance.
* **Current:** The mean(|SHAP value|) for Physical Activity in the current dataset is 0.07730394004727022, ranking 3rd in terms of feature importance.

The decrease in mean(|SHAP value|) and ranking position suggests that the Physical Activity feature has become less important in the current dataset, which may be due to changes in the distribution of this feature.

**Overall Feature Analysis**

The analysis of the Physical Activity feature using the get_drift_report and get_shap_values tools reveals that:

* Drift is detected in the Physical Activity feature, indicating a significant change in its distribution between the reference and current datasets.
* The feature's importance has decreased in the current dataset, as indicated by the lower mean(|SHAP value|) and ranking position.

These findings suggest that the Physical Activity feature may require re-evaluation and potential re-training of the model to ensure accurate predictions in the current dataset.

            ### Blood Pressure

            **Chronic Condition Prediction Data: Blood Pressure Feature Analysis Report**

**Feature Description**

* **Name:** Blood Pressure
* **Description:** Systolic blood pressure of the individual in mmHg, ranging from 80 to 180.
* **Type:** numerical
* **Possible Values:** Ranging from 80 to 180 mmHg.
* **Data Type:** int

**Tool Results**

### get_drift_report

The get_drift_report tool was used to analyze the distribution of the Blood Pressure feature between the reference and current datasets. The results are as follows:

* **Drift Detected:** True
* **Drift Score:** 0.3296
* **Statistical Test:** Kullback-Leibler divergence
* **Statistical Test Threshold:** 0.1
* **Current Distribution:** The current distribution of Blood Pressure values shows a slight shift towards lower values, with a higher density around 80-100 mmHg.
* **Reference Distribution:** The reference distribution of Blood Pressure values is more uniform, with a higher density around 120-140 mmHg.

The drift detection suggests that the distribution of Blood Pressure values has changed significantly between the reference and current datasets, which may lead to a decrease in model performance.

### get_shap_values

The get_shap_values tool was used to calculate the mean(|SHAP value|) for the Blood Pressure feature to show its average impact on the model's predictions. The results are as follows:

* **Reference:** Mean(|SHAP value|) = 0.0711, Position = 4
* **Current:** Mean(|SHAP value|) = 0.0536, Position = 4

The results indicate that the Blood Pressure feature is ranked 4th in terms of its contribution to the model's predictions in both the reference and current datasets. However, the mean(|SHAP value|) has decreased in the current dataset, suggesting a potential change in the feature's importance.

**Overall Feature Analysis**

The analysis of the Blood Pressure feature using the get_drift_report and get_shap_values tools reveals some interesting insights:

* The distribution of Blood Pressure values has changed significantly between the reference and current datasets, indicating data drift.
* The Blood Pressure feature is still an important contributor to the model's predictions, but its importance has decreased in the current dataset.

These findings suggest that the model may need to be re-trained or updated to accommodate the changes in the Blood Pressure feature distribution. Additionally, further analysis is required to understand the underlying causes of the data drift and its impact on the model's performance.

            ### Cholesterol

            **Chronic Condition Prediction Data: Feature Analysis Report**

**Feature Description**

* **Name:** Cholesterol
* **Description:** Total cholesterol level of the individual in mg/dL, ranging from 150 to 300.
* **Type:** Numerical
* **Possible Values:** Ranging from 150 to 300 mg/dL.
* **Data Type:** int

**Tool Results**

### get_drift_report

The get_drift_report tool was used to analyze the Cholesterol feature for data drift. The results indicate that drift was detected in this feature.

* **Drift Detection:** True
* **Drift Score:** 0.23450676168929094
* **Statistical Test:** Kullback-Leibler divergence
* **Statistical Test Threshold:** 0.1

The drift report shows a significant difference in the distribution of Cholesterol values between the reference and current datasets. The current dataset has a more dispersed distribution, with a higher frequency of values at the lower and upper ends of the range.

### get_shap_values

The get_shap_values tool was used to calculate the mean(|SHAP value|) for the Cholesterol feature in both the reference and current datasets. The results show the average impact of the Cholesterol feature on the model's predictions.

* **Reference:** Mean(|SHAP value|) = 0.03926329553692529, Position = 6
* **Current:** Mean(|SHAP value|) = 0.04945714499086426, Position = 6

The results indicate that the Cholesterol feature has a similar rank position in both datasets, but the mean(|SHAP value|) has increased in the current dataset. This suggests that the Cholesterol feature has become more influential in the model's predictions over time.

**Overall Feature Analysis**

The analysis of the Cholesterol feature reveals that data drift has occurred between the reference and current datasets. The distribution of Cholesterol values has changed, with a more dispersed distribution in the current dataset. Furthermore, the Cholesterol feature has become more influential in the model's predictions, as indicated by the increased mean(|SHAP value|). These findings suggest that the model may require retraining or updating to accommodate the changes in the data distribution.

            ### BMI

            **Chronic Condition Prediction Data: BMI Feature Analysis**

**Feature Description**

* **Name:** BMI
* **Description:** Body Mass Index of the individual, ranging from 18.5 to 40.0.
* **Type:** numerical
* **Possible Values:** Ranging from 18.5 to 40.0.
* **Data Type:** float

**Tool Results**

### get_drift_report

The get_drift_report tool was used to analyze the BMI feature for data drift between the reference and current datasets. The results indicate that drift is detected in the BMI feature.

* **drift_detected:** True
* **drift_score:** 0.11257326919665277
* **stattest_name:** Kullback-Leibler divergence
* **stattest_threshold:** 0.1
* **current:** The current dataset's distribution information shows a shifted distribution with a higher frequency of BMI values between 24.43 and 30.45.
* **reference:** The reference dataset's distribution information shows a more uniform distribution of BMI values across the range.

### get_shap_values

The get_shap_values tool was used to calculate the mean(|SHAP value|) for the BMI feature in both the reference and current datasets. The results indicate that the average impact of the BMI feature on the model's predictions has increased in the current dataset.

* **reference:** Mean(|SHAP value|) = 0.14121425129867368, Rank position = 1
* **current:** Mean(|SHAP value|) = 0.16781096493974235, Rank position = 1

**Overall Feature Analysis**

The analysis of the BMI feature using both the get_drift_report and get_shap_values tools suggests that:

* Data drift is detected in the BMI feature, indicating a significant change in the distribution of BMI values between the reference and current datasets.
* The average impact of the BMI feature on the model's predictions has increased in the current dataset, suggesting that the feature has become more important for predicting chronic conditions.

These results highlight the need to monitor and adapt the model to the changing data distribution to maintain its performance and accuracy in predicting chronic conditions.

            ### Education Level

            **Feature Description**

* **Name:** Education Level
* **Description:** Highest education level attained, represented as 0 (no formal education) to 3 (graduate degree).
* **Type:** categorical
* **Possible Values:** {'0': 'No formal education', '1': 'High school diploma', '2': 'Bachelor degree', '3': 'Graduate degree'}
* **Data Type:** int

**Tool Results**

### get_drift_report

The get_drift_report tool was used to analyze the distribution of the Education Level feature between the reference and current datasets. The results indicate that drift was detected in this feature.

* **Drift Detected:** True
* **Drift Score:** 1.6716891527291513
* **Statistical Test:** Kullback-Leibler divergence
* **Statistical Test Threshold:** 0.1
* **Current Dataset Distribution:** {'small_distribution': {'x': [0, 1, 2, 3], 'y': [2, 44, 11, 143]}}
* **Reference Dataset Distribution:** {'small_distribution': {'x': [0, 1, 2, 3], 'y': [3, 197, 560, 40]}}

The drift score of 1.6716891527291513 indicates a significant difference in the distribution of the Education Level feature between the reference and current datasets. This suggests that the model's performance may be affected by this drift.

### get_shap_values

The get_shap_values tool was used to calculate the mean(|SHAP value|) for the Education Level feature to show its average impact on the model's predictions.

* **Reference Dataset:** {'value': 0.016434074575538762, 'position': 8}
* **Current Dataset:** {'value': 0.01641983309158441, 'position': 8}

The results indicate that the Education Level feature has a relatively low impact on the model's predictions, ranking 8th in both the reference and current datasets. The mean(|SHAP value|) values for both datasets are similar, suggesting that the feature's contribution to the model's predictions has not changed significantly.

**Overall Feature Analysis**

The Education Level feature exhibits drift between the reference and current datasets, which may affect the model's performance. However, the feature's contribution to the model's predictions remains relatively consistent, ranking 8th in both datasets. This suggests that the drift in the Education Level feature may not have a significant impact on the model's overall performance. Nevertheless, it is essential to monitor and address data drift to ensure the model's reliability and accuracy.

            ### Smoking Status

            **Chronic Condition Prediction Data: Smoking Status Feature Analysis**

**Feature Description**

* **Name:** Smoking Status
* **Description:** Current smoking status, represented as 0 (non-smoker), 1 (former smoker), or 2 (current smoker).
* **Type:** categorical
* **Possible Values:** {'0': 'Non-smoker', '1': 'Former smoker', '2': 'Current smoker'}
* **Data Type:** int

**Tool Results**

### get_drift_report

The get_drift_report tool was used to analyze the Smoking Status feature for data drift between the reference and current datasets. The results indicate that drift is detected for this feature.

* **Drift Detected:** True
* **Drift Score:** 0.20183373734484897
* **Statistical Test:** Kullback-Leibler divergence
* **Statistical Test Threshold:** 0.1
* **Current Distribution:** {'x': [0, 1, 2], 'y': [14, 186, 0]}
* **Reference Distribution:** {'x': [0, 1, 2], 'y': [44, 724, 32]}

The drift report suggests that the distribution of the Smoking Status feature has changed significantly between the reference and current datasets. This drift may lead to a decrease in model performance.

### get_shap_values

The get_shap_values tool was used to calculate the mean(|SHAP value|) for the Smoking Status feature to determine its average impact on the model's predictions.

* **Reference:** {'value': 0.006457749486556214, 'position': 10}
* **Current:** {'value': 0.004061665409373835, 'position': 10}

The SHAP values indicate that the Smoking Status feature has a relatively low impact on the model's predictions, ranking 10th in both the reference and current datasets. However, there is a slight decrease in the mean(|SHAP value|) from the reference to the current dataset, which may be attributed to the detected drift in the feature's distribution.

**Overall Feature Analysis**

The analysis of the Smoking Status feature using the get_drift_report and get_shap_values tools reveals that:

1. Data drift is detected in the Smoking Status feature between the reference and current datasets, which may lead to a decrease in model performance.
2. The feature has a relatively low impact on the model's predictions, ranking 10th in both datasets.
3. There is a slight decrease in the feature's mean(|SHAP value|) from the reference to the current dataset, which may be related to the detected drift.

These findings suggest that the Smoking Status feature may require additional attention and potential re-calibration to ensure that the model remains accurate and effective in predicting chronic conditions.

            ### Family History

            **Chronic Condition Prediction Data - Feature Analysis Report**

**Feature Description**

* **Name:** Family History
* **Description:** Family history of chronic condition, represented as 0 (no family history) or 1 (family history)
* **Type:** categorical
* **Possible Values:** {'0': 'No family history', '1': 'Family history'}
* **Data Type:** int

**Tool Results**

### get_drift_report

The get_drift_report tool was used to analyze the distribution of the Family History feature between the reference and current datasets. The results are as follows:

* **Drift Detected:** False
* **Drift Score:** 0.005370730255683034
* **Statistical Test:** Kullback-Leibler divergence
* **Statistical Test Threshold:** 0.1
* **Current Distribution:** {'small_distribution': {'x': [0, 1], 'y': [118, 82]}}
* **Reference Distribution:** {'small_distribution': {'x': [0, 1], 'y': [431, 369]}}

The drift score indicates that the distribution of the Family History feature has not changed significantly between the reference and current datasets. The statistical test used was the Kullback-Leibler divergence, which measures the difference between the two distributions. The threshold for detecting drift was set to 0.1. The current and reference distributions show that the proportion of individuals with and without a family history of chronic conditions has remained relatively consistent.

### get_shap_values

The get_shap_values tool was used to calculate the mean(|SHAP value|) for the Family History feature to evaluate its contribution to the model's predictions. The results are as follows:

* **Reference:** {'value': 0.01724435122228072, 'position': 7}
* **Current:** {'value': 0.018126868998631664, 'position': 7}

The SHAP values indicate that the Family History feature has a relatively low impact on the model's predictions, ranking 7th in terms of feature importance. The mean(|SHAP value|) has increased slightly from 0.0172 in the reference dataset to 0.0181 in the current dataset, suggesting a minor change in the feature's contribution to the model's predictions.

**Overall Feature Analysis**

The analysis of the Family History feature using the get_drift_report and get_shap_values tools suggests that:

* The distribution of the Family History feature has not changed significantly between the reference and current datasets.
* The feature has a relatively low impact on the model's predictions, ranking 7th in terms of feature importance.
* There is a minor change in the feature's contribution to the model's predictions between the reference and current datasets.

These findings indicate that the Family History feature is stable and has not undergone significant changes between the reference and current datasets. However, the slight increase in the feature's contribution to the model's predictions warrants further investigation to ensure that the model remains accurate and reliable.

            ### Income

            **Chronic Condition Prediction Data: Feature Analysis Report**

**Feature Description**

* **Name:** Income
* **Description:** Annual income of the individual in thousands of dollars, ranging from 20k to 100k.
* **Type:** Numerical
* **Possible Values:** Ranging from $20,000 to $100,000.
* **Data Type:** Float

**Tool Results**

### get_drift_report

The get_drift_report tool was used to generate a data drift report for the Income feature. The results indicate that drift was detected in the Income column, with a drift score of 0.91626108741935.

* **Drift Detected:** True
* **Drift Score:** 0.91626108741935
* **Statistical Test:** Kullback-Leibler divergence
* **Statistical Test Threshold:** 0.1
* **Current Distribution:**
	+ Small distribution: x = [20000.0, 28000.0, 36000.0, 44000.0, 52000.0, 60000.0, 68000.0, 76000.0, 84000.0, 92000.0, 100000.0]
	+ y = [7.5e-06, 3.75e-06, 4.3750000000000005e-06, 8.125e-06, 9.375e-06, 8.750000000000001e-06, 1.3749999999999999e-05, 1.25e-05, 1.1874999999999999e-05, 4.4999999999999996e-05]
* **Reference Distribution:**
	+ Small distribution: x = [20412.74114767384, 28371.467032906457, 36330.19291813907, 44288.91880337169, 52247.64468860431, 60206.370573836924, 68165.09645906955, 76123.82234430216, 84082.54822953478, 92041.27411476738, 100000.0]
	+ y = [4.7118094706064826e-07, 5.811231680414662e-06, 1.6020152200062035e-05, 2.9213218717760177e-05, 3.6280932923669935e-05, 2.1674323564789792e-05, 1.115128241376869e-05, 3.926507892172067e-06, 7.853015784344147e-07, 3.141206313737654e-07]

The drift report suggests that the distribution of the Income feature has changed significantly between the reference and current datasets, which may lead to a decrease in model performance.

### get_shap_values

The get_shap_values tool was used to calculate the mean(|SHAP value|) for the Income feature. The results indicate that the mean(|SHAP value|) for the Income feature has increased from 0.06594070343394506 in the reference dataset to 0.12549868716954315 in the current dataset, with a corresponding increase in rank position from 5 to 2.

* **Reference:**
	+ Mean(|SHAP value|): 0.06594070343394506
	+ Position: 5
* **Current:**
	+ Mean(|SHAP value|): 0.12549868716954315
	+ Position: 2

The increase in mean(|SHAP value|) and rank position suggests that the Income feature has become a more important contributor to the model's predictions in the current dataset.

**Overall Feature Analysis**

The results from the get_drift_report and get_shap_values tools suggest that the Income feature has undergone significant changes between the reference and current datasets. The drift detected in the Income column may lead to a decrease in model performance, while the increase in mean(|SHAP value|) and rank position indicates that the Income feature has become a more important contributor to the model's predictions. These findings suggest that the model may need to be re-trained or updated to accommodate the changes in the Income feature distribution and its increased importance in the model's predictions.
