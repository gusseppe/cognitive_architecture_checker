
        # Chronic Condition Prediction Data - Deep Insight Report

        ## Overview
        Overview report

        ## Details

        ### Label Insight
        The label in the "Chronic Condition Prediction Data" dataset is "ChronicCondition", which indicates the likelihood of an individual developing a chronic condition. The label is a categorical variable with two possible values: '0' representing no chronic condition and '1' representing chronic condition.

In essence, the label is a binary classification problem, where the goal is to predict whether an individual is likely to develop a chronic condition (label = 1) or not (label = 0) based on the provided attributes such as Age, BMI, Blood Pressure, Cholesterol, Physical Activity, Smoking Status, Diet Quality, Family History, Income, and Education Level.

There are no apparent issues with the label based on the available information. The label is clearly defined, and its possible values are well-documented. However, it is essential to note that the accuracy of the label depends on the quality and relevance of the provided attributes and the dataset's overall representativeness of the population being studied.


            ### Family History

            **Chronic Condition Prediction Data: Family History Feature Analysis**

**Feature Description**

* Name: Family History
* Description: Family history of chronic condition, represented as 0 (no family history) or 1 (family history).
* Type: categorical
* Possible Values: {'0': 'No family history', '1': 'Family history'}
* Data Type: int

**Tool Results**

### get_drift_report

The get_drift_report tool was used to analyze the distribution of the Family History feature between the reference and current datasets. The results are as follows:

* **General Drift Report Summary**
	+ Drift Share: 0.0
	+ Number of Columns: 1
	+ Number of Drifted Columns: 0
	+ Share of Drifted Columns: 0.0
	+ Dataset Drift: False
* **Detailed Drift Analysis per Column**
	+ Column Name: Family History
	+ Column Type: categorical
	+ Stat Test Name: Kullback-Leibler divergence
	+ Stat Test Threshold: 0.1
	+ Drift Score: 0.005370730255683034
	+ Drift Detected: False
	+ Current: {'small_distribution': {'x': [0, 1], 'y': [118, 82]}}
	+ Reference: {'small_distribution': {'x': [0, 1], 'y': [431, 369]}}

The results indicate that there is no significant drift detected in the Family History feature between the reference and current datasets.

### get_shap_values

The get_shap_values tool was used to calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions. The results are as follows:

* **Reference**
	+ Value: 0.01724435122228072
	+ Position: 7
* **Current**
	+ Value: 0.018126868998631664
	+ Position: 7

The results indicate that the mean(|SHAP value|) for the Family History feature is relatively stable between the reference and current datasets, with a slight increase in the current dataset. However, the position of the feature remains the same, indicating that its impact on the model's predictions is still significant.

**Overall Feature Analysis**

The analysis of the Family History feature using the get_drift_report and get_shap_values tools suggests that there is no significant drift detected in the feature between the reference and current datasets. The mean(|SHAP value|) for the feature is relatively stable, indicating that its impact on the model's predictions is still significant. However, the slight increase in the mean(|SHAP value|) in the current dataset may indicate a slight change in the feature's importance. Further analysis is needed to determine the impact of this change on the model's performance.

            ### Physical Activity

            **Chronic Condition Prediction Data: Physical Activity Feature Analysis**

**Feature Description**

* Name: Physical Activity
* Description: Number of days per week the individual engages in physical activity, ranging from 0 to 7.
* Type: numerical
* Possible Values: Ranging from 0 to 7 days per week.
* Data Type: int

**Tool Results**

### get_drift_report

The get_drift_report tool was used to analyze the distribution of the Physical Activity feature between the reference and current datasets. The results are as follows:

* **General Drift Report Summary**
	+ Drift Share: 0.8571428571428571
	+ Number of Columns: 1
	+ Number of Drifted Columns: 1
	+ Share of Drifted Columns: 1.0
	+ Dataset Drift: True
