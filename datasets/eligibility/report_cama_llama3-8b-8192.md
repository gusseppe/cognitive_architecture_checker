
        # Eligibility Simulation Data - Deep Insight Report

        ## Overview
        Overview report

        ## Details

        ### Label Insight
        The label in the "Eligibility Simulation Data" dataset is "ProgramEligibility", which indicates whether an individual is eligible (1) or not eligible (0) for a specific program. This categorical label variable serves as the target variable for predictions, meaning that the goal of the analysis is to predict the eligibility status of individuals based on their attributes.

The possible values for the "ProgramEligibility" label are '0' for not eligible and '1' for eligible, which are represented as integers. This suggests that the label is a binary classification problem, where the model will learn to distinguish between individuals who are eligible and those who are not eligible for the program.

Based on the available information, there do not appear to be any obvious problems or issues with the label. The label is clearly defined, and the possible values are well-documented. However, it would be beneficial to know more about the program and the criteria used to determine eligibility, as this could provide additional context and insights for the analysis.


            ### Education Level

            **Feature Description**

**Name:** Education Level

**Description:** Reflects the highest education level attained, on a scale from 0 (no formal education) to 3 (graduate degree), suggesting educational attainment.

**Type:** categorical

**Possible Values:** {'0': 'No formal education', '1': 'High school diploma', '2': 'Bachelor degree', '3': 'Graduate degree'}

**Data Type:** int

**Tool Results**

**get_drift_report**

The get_drift_report tool was used to analyze the Education Level feature for data drift. The results are as follows:

* **General Drift Report Summary:**
	+ Drift Share: 0.1851521399815421
	+ Number of Columns Analyzed: 1
	+ Number of Drifted Columns: 1
	+ Share of Drifted Columns: 100.0%
	+ Dataset Drift: True
* **Detailed Drift Analysis per Column:**
	+ Column Name: Education Level
	+ Column Type: categorical
	+ Stat Test Name: Kullback-Leibler divergence
	+ Stat Test Threshold: 0.1
	+ Drift Score: 0.1851521399815421
	+ Drift Detected: True
	+ Current Distribution: {'small_distribution': {'x': [0, 1, 2, 3], 'y': [1, 49, 150, 0]}}
	+ Reference Distribution: {'small_distribution': {'x': [0, 1, 2, 3], 'y': [12, 302, 464, 22]}}

The results indicate that the Education Level feature has drifted significantly between the reference and current datasets, with a drift score of 0.1851521399815421. This suggests that the distribution of the Education Level feature has changed significantly, which may impact the model's performance.

**get_shap_values**

The get_shap_values tool was used to calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions. The results are as follows:

* **Reference SHAP Values:**
	+ Value: 0.11009905271521023
	+ Position: 3
* **Current SHAP Values:**
	+ Value: 0.06845397004237376
	+ Position: 4

The results indicate that the Education Level feature has a lower mean(|SHAP value|) in the current dataset compared to the reference dataset, indicating a potential decrease in the feature's importance. This may be due to changes in the input data distribution, leading to changes in the order of feature contributions.

**Overall Feature Analysis**

The Education Level feature has been analyzed using the get_drift_report and get_shap_values tools. The results indicate that the feature has drifted significantly between the reference and current datasets, with a drift score of 0.1851521399815421. Additionally, the feature's importance has decreased in the current dataset, as indicated by the lower mean(|SHAP value|) value. These findings suggest that the Education Level feature may require retraining or re-evaluation to ensure optimal performance in the current dataset.

            ### Employment Status

            **Feature Analysis Report: Employment Status**

**Feature Description**

* Name: Employment Status
* Description: Current employment status, represented as 0 (unemployed), 1 (part-time), or 2 (full-time), indicating job market participation.
* Type: categorical
* Possible Values: {'0': 'Unemployed', '1': 'Part-time employment', '2': 'Full-time employment'}
* Data Type: int

**Tool Results**

### get_drift_report

The get_drift_report tool was used to analyze the Employment Status feature for data drift. The results are as follows:

* **General Drift Report Summary**
	+ Drift Share: 0.7046963105072126
	+ Number of Columns Analyzed: 1
	+ Number of Drifted Columns: 1
	+ Share of Drifted Columns: 100.0%
	+ Dataset Drift: True
* **Detailed Drift Analysis per Column**
	+ Column Name: Employment Status
	+ Column Type: categorical
	+ Stat Test Name: Kullback-Leibler divergence
	+ Stat Test Threshold: 0.1
	+ Drift Score: 0.7046963105072126
	+ Drift Detected: True
	+ Current Distribution: {'small_distribution': {'x': [0, 1, 2], 'y': [8, 192, 0]}}
	+ Reference Distribution: {'small_distribution': {'x': [0, 1, 2], 'y': [19, 689, 92]}}

