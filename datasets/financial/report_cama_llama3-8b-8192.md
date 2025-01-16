
        # Loan Default Prediction Data - Deep Insight Report

        ## Overview
        Overview report

        ## Details

        ### Label Insight
        The label in the "Loan Default Prediction Data" dataset is "Loan Default", which indicates the likelihood of a borrower defaulting on a loan. The label is a categorical variable with two possible values: '0' representing no default and '1' representing default.

In other words, the label is a binary classification problem, where the goal is to predict whether a borrower is likely to default on a loan (label = 1) or not (label = 0). This label serves as the target variable for the machine learning model, which aims to learn patterns and relationships between the input features (such as Age, Income, Credit Score, etc.) and the likelihood of loan default.

Based on the available information, there do not appear to be any obvious problems or issues with the label. The label is clearly defined, and the possible values are well-documented. However, it is always important to review the data and label quality to ensure that they are accurate and consistent, as this can impact the performance and reliability of the machine learning model.


            ### Home Ownership

            **Loan Default Prediction Data: Home Ownership Feature Analysis**

**Feature Description**

* Name: Home Ownership
* Description: Home ownership status, represented as 0 (Rent), 1 (Own), or 2 (Mortgage).
* Type: categorical
* Possible Values: {'0': 'Rent', '1': 'Own', '2': 'Mortgage'}
* Data Type: int

**Tool Results**

### get_drift_report

The get_drift_report tool was used to analyze the Home Ownership feature for data drift. The results are as follows:

* **General Drift Report Summary**
	+ Drift Share: 0.18557356469873026
	+ Number of Columns Analyzed: 1
	+ Number of Drifted Columns: 1
	+ Share of Drifted Columns: 100.0%
	+ Dataset Drift: True
* **Detailed Drift Analysis per Column**
	+ Column Name: Home Ownership
	+ Column Type: categorical
	+ Stat Test Name: Kullback-Leibler divergence
	+ Stat Test Threshold: 0.1
	+ Drift Score: 0.18557356469873026
	+ Drift Detected: True
	+ Current Distribution: {'small_distribution': {'x': [0, 1, 2], 'y': [16, 184, 0]}}
	+ Reference Distribution: {'small_distribution': {'x': [0, 1, 2], 'y': [62, 708, 30]}}

The results indicate that the Home Ownership feature has shown significant data drift, with a drift score of 0.18557356469873026. This suggests that the distribution of the Home Ownership feature has changed significantly between the reference and current datasets, which may lead to a decrease in model performance.

### get_shap_values

The get_shap_values tool was used to calculate the mean(|SHAP value|) for each feature to detect feature attribution drift. The results are as follows:

* **Reference SHAP Values**
	+ Value: 0.003640297286226866
	+ Position: 10
* **Current SHAP Values**
	+ Value: 0.003270709366873879
	+ Position: 10

The results indicate that the mean(|SHAP value|) for the Home Ownership feature has decreased slightly between the reference and current datasets, with a position rank of 10 in both datasets. This suggests that the feature attribution drift may be present, but the impact is relatively small.

**Overall Feature Analysis**

The analysis of the Home Ownership feature using the get_drift_report and get_shap_values tools suggests that the feature has shown significant data drift, which may lead to a decrease in model performance. Additionally, the feature attribution drift may be present, but the impact is relatively small. To mitigate these issues, it is recommended to retrain the model using the current dataset and monitor the feature's performance over time.

            ### Age

            **Loan Default Prediction Data: Feature Analysis Report**

**Feature Description**

* **Name:** Age
* **Description:** Age of the borrower in years, ranging from 18 to 70.
* **Type:** Numerical
* **Possible Values:** Ranging from 18 to 70 years.
* **Data Type:** int

**Tool Results**

### get_drift_report

The get_drift_report tool was used to analyze the distribution of the Age feature between the reference and current datasets. The results are as follows:

* **General Drift Report Summary:**
	+ Drift Share: 0.03883719590118
	+ Number of Columns Analyzed: 1
	+ Number of Drifted Columns: 0
	+ Share of Drifted Columns: 0.0
	+ Dataset Drift: False