* **Detailed Drift Analysis per Column**
	+ Column Name: Physical Activity
	+ Column Type: num
	+ Stat Test Name: Kullback-Leibler divergence
	+ Stat Test Threshold: 0.1
	+ Drift Score: 7.48442577690803
	+ Drift Detected: True
	+ Current Distribution: {'small_distribution': {'x': [0.8292978352142784, 1.3040489151174648, 1.778799995020651, 2.2535510749238377, 2.7283021548270234, 3.20305323473021, 3.6778043146333967, 4.1525553945365825, 4.627306474439769, 5.102057554342956, 5.576808634246142], 'y': [0.10531834916562222, 0.10531834916562227, 0.22116853324780653, 0.2317003681643692, 0.38967789191280205, 0.3475505522465532, 0.358082387163116, 0.22116853324780653, 0.09478651424905994, 0.03159550474968671]}}
	+ Reference Distribution: {'small_distribution': {'x': [0.0, 0.7, 1.4, 2.0999999999999996, 2.8, 3.5, 4.199999999999999, 4.8999999999999995, 5.6, 6.3, 7.0], 'y': [0.014285714285714285, 0.0625, 0.22678571428571437, 0.0, 0.5089285714285713, 0.466071428571429, 0.0, 0.13749999999999996, 0.010714285714285711, 0.0017857142857142852]}}

The results indicate that the Physical Activity feature shows significant drift between the reference and current datasets, with a drift score of 7.48442577690803.

### get_shap_values

The get_shap_values tool was used to calculate the mean(|SHAP value|) for each feature to detect feature attribution drift. The results are as follows:

* **Feature Attribution Drift Analysis**
	+ Reference: {'value': 0.09817662833236682, 'position': 2}
	+ Current: {'value': 0.07730394004727022, 'position': 3}

The results indicate that the Physical Activity feature has a lower mean(|SHAP value|) in the current dataset compared to the reference dataset, indicating a potential change in the feature's contribution to the model's predictions.

**Overall Feature Analysis**

The analysis of the Physical Activity feature using the get_drift_report and get_shap_values tools suggests that there is significant drift between the reference and current datasets. The feature's distribution has changed, and its contribution to the model's predictions has also changed. This may impact the model's performance and accuracy. Further analysis and model retraining may be necessary to address these changes.

            ### Diet Quality

            **Chronic Condition Prediction Data: Diet Quality Feature Analysis**

**Feature Description**

* Name: Diet Quality
* Description: Quality of diet, represented as 0 (poor), 1 (average), or 2 (good).
* Type: categorical
* Possible Values: {'0': 'Poor', '1': 'Average', '2': 'Good'}
* Data Type: int

**Tool Results**

### get_drift_report

The `get_drift_report` tool was used to analyze the Diet Quality feature for data drift. The results are as follows:

* **General Drift Report Summary**
	+ Drift Share: 0.0
	+ Number of Columns: 1
	+ Number of Drifted Columns: 0
	+ Share of Drifted Columns: 0.0
	+ Dataset Drift: False
* **Detailed Drift Analysis per Column**
	+ Column Name: Diet Quality
	+ Column Type: categorical
	+ Stat Test Name: Kullback-Leibler divergence
	+ Stat Test Threshold: 0.1
	+ Drift Score: 0.0018915553873695345
	+ Drift Detected: False
	+ Current Distribution: {'small_distribution': {'x': [0, 1, 2], 'y': [10, 180, 10]}}
	+ Reference Distribution: {'small_distribution': {'x': [0, 1, 2], 'y': [30, 727, 43]}}

The results indicate that there is no data drift detected for the Diet Quality feature.

### get_shap_values

The `get_shap_values` tool was used to calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions. The results are as follows:

* **Reference**
	+ Value: 0.013835053054035294
	+ Position: 9
* **Current**
	+ Value: 0.011401517327642103
	+ Position: 9

The results indicate that the mean(|SHAP value|) for the Diet Quality feature has decreased slightly from the reference to the current dataset, but the position of the feature remains the same.

**Overall Feature Analysis**

The analysis of the Diet Quality feature using the `get_drift_report` and `get_shap_values` tools suggests that there is no data drift detected for this feature. However, the SHAP values indicate a slight decrease in the average impact of the feature on the model's predictions. This could be due to changes in the input data distribution, leading to changes in the order of feature contributions. Further analysis is recommended to understand the implications of these changes on the model's performance.

            ### Income

            **Chronic Condition Prediction Data: Income Feature Analysis Report**