The results indicate that the Employment Status feature has shown significant data drift, with a drift score of 0.7046963105072126. This suggests that the distribution of the Employment Status feature has changed significantly between the reference and current datasets, which may lead to a decrease in model performance.

### get_shap_values

The get_shap_values tool was used to calculate the mean(|SHAP value|) for each feature to detect feature attribution drift. The results are as follows:

* **SHAP Values**
	+ Reference: {'value': 0.018275746416542244, 'position': 5}
	+ Current: {'value': 0.010987271996598626, 'position': 5}

The results indicate that the mean(|SHAP value|) for the Employment Status feature has decreased from 0.018275746416542244 in the reference dataset to 0.010987271996598626 in the current dataset. This suggests that the feature attribution drift may have occurred, which may impact the model's predictions.

**Overall Feature Analysis**

The Employment Status feature has shown significant data drift, with a drift score of 0.7046963105072126. Additionally, the feature attribution drift has been detected, with a decrease in the mean(|SHAP value|) from 0.018275746416542244 to 0.010987271996598626. These results suggest that the Employment Status feature may require retraining or re-evaluation to maintain its effectiveness in the current dataset.

            ### Marital Status

            **Feature Description**

**Name:** Marital Status

**Description:** Current marital status, categorized into Single, Married, or Divorced, to provide demographic insights.

**Type:** categorical

**Possible Values:** {'0': 'Single', '1': 'Married', '2': 'Divorced'}

**Data Type:** int

**Tool Results**

**get_drift_report**

The get_drift_report tool was used to analyze the Marital Status feature for data drift. The results are as follows:

* **General Drift Report Summary:**
	+ Drift Share: 0.8026944167960824
	+ Number of Columns Analyzed: 1
	+ Number of Drifted Columns: 1
	+ Share of Drifted Columns: 100.0%
	+ Dataset Drift: True
* **Detailed Drift Analysis per Column:**
	+ Column Name: Marital Status
	+ Column Type: categorical
	+ Stat Test Name: Kullback-Leibler divergence
	+ Stat Test Threshold: 0.1
	+ Drift Score: 0.8026944167960824
	+ Drift Detected: True
	+ Current Distribution: {'small_distribution': {'x': [0, 1, 2], 'y': [83, 53, 64]}}
	+ Reference Distribution: {'small_distribution': {'x': [0, 1, 2], 'y': [93, 688, 19]}}

The results indicate that the Marital Status feature has drifted significantly between the reference and current datasets, with a drift score of 0.8026944167960824. This suggests that the distribution of the Marital Status feature has changed significantly, which may impact the model's performance.

**get_shap_values**

The get_shap_values tool was used to calculate the mean(|SHAP value|) for the Marital Status feature. The results are as follows:

* **Reference:**
	+ Value: 0.05409217592159332
	+ Position: 4
* **Current:**
	+ Value: 0.09958768447538655
	+ Position: 3

The results indicate that the mean(|SHAP value|) for the Marital Status feature has increased from 0.05409217592159332 in the reference dataset to 0.09958768447538655 in the current dataset. This suggests that the Marital Status feature has a greater impact on the model's predictions in the current dataset compared to the reference dataset.

**Overall Feature Analysis**

The Marital Status feature has been analyzed using the get_drift_report and get_shap_values tools. The results indicate that the feature has drifted significantly between the reference and current datasets, with a drift score of 0.8026944167960824. Additionally, the mean(|SHAP value|) for the feature has increased in the current dataset compared to the reference dataset. These results suggest that the Marital Status feature may require retraining or re-tuning to maintain optimal performance in the current dataset.

            ### Income

            **Feature Description**

* Name: Income
* Description: Annual income of the individual in thousands of dollars, indicating economic status, ranging from $20,000 to $70,000.
* Type: numerical
* Possible Values: Ranging from $20,000 to $70,000.
* Data Type: float

**Tool Results**

### get_drift_report

The get_drift_report tool was used to analyze the drift in the Income feature between the reference and current datasets. The results are as follows:

* General Drift Report Summary:
	+ Drift Share: 0.7978008461594442
	+ Number of Columns: 1
	+ Number of Drifted Columns: 1
	+ Share of Drifted Columns: 1.0
	+ Dataset Drift: True