* **Detailed Drift Analysis per Column:**
	+ Column Name: Age
	+ Column Type: num
	+ Stat Test Name: Kullback-Leibler divergence
	+ Stat Test Threshold: 0.1
	+ Drift Score: 0.03883719590118
	+ Drift Detected: False
	+ Current Distribution: {'small_distribution': {'x': [27.0, 31.0, 35.0, 39.0, 43.0, 47.0, 51.0, 55.0, 59.0, 63.0, 67.0], 'y': [0.0025, 0.00375, 0.01625, 0.0175, 0.06125, 0.0575, 0.04125, 0.0325, 0.01125, 0.00625]}}
	+ Reference Distribution: {'small_distribution': {'x': [18.0, 23.2, 28.4, 33.6, 38.8, 44.0, 49.2, 54.4, 59.6, 64.80000000000001, 70.0], 'y': [0.00024038461538461543, 0.0007211538461538462, 0.00456730769230769, 0.01418269230769232, 0.036298076923076905, 0.05697115384615382, 0.0432692307692308, 0.023076923076923064, 0.010336538461538442, 0.002644230769230775]}}

The results indicate that there is no significant drift detected in the Age feature between the reference and current datasets.

### get_shap_values

The get_shap_values tool was used to calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions. The results are as follows:

* **Reference SHAP Values:**
	+ Value: 0.08155174483476563
	+ Position: 3
* **Current SHAP Values:**
	+ Value: 0.05350981388279517
	+ Position: 5

The results indicate that the mean(|SHAP value|) for the Age feature has decreased from 0.08155174483476563 in the reference dataset to 0.05350981388279517 in the current dataset, indicating a potential change in the feature attribution drift.

**Overall Feature Analysis**

Based on the results from the get_drift_report and get_shap_values tools, it can be concluded that:

* The Age feature does not show significant drift between the reference and current datasets.
* However, the mean(|SHAP value|) for the Age feature has decreased in the current dataset, indicating a potential change in the feature attribution drift.

These findings suggest that the model's predictions may be affected by changes in the input data distribution, and further analysis is recommended to understand the impact of these changes on the model's performance.

            ### Income

            **Loan Default Prediction Data: Income Feature Analysis Report**

**Feature Description**

* Name: Income
* Description: Annual income of the borrower in dollars, ranging from $20,000 to $150,000.
* Type: Numerical
* Possible Values: Ranging from $20,000 to $150,000.
* Data Type: Float

**Tool Results**

### get_drift_report

The get_drift_report tool was used to analyze the drift between the reference and current datasets. The results are as follows:

* **General Drift Report Summary**
	+ Drift Share: 0.130772018665271
	+ Number of Columns: 1
	+ Number of Drifted Columns: 1
	+ Share of Drifted Columns: 100.0%
	+ Dataset Drift: True
* **Detailed Drift Analysis per Column**
	+ Column Name: Income
	+ Column Type: Numerical
	+ Stat Test Name: Kullback-Leibler divergence
	+ Stat Test Threshold: 0.1
	+ Drift Score: 0.130772018665271
	+ Drift Detected: True
	+ Current Distribution: {'small_distribution': {'x': [25501.45540738348, 37951.30986664513, 50401.164325906786, 62851.01878516844, 75300.87324443008, 87750.72770369175, 100200.58216295339, 112650.43662221506, 125100.2910814767, 137550.14554073836, 150000.0], 'y': [8.03222241088998e-07, 6.024166808167485e-06, 6.024166808167485e-06, 1.8072500424502464e-05, 1.405638921905745e-05, 1.0441889134156987e-05, 9.638666893067965e-06, 6.8273890492564905e-06, 4.016111205444986e-06, 4.417722325989494e-06]}}
	+ Reference Distribution: {'small_distribution': {'x': [20000.0, 32745.298315057298, 45490.596630114596, 58235.894945171895, 70981.19326022919, 83726.49157528649, 96471.78989034379, 109217.08820540109, 121962.38652045839, 134707.68483551568, 147452.98315057298], 'y': [3.923015277008463e-07, 1.9615076385042317e-06, 7.944105935942136e-06, 1.4809382670706947e-05, 1.941892562119189e-05, 1.941892562119189e-05, 9.41523666482031e-06, 3.7268645131580396e-06, 1.1769045831025388e-06, 1.9615076385042315e-07]}}