**Feature Description**

* Name: Income
* Description: Annual income of the individual in thousands of dollars, ranging from $20,000 to $100,000.
* Type: Numerical
* Possible Values: Ranging from $20,000 to $100,000.
* Data Type: Float

**Tool Results**

### get_drift_report

The `get_drift_report` tool was used to analyze the drift in the Income feature between the reference and current datasets. The results are as follows:

* General Drift Report Summary:
	+ Drift Share: 0.91626108741935
	+ Number of Columns Analyzed: 1
	+ Number of Drifted Columns: 1
	+ Share of Drifted Columns: 100.0%
	+ Dataset Drift: True
* Detailed Drift Analysis per Column:
	+ Column Name: Income
	+ Column Type: Numerical
	+ Stat Test Name: Kullback-Leibler divergence
	+ Stat Test Threshold: 0.1
	+ Drift Score: 0.91626108741935
	+ Drift Detected: True
	+ Current Distribution: {'small_distribution': {'x': [20000.0, 28000.0, 36000.0, 44000.0, 52000.0, 60000.0, 68000.0, 76000.0, 84000.0, 92000.0, 100000.0], 'y': [7.5e-06, 3.75e-06, 4.3750000000000005e-06, 8.125e-06, 9.375e-06, 8.750000000000001e-06, 1.3749999999999999e-05, 1.25e-05, 1.1874999999999999e-05, 4.4999999999999996e-05]}}
	+ Reference Distribution: {'small_distribution': {'x': [20412.74114767384, 28371.467032906457, 36330.19291813907, 44288.91880337169, 52247.64468860431, 60206.370573836924, 68165.09645906955, 76123.82234430216, 84082.54822953478, 92041.27411476738, 100000.0], 'y': [4.7118094706064826e-07, 5.811231680414662e-06, 1.6020152200062035e-05, 2.9213218717760177e-05, 3.6280932923669935e-05, 2.1674323564789792e-05, 1.115128241376869e-05, 3.926507892172067e-06, 7.853015784344147e-07, 3.141206313737654e-07]}}

The results indicate that the Income feature has drifted significantly between the reference and current datasets, with a drift score of 0.91626108741935.

### get_shap_values

The `get_shap_values` tool was used to calculate the mean(|SHAP value|) for each feature to detect feature attribution drift. The results are as follows:

* Reference:
	+ Value: 0.06594070343394506
	+ Position: 5
* Current:
	+ Value: 0.12549868716954315
	+ Position: 2

The results indicate that the mean(|SHAP value|) for the Income feature has increased from 0.06594070343394506 in the reference dataset to 0.12549868716954315 in the current dataset, indicating a change in the feature's contribution to the model's predictions.

**Overall Feature Analysis**

The analysis of the Income feature using the `get_drift_report` and `get_shap_values` tools indicates that the feature has drifted significantly between the reference and current datasets. The drift score and mean(|SHAP value|) values suggest that the feature's distribution has changed, leading to changes in the model's predictions. This highlights the importance of monitoring feature drift and updating the model accordingly to maintain its performance.

            ### Education Level

            **Chronic Condition Prediction Data: Education Level Feature Analysis**

**Feature Description**

* Name: Education Level
* Description: Highest education level attained, represented as 0 (no formal education) to 3 (graduate degree).
* Type: categorical
* Possible Values: {'0': 'No formal education', '1': 'High school diploma', '2': 'Bachelor degree', '3': 'Graduate degree'}
* Data Type: int

**Tool Results**

### get_drift_report

The get_drift_report tool was used to analyze the Education Level feature for data drift. The results are as follows:

* **General Drift Report Summary**
	+ Drift Share: 0.25
	+ Number of Columns Analyzed: 1
	+ Number of Drifted Columns: 1
	+ Share of Drifted Columns: 100.0%
	+ Dataset Drift: True