* Detailed Drift Analysis per Column:
	+ Column Name: Income
	+ Column Type: num
	+ Stat Test Name: Kullback-Leibler divergence
	+ Stat Test Threshold: 0.1
	+ Drift Score: 0.7978008461594442
	+ Drift Detected: True
	+ Current Distribution: {'small_distribution': {'x': [-3508.2364074368093, 10667.570547951202, 24843.377503339212, 39019.18445872722, 53194.99141411523, 67370.79836950325, 81546.60532489125, 95722.41228027927, 109898.21923566727, 124074.02619105528, 138249.8331464433], 'y': [1.4108544270489167e-06, 4.5852768879089795e-06, 8.465126562293502e-06, 1.6577539517824768e-05, 1.8693821158398144e-05, 1.022869459610465e-05, 5.643417708195664e-06, 2.468995247335605e-06, 1.7635680338111466e-06, 7.05427213524458e-07]}}
	+ Reference Distribution: {'small_distribution': {'x': [21687.0, 26395.8, 31104.6, 35813.4, 40522.2, 45231.0, 49939.8, 54648.6, 59357.4, 64066.200000000004, 68775.0], 'y': [2.389143730886851e-06, 1.964407067618077e-05, 5.707398912674138e-05, 6.211773700305817e-05, 3.4775314305130796e-05, 1.672400611620794e-05, 6.901970778117574e-06, 9.025654094461428e-06, 2.654604145429832e-06, 1.0618416581719344e-06]}}

### get_shap_values

The get_shap_values tool was used to calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions. The results are as follows:

* Reference:
	+ Value: 0.16902756259348087
	+ Position: 1
* Current:
	+ Value: 0.24910130910592299
	+ Position: 1

**Overall Feature Analysis**

Based on the results from the get_drift_report and get_shap_values tools, it can be concluded that:

* The Income feature shows significant drift between the reference and current datasets, with a drift score of 0.7978008461594442.
* The mean(|SHAP value|) for the Income feature has increased from 0.16902756259348087 in the reference dataset to 0.24910130910592299 in the current dataset, indicating a change in the feature's contribution to the model's predictions.
* The feature's position in the ranking has also changed, with the Income feature now ranking first in the current dataset compared to ranking second in the reference dataset.

Overall, these results suggest that the Income feature has undergone significant changes between the reference and current datasets, which may impact the model's performance and require retraining or re-evaluation.

            ### Age

            **Feature Analysis Report: Age**

**Feature Description**

* Name: Age
* Description: Age of the individual in years, ranging from 18 to 65.
* Type: numerical
* Possible Values: Ranging from 18 to 65 years.
* Data Type: int

**Tool Results**

### get_drift_report

The get_drift_report tool was used to analyze the distribution of the Age feature between the reference and current datasets. The results are as follows:

* General Drift Report Summary:
	+ Drift Share: 0.06325575780482698
	+ Number of Columns Analyzed: 1
	+ Number of Drifted Columns: 0
	+ Share of Drifted Columns: 0.0
	+ Dataset Drift: False
* Detailed Drift Analysis per Column:
	+ Column Name: Age
	+ Column Type: numerical
	+ Stat Test Name: Kullback-Leibler divergence
	+ Stat Test Threshold: 0.1
	+ Drift Score: 0.06325575780482698
	+ Drift Detected: False
	+ Current Distribution: {'small_distribution': {'x': [24.0, 27.4, 30.8, 34.2, 37.6, 41.0, 44.4, 47.8, 51.2, 54.599999999999994, 58.0], 'y': [0.010294117647058827, 0.0264705882352941, 0.03970588235294115, 0.038235294117647076, 0.039705882352941195, 0.06911764705882356, 0.027941176470588247, 0.02499999999999996, 0.01029411764705885, 0.007352941176470575]}}
	+ Reference Distribution: {'small_distribution': {'x': [18.0, 22.7, 27.4, 32.1, 36.8, 41.5, 46.2, 50.9, 55.6, 60.300000000000004, 65.0], 'y': [0.0007978723404255321, 0.0053191489361702135, 0.02313829787234041, 0.03085106382978726, 0.05265957446808508, 0.04893617021276593, 0.025265957446808533, 0.018351063829787222, 0.005851063829787231, 0.0015957446808510653]}}

The results indicate that there is no significant drift detected in the Age feature between the reference and current datasets.

### get_shap_values

The get_shap_values tool was used to calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions. The results are as follows:

* Reference:
	+ Value: 0.1675692700443467
	+ Position: 2
* Current:
	+ Value: 0.10098040394127042
	+ Position: 2

The results indicate that the mean(|SHAP value|) for the Age feature has decreased from 0.1675692700443467 in the reference dataset to 0.10098040394127042 in the current dataset, indicating a potential feature attribution drift.

**Overall Feature Analysis**

The analysis of the Age feature using the get_drift_report and get_shap_values tools suggests that there is no significant drift detected in the distribution of the Age feature between the reference and current datasets. However, the mean(|SHAP value|) for the Age feature has decreased, indicating a potential feature attribution drift. This may indicate that the input data distribution has changed, leading to changes in the order of feature contributions.