### get_shap_values

The get_shap_values tool was used to calculate the mean(|SHAP value|) for each feature. The results are as follows:

* **Reference SHAP Values**
	+ Value: 0.13983600738410132
	+ Position: 1
* **Current SHAP Values**
	+ Value: 0.1676025103420878
	+ Position: 1

**Overall Feature Analysis**

Based on the results from the get_drift_report and get_shap_values tools, it can be concluded that:

* The Income feature shows significant drift between the reference and current datasets, with a drift score of 0.130772018665271.
* The mean(|SHAP value|) for the Income feature has increased from 0.13983600738410132 in the reference dataset to 0.1676025103420878 in the current dataset, indicating a change in the feature's contribution to the model's predictions.
* The feature's position in the ranking has remained the same, indicating that the feature's importance has not changed significantly.

Overall, the analysis suggests that the Income feature has undergone significant changes between the reference and current datasets, which may impact the model's performance. Further investigation is recommended to understand the implications of these changes on the model's predictions.

            ### Marital Status

            **Loan Default Prediction Data: Marital Status Feature Analysis**

**Feature Description**

* Name: Marital Status
* Description: Marital status, represented as 0 (Single), 1 (Married), 2 (Divorced), or 3 (Widowed).
* Type: categorical
* Possible Values: {'0': 'Single', '1': 'Married', '2': 'Divorced', '3': 'Widowed'}
* Data Type: int

**Tool Results**

### get_drift_report

The get_drift_report tool was used to analyze the Marital Status feature for data drift. The results are as follows:

* **General Drift Report Summary**
	+ Drift Share: 0.25
	+ Number of Columns Analyzed: 1
	+ Number of Drifted Columns: 1
	+ Share of Drifted Columns: 100.0%
	+ Dataset Drift: True
* **Detailed Drift Analysis per Column**
	+ Column Name: Marital Status
	+ Column Type: categorical
	+ Stat Test Name: Kullback-Leibler divergence
	+ Stat Test Threshold: 0.1
	+ Drift Score: 5.655843738731566
	+ Drift Detected: True
	+ Current Distribution: {'small_distribution': {'x': [0, 1, 2, 3], 'y': [2, 1, 0, 197]}}
	+ Reference Distribution: {'small_distribution': {'x': [0, 1, 2, 3], 'y': [20, 538, 237, 5]}}

The results indicate that the Marital Status feature has drifted significantly between the reference and current datasets, with a drift score of 5.655843738731566. This suggests that the distribution of the Marital Status feature has changed, which may impact the performance of the loan default prediction model.

### get_shap_values

The get_shap_values tool was used to calculate the mean(|SHAP value|) for the Marital Status feature. The results are as follows:

* **SHAP Values**
	+ Reference: {'value': 0.041422401537971096, 'position': 6}
	+ Current: {'value': 0.07354211915327408, 'position': 4}

The results indicate that the mean(|SHAP value|) for the Marital Status feature has increased from 0.041422401537971096 in the reference dataset to 0.07354211915327408 in the current dataset. This suggests that the Marital Status feature has become more important in the loan default prediction model, potentially due to changes in the input data distribution.

**Overall Feature Analysis**

The Marital Status feature has been found to have drifted significantly between the reference and current datasets, with a drift score of 5.655843738731566. Additionally, the mean(|SHAP value|) for the Marital Status feature has increased in the current dataset, indicating that the feature has become more important in the loan default prediction model. These findings suggest that the Marital Status feature may require retraining or re-tuning to maintain optimal performance in the current dataset.

            ### Credit Score

            **Loan Default Prediction Data: Credit Score Analysis Report**

**Feature Description**

* Name: Credit Score
* Description: Credit score of the borrower, ranging from 300 to 850.
* Type: numerical
* Possible Values: Ranging from 300 to 850.
* Data Type: int

**Tool Results**

### get_drift_report

The get_drift_report tool was used to analyze the distribution of the Credit Score feature between the reference and current datasets. The results are as follows:

* General Drift Report Summary:
	+ Drift Share: 0.0778065393961156
	+ Number of Columns Analyzed: 1
	+ Number of Drifted Columns: 0
	+ Share of Drifted Columns: 0.0
	+ Dataset Drift: False
* Detailed Drift Analysis per Column:
	+ Column Name: Credit Score
	+ Column Type: num
	+ Stat Test Name: Kullback-Leibler divergence
	+ Stat Test Threshold: 0.1
	+ Drift Score: 0.0778065393961156
	+ Drift Detected: False
	+ Current Distribution: {'small_distribution': {'x': [302.0, 356.8, 411.6, 466.4, 521.2, 576.0, 630.8, 685.5999999999999, 740.4, 795.2, 850.0], 'y': [0.00036496350364963496, 0.0008211678832116786, 0.0017335766423357678, 0.002372262773722625, 0.0031021897810219, 0.003558394160583945, 0.0031021897810219, 0.0019160583941605816, 0.0009124087591240865, 0.00036496350364963534]}}
	+ Reference Distribution: {'small_distribution': {'x': [300.0, 355.0, 410.0, 465.0, 520.0, 575.0, 630.0, 685.0, 740.0, 795.0, 850.0], 'y': [4.545454545454545e-05, 0.0003636363636363636, 0.0005454545454545455, 0.0016363636363636363, 0.0034772727272727273, 0.0045000000000000005, 0.0037272727272727275, 0.002545454545454545, 0.0010454545454545454, 0.00029545454545454547]}}

The results indicate that there is no significant drift detected in the Credit Score feature between the reference and current datasets.

### get_shap_values

The get_shap_values tool was used to calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions. The results are as follows:

* Reference:
	+ Value: 0.057266813197127224
	+ Position: 5
* Current:
	+ Value: 0.05259014360839969
	+ Position: 6

The results indicate that the Credit Score feature has a relatively stable impact on the model's predictions, with a slight decrease in its mean(|SHAP value|) value from the reference to the current dataset.

**Overall Feature Analysis**

The analysis of the Credit Score feature using the get_drift_report and get_shap_values tools suggests that there is no significant drift detected in the feature between the reference and current datasets. However, the get_shap_values tool indicates a slight decrease in the feature's impact on the model's predictions. This could be due to changes in the input data distribution, leading to changes in the order of feature contributions. Further analysis is recommended to understand the implications of these changes on the model's performance.

            ### Loan Term

            **Loan Term Feature Analysis Report**

**Feature Description**

* Name: Loan Term
* Description: Loan term in months, ranging from 12 to 60.
* Type: numerical
* Possible Values: Ranging from 12 to 60 months.
* Data Type: int

**Tool Results**

### get_drift_report

The get_drift_report tool was used to analyze the distribution of the Loan Term feature between the reference and current datasets. The results are as follows:

* General Drift Report Summary:
	+ Drift Share: 0.06991922445224397
	+ Number of Columns Analyzed: 1
	+ Number of Drifted Columns: 0
	+ Share of Drifted Columns: 0.0
	+ Dataset Drift: False
* Detailed Drift Analysis per Column:
	+ Column Name: Loan Term
	+ Column Type: num
	+ Stat Test Name: Kullback-Leibler divergence
	+ Stat Test Threshold: 0.1
	+ Drift Score: 0.06991922445224397
	+ Drift Detected: False
	+ Current Distribution: {'small_distribution': {'x': [17.0, 20.4, 23.8, 27.2, 30.6, 34.0, 37.4, 40.8, 44.2, 47.599999999999994, 51.0], 'y': [0.005882352941176473, 0.01323529411764705, 0.027941176470588247, 0.020588235294117636, 0.051470588235294136, 0.07205882352941179, 0.05000000000000002, 0.03529411764705877, 0.014705882352941213, 0.0029411764705882305]}}
	+ Reference Distribution: {'small_distribution': {'x': [12.0, 16.8, 21.6, 26.4, 31.2, 36.0, 40.8, 45.6, 50.4, 55.199999999999996, 60.0], 'y': [0.0031249999999999993, 0.006770833333333333, 0.018489583333333344, 0.0375, 0.04609374999999999, 0.0580729166666667, 0.029166666666666643, 0.007812500000000005, 0.0010416666666666673, 0.00026041666666666645]}}