* **Detailed Drift Analysis per Column**
	+ Column Name: Education Level
	+ Column Type: categorical
	+ Stat Test Name: Kullback-Leibler divergence
	+ Stat Test Threshold: 0.1
	+ Drift Score: 1.6716891527291513
	+ Drift Detected: True
	+ Current Distribution: {'small_distribution': {'x': [0, 1, 2, 3], 'y': [2, 44, 11, 143]}}
	+ Reference Distribution: {'small_distribution': {'x': [0, 1, 2, 3], 'y': [3, 197, 560, 40]}}

The results indicate that the Education Level feature has drifted significantly between the reference and current datasets, with a drift score of 1.6716891527291513. This suggests that the distribution of the Education Level feature has changed, which may impact the model's performance.

### get_shap_values

The get_shap_values tool was used to calculate the mean(|SHAP value|) for each feature to detect feature attribution drift. The results are as follows:

* **Reference SHAP Values**
	+ Value: 0.016434074575538762
	+ Position: 8
* **Current SHAP Values**
	+ Value: 0.01641983309158441
	+ Position: 8

The results indicate that the mean(|SHAP value|) for the Education Level feature has changed slightly between the reference and current datasets, with a decrease in value from 0.016434074575538762 to 0.01641983309158441. However, the position of the feature remains the same, indicating that the feature's contribution to the model's predictions has not changed significantly.

**Overall Feature Analysis**

The analysis of the Education Level feature using the get_drift_report and get_shap_values tools suggests that the feature has drifted significantly between the reference and current datasets. The drift score indicates a significant change in the distribution of the feature, which may impact the model's performance. However, the SHAP values indicate that the feature's contribution to the model's predictions has not changed significantly. Overall, the results suggest that the model may require retraining or updating to account for the changes in the Education Level feature.

            ### Blood Pressure

            **Chronic Condition Prediction Data: Blood Pressure Feature Analysis**

**Feature Description**

* Name: Blood Pressure
* Description: Systolic blood pressure of the individual in mmHg, ranging from 80 to 180.
* Type: numerical
* Possible Values: Ranging from 80 to 180 mmHg.
* Data Type: int

**Tool Results**

### get_drift_report

The get_drift_report tool was used to analyze the Blood Pressure feature for data drift. The results are as follows:

* **General Drift Report Summary**
	+ Drift Share: 0.3295963763250584
	+ Number of Columns Analyzed: 1
	+ Number of Drifted Columns: 1
	+ Share of Drifted Columns: 1.0
	+ Dataset Drift: True
* **Detailed Drift Analysis per Column**
	+ Column Name: Blood Pressure
	+ Column Type: numerical
	+ Stat Test Name: Kullback-Leibler divergence
	+ Stat Test Threshold: 0.1
	+ Drift Score: 0.3295963763250584
	+ Drift Detected: True
	+ Current Distribution: {'small_distribution': {'x': [77.42647761458834, 93.60024655055858, 109.77401548652881, 125.94778442249904, 142.12155335846927, 158.29532229443953, 174.46909123040976, 190.64286016638, 206.81662910235025, 222.99039803832045, 239.1641669742907], 'y': [0.0015457126968347085, 0.0021639977755685937, 0.008346848562907433, 0.009892561259742144, 0.014838841889613187, 0.01112913141720991, 0.008965133641641317, 0.003400567933036356, 0.0012365701574677701, 0.0003091425393669414]}}
	+ Reference Distribution: {'small_distribution': {'x': [80.0, 90.0, 100.0, 110.0, 120.0, 130.0, 140.0, 150.0, 160.0, 170.0, 180.0], 'y': [0.000125, 0.001875, 0.003, 0.00875, 0.018500000000000003, 0.025625, 0.020125, 0.014125, 0.006, 0.001875]}}

The results indicate that the Blood Pressure feature shows significant data drift, with a drift score of 0.3295963763250584. This suggests that the distribution of the Blood Pressure values in the current dataset has changed significantly compared to the reference dataset.

### get_shap_values

The get_shap_values tool was used to calculate the mean(|SHAP value|) for the Blood Pressure feature. The results are as follows:

* **SHAP Values**
	+ Reference: {'value': 0.07114418923716576, 'position': 4}
	+ Current: {'value': 0.053554968593565636, 'position': 4}