The results indicate that there is no significant drift detected in the Loan Term feature between the reference and current datasets.

### get_shap_values

The get_shap_values tool was used to calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions. The results are as follows:

* Reference:
	+ Value: 0.10786701225337081
	+ Position: 2
* Current:
	+ Value: 0.08865791016936486
	+ Position: 2

The results indicate that the mean(|SHAP value|) for the Loan Term feature has decreased slightly between the reference and current datasets, but the position of the feature remains the same.

**Overall Feature Analysis**

The analysis of the Loan Term feature using the get_drift_report and get_shap_values tools suggests that there is no significant drift detected in the feature between the reference and current datasets. However, the mean(|SHAP value|) for the feature has decreased slightly, indicating a potential change in the feature's contribution to the model's predictions. Further analysis is recommended to determine the impact of this change on the model's performance.

            ### Employment Length

            **Loan Default Prediction Data: Employment Length Feature Analysis**

**Feature Description**

* Name: Employment Length
* Description: Number of years the borrower has been employed, ranging from 0 to 40.
* Type: numerical
* Possible Values: Ranging from 0 to 40 years.
* Data Type: int

**Tool Results**

### get_drift_report

The get_drift_report tool was used to analyze the Employment Length feature for data drift. The results are as follows:

* **General Drift Report Summary**
	+ Drift Share: 0.10422809774139326
	+ Number of Columns Analyzed: 1
	+ Number of Drifted Columns: 1
	+ Share of Drifted Columns: 100.0%
	+ Dataset Drift: True
* **Detailed Drift Analysis per Column**
	+ Column Name: Employment Length
	+ Column Type: numerical
	+ Stat Test Name: Kullback-Leibler divergence
	+ Stat Test Threshold: 0.1
	+ Drift Score: 0.10422809774139326
	+ Drift Detected: True
	+ Current Distribution: {'small_distribution': {'x': [0.0, 4.0, 8.0, 12.0, 16.0, 20.0, 24.0, 28.0, 32.0, 36.0, 40.0], 'y': [0.0025, 0.00375, 0.03, 0.0525, 0.06375, 0.04375, 0.03125, 0.0175, 0.00375, 0.00125]}}
	+ Reference Distribution: {'small_distribution': {'x': [1.0, 4.9, 8.8, 12.7, 16.6, 20.5, 24.4, 28.3, 32.2, 36.1, 40.0], 'y': [0.0016025641025641025, 0.004807692307692307, 0.014102564102564108, 0.038141025641025623, 0.07211538461538464, 0.06730769230769233, 0.038141025641025623, 0.014102564102564094, 0.00480769230769231, 0.0012820512820512825]}}

The results indicate that the Employment Length feature shows significant data drift, with a drift score of 0.10422809774139326. This suggests that the distribution of the Employment Length feature has changed significantly between the reference and current datasets, which may lead to a decrease in model performance.

### get_shap_values

The get_shap_values tool was used to calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions. The results are as follows:

* **Reference SHAP Values**
	+ Value: 0.07748587080834744
	+ Position: 4
* **Current SHAP Values**
	+ Value: 0.07723764793746474
	+ Position: 3

The results indicate that the Employment Length feature has a relatively high mean(|SHAP value|) value, indicating that it has a significant impact on the model's predictions. However, the position of the feature has changed slightly between the reference and current datasets, suggesting that the feature attribution drift may be present.

**Overall Feature Analysis**

The Employment Length feature shows significant data drift, with a drift score of 0.10422809774139326. This suggests that the distribution of the Employment Length feature has changed significantly between the reference and current datasets, which may lead to a decrease in model performance. Additionally, the feature attribution drift analysis suggests that the feature may have a different impact on the model's predictions in the current dataset compared to the reference dataset. Therefore, it is recommended to retrain the model using the current dataset to ensure optimal performance.

            ### Dependents

            **Loan Default Prediction Data: Dependents Feature Analysis Report**

**Feature Description**

* Name: Dependents
* Description: Number of dependents, ranging from 0 to 5.
* Type: categorical
* Possible Values: Ranging from 0 to 5.
* Data Type: int

**Tool Results**

### get_drift_report

The get_drift_report tool was used to analyze the distribution of the Dependents feature between the reference and current datasets. The results are as follows:

* **General Drift Report Summary**
	+ Drift Share: 0.1290888567959812
	+ Number of Columns Analyzed: 1
	+ Number of Drifted Columns: 1
	+ Share of Drifted Columns: 100.0%
	+ Dataset Drift: True
* **Detailed Drift Analysis per Column**
	+ Column Name: Dependents
	+ Column Type: categorical
	+ Stat Test Name: Kullback-Leibler divergence
	+ Stat Test Threshold: 0.1
	+ Drift Score: 0.1290888567959812
	+ Drift Detected: True
	+ Current Distribution: {'small_distribution': {'x': [0, 1, 2, 3, 4, 5], 'y': [0, 2, 29, 78, 69, 22]}}
	+ Reference Distribution: {'small_distribution': {'x': [0, 1, 2, 3, 4, 5], 'y': [2, 20, 178, 385, 207, 8]}}

The results indicate that the Dependents feature shows significant drift between the reference and current datasets, with a drift score of 0.1290888567959812. This suggests that the distribution of the Dependents feature has changed significantly, which may impact the performance of the loan default prediction model.

### get_shap_values

The get_shap_values tool was used to calculate the mean(|SHAP value|) for each feature to detect feature attribution drift. The results are as follows:

* **SHAP Values for Reference and Current Datasets**
	+ Reference: {'value': 0.02095623100403098, 'position': 9}
	+ Current: {'value': 0.01848637683404379, 'position': 8}

The results indicate that the mean(|SHAP value|) for the Dependents feature has decreased from 0.02095623100403098 in the reference dataset to 0.01848637683404379 in the current dataset, with a position change from 9 to 8. This suggests that the feature attribution drift may be occurring, which could impact the performance of the loan default prediction model.

**Overall Feature Analysis**

The analysis of the Dependents feature using the get_drift_report and get_shap_values tools suggests that there is significant drift in the feature distribution between the reference and current datasets. The drift score and SHAP value analysis indicate that the feature attribution drift may be occurring, which could impact the performance of the loan default prediction model. Therefore, it is recommended to retrain the model using the current dataset to ensure optimal performance.

            ### Loan Amount

            **Loan Amount Feature Analysis Report**

**Feature Description**

* Name: Loan Amount
* Description: Loan amount requested by the borrower in dollars, ranging from $1,000 to $50,000.
* Type: numerical
* Possible Values: Ranging from $1,000 to $50,000.
* Data Type: float

**Tool Results**

### get_drift_report

The get_drift_report tool was used to analyze the distribution of the Loan Amount feature between the reference and current datasets. The results are as follows:

* General Drift Report Summary:
	+ Drift Share: 0.06465984187565631
	+ Number of Columns Analyzed: 1
	+ Number of Drifted Columns: 0
	+ Share of Drifted Columns: 0.0
	+ Dataset Drift: False
* Detailed Drift Analysis per Column:
	+ Column Name: Loan Amount
	+ Column Type: num
	+ Stat Test Name: Kullback-Leibler divergence
	+ Stat Test Threshold: 0.1
	+ Drift Score: 0.06465984187565631
	+ Drift Detected: False
	+ Current Distribution: {'small_distribution': {'x': [3141.1142328202486, 7827.002809538224, 12512.8913862562, 17198.779962974175, 21884.66853969215, 26570.557116410124, 31256.445693128102, 35942.33426984608, 40628.22284656405, 45314.111423282025, 50000.0], 'y': [1.0670334810867463e-06, 1.0670334810867459e-05, 2.2407703102821676e-05, 3.9480238800209616e-05, 5.3351674054337314e-05, 3.841320531912284e-05, 3.201100443260239e-05, 1.173736829195421e-05, 1.0670334810867465e-06, 3.2011004432602396e-06]}}
	+ Reference Distribution: {'small_distribution': {'x': [1000.0, 5900.0, 10800.0, 15700.0, 20600.0, 25500.0, 30400.0, 35300.0, 40200.0, 45100.0, 50000.0], 'y': [7.653061224489795e-07, 6.122448979591836e-06, 1.8112244897959183e-05, 4.23469387755102e-05, 5.2806122448979595e-05, 5.4081632653061225e-05, 2.2448979591836734e-05, 6.122448979591836e-06, 1.0204081632653063e-06, 2.5510204081632656e-07]}}