The results indicate that the mean(|SHAP value|) for the Blood Pressure feature is 0.07114418923716576 in the reference dataset and 0.053554968593565636 in the current dataset. The position of the feature based on its mean Mean(|SHAP value|) value is 4 in both datasets.

**Overall Feature Analysis**

The analysis of the Blood Pressure feature using the get_drift_report and get_shap_values tools suggests that there is significant data drift in the feature. The drift score indicates that the distribution of the Blood Pressure values in the current dataset has changed significantly compared to the reference dataset. The SHAP values also indicate that the feature's contribution to the model's predictions has changed. These changes may impact the model's performance and require retraining or updating the model to adapt to the new data distribution.

            ### BMI

            **Chronic Condition Prediction Data - BMI Feature Analysis Report**

**Feature Description**

* Name: BMI
* Description: Body Mass Index of the individual, ranging from 18.5 to 40.0.
* Type: numerical
* Possible Values: Ranging from 18.5 to 40.0.
* Data Type: float

**Tool Results**

### get_drift_report

The get_drift_report tool was used to analyze the drift in the BMI feature between the reference and current datasets. The results are as follows:

* General Drift Report Summary:
	+ Drift Share: 0.11257326919665277
	+ Number of Columns Analyzed: 1
	+ Number of Drifted Columns: 1
	+ Share of Drifted Columns: 100.0%
	+ Dataset Drift: True
* Detailed Drift Analysis per Column:
	+ Column Name: BMI
	+ Column Type: numerical
	+ Stat Test Name: Kullback-Leibler divergence
	+ Stat Test Threshold: 0.1
	+ Drift Score: 0.11257326919665277
	+ Drift Detected: True
	+ Current Distribution:
		- Small Distribution: {'x': [18.41029156979427, 21.42048565665614, 24.43067974351801, 27.44087383037988, 30.451067917241744, 33.46126200410362, 36.47145609096548, 39.48165017782735, 42.49184426468922, 45.50203835155109, 48.51223243841296], 'y': [0.004983067392720021, 0.029898404356320126, 0.08139010074776035, 0.08471214567624047, 0.06644089856960021, 0.03322044928480018, 0.023254314499360128, 0.004983067392720016, 0.001661022464240005, 0.0016610224642400093]}
	+ Reference Distribution:
		- Small Distribution: {'x': [18.5, 20.61, 22.72, 24.830000000000002, 26.94, 29.05, 31.160000000000004, 33.27, 35.38, 37.49, 39.6], 'y': [0.0023696682464454982, 0.01184834123222749, 0.04798578199052126, 0.09063981042654032, 0.1167061611374408, 0.11670616113744059, 0.05627962085308059, 0.02251184834123223, 0.00770142180094787, 0.0011848341232227491]}

The results indicate that the BMI feature has drifted significantly between the reference and current datasets, with a drift score of 0.11257326919665277.

### get_shap_values

The get_shap_values tool was used to calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions. The results are as follows:

* Reference:
	+ Value: 0.14121425129867368
	+ Position: 1
* Current:
	+ Value: 0.16781096493974235
	+ Position: 1

The results indicate that the mean(|SHAP value|) for the BMI feature has increased from 0.14121425129867368 in the reference dataset to 0.16781096493974235 in the current dataset, indicating a change in the feature's contribution to the model's predictions.

**Overall Feature Analysis**

The analysis of the BMI feature using the get_drift_report and get_shap_values tools indicates that the feature has drifted significantly between the reference and current datasets. The drift score and mean(|SHAP value|) values suggest that the feature's distribution has changed, leading to changes in the model's predictions. This highlights the importance of monitoring feature drift and updating the model accordingly to maintain its performance.

            ### Age

            **Chronic Condition Prediction Data Analysis Report**

**Feature Description**

* **Name:** Age
* **Description:** Age of the individual in years, ranging from 18 to 90.
* **Type:** Numerical
* **Possible Values:** Ranging from 18 to 90 years.
* **Data Type:** int

**Tool Results**

### get_drift_report

The get_drift_report tool was used to analyze the distribution of the Age feature between the reference and current datasets. The results are as follows:

* **General Drift Report Summary:**
	+ Drift Share: 0.03778629771302727
	+ Number of Columns Analyzed: 1
	+ Number of Drifted Columns: 0
	+ Share of Drifted Columns: 0.0
	+ Dataset Drift: False
* **Detailed Drift Analysis per Column:**
	+ Column Name: Age
	+ Column Type: Numerical
	+ Stat Test Name: Kullback-Leibler divergence
	+ Stat Test Threshold: 0.1
	+ Drift Score: 0.03778629771302727
	+ Drift Detected: False
	+ Current Distribution: {'small_distribution': {'x': [31.0, 36.5, 42.0, 47.5, 53.0, 58.5, 64.0, 69.5, 75.0, 80.5, 86.0], 'y': [0.002727272727272727, 0.0036363636363636364, 0.013636363636363636, 0.016363636363636365, 0.045454545454545456, 0.035454545454545454, 0.03363636363636364, 0.02090909090909091, 0.005454545454545454, 0.004545454545454545]}}
	+ Reference Distribution: {'small_distribution': {'x': [18.0, 25.2, 32.4, 39.6, 46.8, 54.0, 61.2, 68.4, 75.6, 82.8, 90.0], 'y': [0.00017361111111111112, 0.0005208333333333333, 0.00329861111111111, 0.010416666666666671, 0.02690972222222221, 0.0392361111111111, 0.03229166666666665, 0.016840277777777805, 0.007291666666666664, 0.0019097222222222215]}}

The results indicate that there is no significant drift detected in the Age feature between the reference and current datasets.

### get_shap_values

The get_shap_values tool was used to calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions. The results are as follows:

* **Reference SHAP Values:**
	+ Value: 0.08906002648096621
	+ Position: 3
* **Current SHAP Values:**
	+ Value: 0.050937679805919664
	+ Position: 5

The results indicate that the mean(|SHAP value|) for the Age feature has decreased from 0.08906002648096621 in the reference dataset to 0.050937679805919664 in the current dataset, indicating a potential feature attribution drift.

**Overall Feature Analysis**

Based on the results from the get_drift_report and get_shap_values tools, it can be concluded that:

* The Age feature does not show significant drift between the reference and current datasets.
* However, the mean(|SHAP value|) for the Age feature has decreased in the current dataset, indicating a potential feature attribution drift.

These findings suggest that the model's predictions may be affected by changes in the input data distribution, particularly with respect to the Age feature. Further analysis and model retraining may be necessary to mitigate the impact of this drift.

            ### Smoking Status

            **Chronic Condition Prediction Data: Smoking Status Feature Analysis**

**Feature Description**

* Name: Smoking Status
* Description: Current smoking status, represented as 0 (non-smoker), 1 (former smoker), or 2 (current smoker).
* Type: categorical
* Possible Values: {'0': 'Non-smoker', '1': 'Former smoker', '2': 'Current smoker'}
* Data Type: int

**Tool Results**

### get_drift_report

The get_drift_report tool was used to analyze the Smoking Status feature for data drift. The results are as follows:

* **General Drift Report Summary**
	+ Drift Share: 0.20183373734484897
	+ Number of Columns: 1
	+ Number of Drifted Columns: 1
	+ Share of Drifted Columns: 100.0%
	+ Dataset Drift: True
* **Detailed Drift Analysis per Column**
	+ Column Name: Smoking Status
	+ Column Type: categorical
	+ Stat Test Name: Kullback-Leibler divergence
	+ Stat Test Threshold: 0.1
	+ Drift Score: 0.20183373734484897
	+ Drift Detected: True
	+ Current Distribution: {'small_distribution': {'x': [0, 1, 2], 'y': [14, 186, 0]}}
	+ Reference Distribution: {'small_distribution': {'x': [0, 1, 2], 'y': [44, 724, 32]}}

The results indicate that the Smoking Status feature has drifted significantly between the reference and current datasets, with a drift score of 0.20183373734484897. This suggests that the distribution of the data has changed significantly, which may lead to a decrease in model performance.

### get_shap_values

The get_shap_values tool was used to calculate the mean(|SHAP value|) for each feature to detect feature attribution drift. The results are as follows:

* **Reference SHAP Values**
	+ Value: 0.006457749486556214
	+ Position: 10
* **Current SHAP Values**
	+ Value: 0.004061665409373835
	+ Position: 10

The results indicate that the mean(|SHAP value|) for the Smoking Status feature has decreased from 0.006457749486556214 in the reference dataset to 0.004061665409373835 in the current dataset, while maintaining the same position (10). This suggests that the feature attribution drift may be occurring, which could impact the model's predictions.

**Overall Feature Analysis**

The analysis of the Smoking Status feature using the get_drift_report and get_shap_values tools suggests that the feature has drifted significantly between the reference and current datasets. The drift score indicates a significant change in the distribution of the data, which may lead to a decrease in model performance. Additionally, the feature attribution drift detected by get_shap_values suggests that the feature's contribution to the model's predictions may be changing. These findings highlight the importance of monitoring feature drift and updating the model accordingly to maintain its performance.

            ### Cholesterol

            **Chronic Condition Prediction Data: Cholesterol Feature Analysis**

**Feature Description**

* Name: Cholesterol
* Description: Total cholesterol level of the individual in mg/dL, ranging from 150 to 300.
* Type: numerical
* Possible Values: Ranging from 150 to 300 mg/dL.
* Data Type: int

**Tool Results**

### get_drift_report

The get_drift_report tool was used to analyze the distribution of the Cholesterol feature between the reference and current datasets. The results are as follows:

* **General Drift Report Summary**
	+ Drift Share: 0.23450676168929094
	+ Number of Columns: 1
	+ Number of Drifted Columns: 1
	+ Share of Drifted Columns: 100.0%
	+ Dataset Drift: True
* **Detailed Drift Analysis per Column**
	+ Column Name: Cholesterol
	+ Column Type: num
	+ Stat Test Name: Kullback-Leibler divergence
	+ Stat Test Threshold: 0.1
	+ Drift Score: 0.23450676168929094
	+ Drift Detected: True
	+ Current Distribution: {'small_distribution': {'x': [153.16247399274783, 172.59032864659406, 192.01818330044026, 211.44603795428648, 230.87389260813268, 250.3017472619789, 269.7296019158251, 289.15745656967135, 308.5853112235176, 328.0131658773638, 347.44102053121], 'y': [0.001544174616009944, 0.006176698464039786, 0.006691423336043091, 0.011838672056076256, 0.01158130962007458, 0.008492960388054692, 0.0033457116680215455, 0.0005147248720033148, 0.0005147248720033148, 0.0007720873080049744]}}
	+ Reference Distribution: {'small_distribution': {'x': [150.0, 165.0, 180.0, 195.0, 210.0, 225.0, 240.0, 255.0, 270.0, 285.0, 300.0], 'y': [0.00025, 0.002, 0.005583333333333333, 0.01375, 0.017, 0.018000000000000002, 0.007666666666666667, 0.0019166666666666668, 0.00041666666666666664, 8.333333333333333e-05]}}

The results indicate that the Cholesterol feature shows significant drift between the reference and current datasets, with a drift score of 0.2345. This suggests that the distribution of the Cholesterol feature has changed significantly, which may impact the performance of the model.

### get_shap_values

The get_shap_values tool was used to calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions. The results are as follows:

* **Reference SHAP Values**
	+ Value: 0.03926329553692529
	+ Position: 6
* **Current SHAP Values**
	+ Value: 0.04945714499086426
	+ Position: 6

The results indicate that the Cholesterol feature has a relatively high mean(|SHAP value|) value in both the reference and current datasets, indicating that it has a significant impact on the model's predictions. However, the position of the feature has changed from 6 to 6, suggesting that the feature attribution drift may not be significant.

**Overall Feature Analysis**

The analysis of the Cholesterol feature using the get_drift_report and get_shap_values tools suggests that the feature shows significant drift between the reference and current datasets. The drift score indicates that the distribution of the Cholesterol feature has changed significantly, which may impact the performance of the model. However, the feature attribution drift analysis suggests that the feature's impact on the model's predictions has not changed significantly. Therefore, it is recommended to retrain the model using the current dataset to account for the changes in the Cholesterol feature distribution.