The results indicate that there is no significant drift detected in the Loan Amount feature between the reference and current datasets.

### get_shap_values

The get_shap_values tool was used to calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions. The results are as follows:

* Reference:
	+ Value: 0.03091725874540736
	+ Position: 7
* Current:
	+ Value: 0.030296443826883252
	+ Position: 7

The results indicate that the Loan Amount feature has a relatively consistent impact on the model's predictions across both the reference and current datasets, with a slight decrease in its mean(|SHAP value|) in the current dataset.

**Overall Feature Analysis**

The Loan Amount feature analysis reveals that there is no significant drift detected in the feature distribution between the reference and current datasets. Additionally, the feature's impact on the model's predictions remains relatively consistent across both datasets, with a slight decrease in its mean(|SHAP value|) in the current dataset.

            ### Interest Rate

            **Loan Default Prediction Data: Interest Rate Feature Analysis**

**Feature Description**

* Name: Interest Rate
* Description: Interest rate of the loan in percentage, ranging from 3.5% to 25%.
* Type: numerical
* Possible Values: Ranging from 3.5% to 25%.
* Data Type: float

**Tool Results**

### get_drift_report

The get_drift_report tool was used to analyze the Interest Rate feature for data drift. The results are as follows:

* **General Drift Report Summary**
	+ Drift Share: 0.12211093048448328
	+ Number of Columns: 1
	+ Number of Drifted Columns: 1
	+ Share of Drifted Columns: 100.0%
	+ Dataset Drift: True
* **Detailed Drift Analysis per Column**
	+ Column Name: Interest Rate
	+ Column Type: numerical
	+ Stat Test Name: Kullback-Leibler divergence
	+ Stat Test Threshold: 0.1
	+ Drift Score: 0.12211093048448328
	+ Drift Detected: True
	+ Current Distribution: {'small_distribution': {'x': [6.40996299737573, 8.268966697638156, 10.127970397900583, 11.98697409816301, 13.845977798425437, 15.704981498687864, 17.56398519895029, 19.42298889921272, 21.281992599475146, 23.140996299737573, 25.0], 'y': [0.016137676324025095, 0.04841302897207526, 0.06724031801677119, 0.08068838162012543, 0.09144683250280883, 0.10220528338549223, 0.05648186713408781, 0.04034419081006271, 0.018827289044695935, 0.016137676324025088]}}
	+ Reference Distribution: {'small_distribution': {'x': [3.5, 5.65, 7.8, 9.95, 12.1, 14.25, 16.4, 18.549999999999997, 20.7, 22.849999999999998, 25.0], 'y': [0.004069767441860464, 0.00930232558139535, 0.03546511627906978, 0.0697674418604651, 0.11104651162790695, 0.12034883720930241, 0.07616279069767447, 0.034302325581395315, 0.004069767441860468, 0.0005813953488372088]}}

The results indicate that the Interest Rate feature shows significant data drift, with a drift score of 0.12211093048448328. This suggests that the distribution of the Interest Rate feature has changed significantly between the reference and current datasets, which may lead to a decrease in model performance.

### get_shap_values

The get_shap_values tool was used to calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions. The results are as follows:

* **SHAP Values**
	+ Reference: {'value': 0.02195194757664086, 'position': 8}
	+ Current: {'value': 0.017982049611167866, 'position': 9}

The results indicate that the Interest Rate feature has a relatively low mean(|SHAP value|) value in both the reference and current datasets, indicating that it has a moderate impact on the model's predictions. However, the position of the feature has changed from 8 in the reference dataset to 9 in the current dataset, suggesting that the feature's importance may have decreased slightly.

**Overall Feature Analysis**

The analysis of the Interest Rate feature using the get_drift_report and get_shap_values tools suggests that the feature shows significant data drift, which may impact the model's performance. The feature's importance has decreased slightly, but it still has a moderate impact on the model's predictions. Further analysis and model retraining may be necessary to address the data drift and improve the model's performance.
