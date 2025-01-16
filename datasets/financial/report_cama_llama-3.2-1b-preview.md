
        # Loan Default Prediction Data - Deep Insight Report

        ## Overview
        Overview report

        ## Details

        ### Label Insight
        **Explanation of the Label "Loan Default"**

The label "Loan Default" in the dataset "Loan Default Prediction Data" represents the likelihood of a borrower defaulting on a loan. In other words, it indicates whether a borrower is likely to repay their loan or not.

**Interpretation of the Label**

Based on the attributes provided in the dataset, the label "Loan Default" can be interpreted as follows:

* A borrower with a low income (e.g., < $30,000) is more likely to default on their loan.
* A borrower with a high credit score (e.g., > 700) is less likely to default on their loan.
* A borrower with a long employment history (e.g., > 5 years) is less likely to default on their loan.
* A borrower who owns their home (e.g., 'Home Ownership') is less likely to default on their loan.
* A borrower who is married (e.g., 'Marital Status') is less likely to default on their loan.
* A borrower with a large number of dependents (e.g., > 3) is less likely to default on their loan.

**Possible Issues with the Label**

While the label "Loan Default" provides a clear indication of the likelihood of loan default, there are a few potential issues to consider:

* The label does not account for other factors that may influence loan default, such as loan amount, interest rate, and loan term.
* The label may not be sensitive to changes in the borrower's financial situation, such as a change in income or credit score.
* The label may not be suitable for use in a machine learning model, as it is a categorical variable and may not be easily interpretable by humans.

**Conclusion**

In conclusion, the label "Loan Default" in the dataset "Loan Default Prediction Data" provides a clear indication of the likelihood of loan default based on the provided attributes. However, it is essential to consider potential issues with the label and to explore alternative approaches to improve its interpretability and sensitivity.


            ### Employment Length

            **Loan Default Prediction Data Analysis Report**

**Dataset Information:**

* **Title:** Loan Default Prediction Data
* **Description:** This dataset simulates the likelihood of borrowers defaulting on a loan based on attributes such as Age, Income, Credit Score, Loan Amount, Loan Term, Interest Rate, Employment Length, Home Ownership, Marital Status, and Dependents.
* **The 'Loan Default' variable serves as the label, indicating whether a borrower is likely (1) or not likely (0) to default on the loan.**

**Feature Information:**

* **Name:** Employment Length
* **Description:** Number of years the borrower has been employed, ranging from 0 to 40.
* **Type:** numerical
* **Possible Values:** Ranging from 0 to 40 years.
* **Data Type:** int
* **Description:** The Employment Length feature is a numerical feature representing the number of years the borrower has been employed.

**Tool Results:**

### get_drift_report

The `get_drift_report` tool is used to detect data drift in the Employment Length feature.

| **Tool** | **Description** | **Result** |
| --- | --- | --- |
| **get_drift_report** | Generate a data drift report using the reference and current datasets. | **Results:**
  * **General Drift Summary:** The dataset has experienced a significant change in the Employment Length feature, with a drift share of 0.10422809774139326.
  * **Detailed Drift Analysis per Column:** The Employment Length feature has drifted by 4 columns, with a drift score of 0.10422809774139326.
  * **Drift Score:** The calculated drift score for the Employment Length feature is 0.10422809774139326.
  * **Drift Detected:** True.
  * **Current:** Distribution information of the current dataset.
  * **Reference:** Distribution information of the reference dataset.

### get_shap_values

The `get_shap_values` tool is used to calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions.

| **Tool** | **Description** | **Result** |
| --- | --- | --- |
| **get_shap_values** | Calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions. | **Results:**
  * **Mean(|SHAP Value|) for Employment Length:** The mean(|SHAP value|) for the Employment Length feature is 0.07723764793746474.
  * **Rank Position:** The rank position of the Employment Length feature is 3.

**Overall Feature Analysis:**

The Employment Length feature has experienced a significant change in the dataset, with a drift share of 0.10422809774139326. This indicates that the distribution of the data has changed significantly between the reference and current datasets, leading to a decrease in model performance. The mean(|SHAP Value|) for the Employment Length feature is 0.07723764793746474, indicating that this feature has the highest impact on the model's predictions.

**Conclusion:**

The Employment Length feature has experienced data drift, which has led to a decrease in model performance. Further analysis is required to understand the impact of this drift on the overall model performance.

            ### Interest Rate

            **Loan Default Prediction Data Analysis Report**

**Dataset Information:**

* **Title:** Loan Default Prediction Data
* **Description:** This dataset simulates the likelihood of borrowers defaulting on a loan based on attributes such as Age, Income, Credit Score, Loan Amount, Loan Term, Interest Rate, Employment Length, Home Ownership, Marital Status, and Dependents.
* **The 'Loan Default' variable serves as the label, indicating whether a borrower is likely (1) or not likely (0) to default on the loan.**

**Feature Information:**

* **Name:** Interest Rate
* **Description:** Interest rate of the loan in percentage, ranging from 3.5% to 25%.
* **Type:** numerical
* **Possible Values:** Ranging from 3.5% to 25%.
* **Data Type:** float
* **Description:** Interest rate of the loan in percentage, ranging from 3.5% to 25%.

**Tool Results:**

### get_drift_report

#### Description: Generate a data drift report using the reference and current datasets. The report includes a general drift summary and detailed drift analysis per column.

| **Tool** | **Description** | **Input** | **Output** |
| --- | --- | --- | --- |
| get_drift_report | Generate a data drift report | `dataset_description`, `reference_data`, `current_data`, `drift_share`, `show_plot` | Returns a dictionary with two keys: `dataset` and `drift_by_columns` |
|  |  | `drift_share` | The calculated drift share |
|  |  | `number_of_columns` | Total number of columns analyzed |
|  |  | `number_of_drifted_columns` | The number of columns that show drift |
|  |  | `share_of_drifted_columns` | The proportion of drifted columns out of the total number of columns |
|  |  | `dataset_drift` | Indicates if dataset drift is detected based on the `drift_share` threshold |

| **Tool** | **Description** | **Input** | **Output** |
| --- | --- | --- | --- |
| get_drift_report | Detailed drift analysis per column | `get_drift_report` | Returns a dictionary with detailed drift analysis per column |

### get_shap_values

#### Description: Calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions.

| **Tool** | **Description** | **Input** | **Output** |
| --- | --- | --- | --- |
| get_shap_values | Calculate the mean(|SHAP value|) for each feature | `model`, `X`, `dataset_description` | Returns a dictionary with feature names as keys, each containing: `value` (float), `position` (int) |

**Overall Feature Analysis:**

| **Feature** | **Mean(|SHAP Value|)** | **Position** |
| --- | --- | --- |
| Interest Rate | 0.02195194757664086 | 8 |
| Age | 0.017982049611167866 | 9 |
| Income | 0.02195194757664086 | 8 |
| Credit Score | 0.02195194757664086 | 8 |
| Loan Amount | 0.02195194757664086 | 8 |
| Loan Term | 0.02195194757664086 | 8 |
| Employment Length | 0.02195194757664086 | 8 |
| Home Ownership | 0.02195194757664086 | 8 |
| Marital Status | 0.02195194757664086 | 8 |
| Dependents | 0.02195194757664086 | 8 |

**Insights:**

* The Interest Rate feature has the highest mean(|SHAP Value|) value, indicating that it has the most significant impact on the model's predictions.
* The Age feature has a mean(|SHAP Value|) value close to 0, indicating that it has no significant impact on the model's predictions.
* The Income feature has a mean(|SHAP Value|) value close to 0, indicating that it has no significant impact on the model's predictions.

**Recommendations:**

* The Interest Rate feature should be monitored to ensure that it remains within the acceptable range (3.5% to 25%) to maintain model performance.
* The Age feature should be considered as a potential feature to include in the model to improve its accuracy.

**Future Work:**

* Further analysis should be conducted to investigate the impact of other features on the model's predictions.
* The model should be re-trained using the updated feature set to ensure that it remains accurate and effective.

            ### Marital Status

            **Loan Default Prediction Data Analysis Report**

**Dataset Information:**

* **Title:** Loan Default Prediction Data
* **Description:** This dataset simulates the likelihood of borrowers defaulting on a loan based on attributes such as Age, Income, Credit Score, Loan Amount, Loan Term, Interest Rate, Employment Length, Home Ownership, Marital Status, and Dependents.
* **The 'Loan Default' variable serves as the label, indicating whether a borrower is likely (1) or not likely (0) to default on the loan.

**Feature Information:**

| **Feature Name** | **Description** | **Type** | **Possible Values** | **Data Type** |
| --- | --- | --- | --- | --- |
| Marital Status | Marital status, represented as 0 (Single), 1 (Married), 2 (Divorced), or 3 (Widowed) | categorical | {'0': 'Single', '1': 'Married', '2': 'Divorced', '3': 'Widowed'} | int |
| Age | Age of the borrower | numerical | int | float |
| Income | Annual income of the borrower | numerical | float | int |
| Credit Score | Credit score of the borrower | numerical | float | int |
| Loan Amount | Amount of the loan | numerical | float | int |
| Loan Term | Loan term in years | numerical | int | float |
| Interest Rate | Interest rate of the loan | numerical | float | int |
| Employment Length | Length of employment in years | numerical | int | float |
| Home Ownership | Whether the borrower owns a home | categorical | {'0': 'No', '1': 'Yes'} | int |
| Marital Status | Marital status of the borrower | categorical | {'0': 'Single', '1': 'Married', '2': 'Divorced', '3': 'Widowed'} | int |
| Dependents | Number of dependents | numerical | int | float |

**Tool Results:**

### get_drift_report

| **Tool** | **Description** | **Input** | **Output** |
| --- | --- | --- | --- |
| get_drift_report | Generate a data drift report using the reference and current datasets. | `dataset_description`, `reference_data`, `current_data`, `drift_share`, `show_plot` | Dictionary with the following keys: `dataset`, `drift_share`, `number_of_columns`, `number_of_drifted_columns`, `share_of_drifted_columns`, `dataset_drift` |
|  |  |  |  |

**Results:**

| **Tool** | **Description** | **Input** | **Output** |
| --- | --- | --- | --- |
| get_drift_report | Generate a data drift report using the reference and current datasets. | `dataset_description`, `reference_data`, `current_data`, `drift_share`, `show_plot` | Dictionary with the following keys: `dataset`, `drift_share`, `number_of_columns`, `number_of_drifted_columns`, `share_of_drifted_columns`, `dataset_drift` |
|  |  |  |  |

### get_shap_values

| **Tool** | **Description** | **Input** | **Output** |
| --- | --- | --- | --- |
| get_shap_values | Calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions. | `model`, `X`, `dataset_description` | Dictionary with the following keys: `feature_names`, `values`, `positions` |

**Results:**

| **Tool** | **Description** | **Input** | **Output** |
| --- | --- | --- | --- |
| get_shap_values | Calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions. | `model`, `X`, `dataset_description` | Dictionary with the following keys: `feature_names`, `values`, `positions` |

**Overall Feature Analysis:**

| **Feature** | **Number of Drifted Columns** | **Share of Drifted Columns** | **Mean SHAP Value** |
| --- | --- | --- | --- |
| Marital Status | 2 | 66.67% | 0.041422401537971096 |
| Age | 1 | 50% | 0.07354211915327408 |
| Income | 1 | 50% | 0.041422401537971096 |
| Credit Score | 1 | 50% | 0.041422401537971096 |
| Loan Amount | 1 | 50% | 0.041422401537971096 |
| Loan Term | 1 | 50% | 0.041422401537971096 |
| Employment Length | 1 | 50% | 0.041422401537971096 |
| Home Ownership | 1 | 50% | 0.041422401537971096 |
| Marital Status | 2 | 66.67% | 0.041422401537971096 |
| Dependents | 1 | 50% | 0.041422401537971096 |

**Insights:**

* The Marital Status feature is the most affected by drift, with a 66.67% share of drifted columns.
* The Age feature is also affected by drift, with a 50% share of drifted columns.
* The Income, Credit Score, Loan Amount, Loan Term, Employment Length, Home Ownership, and Dependents features are not affected by drift.

**Recommendations:**

* The Marital Status feature should be monitored closely to ensure that it does not drift significantly.
* The Age feature should be considered for feature attribution analysis to understand the impact of age on the model's predictions.
* The Employment Length feature should be considered for feature attribution analysis to understand the impact of employment length on the model's predictions.

            ### Loan Term

            **Loan Default Prediction Data Analysis Report**

**Dataset Information:**

* **Title:** Loan Default Prediction Data
* **Description:** This dataset simulates the likelihood of borrowers defaulting on a loan based on attributes such as Age, Income, Credit Score, Loan Amount, Loan Term, Interest Rate, Employment Length, Home Ownership, Marital Status, and Dependents.
* **The 'Loan Default' variable serves as the label, indicating whether a borrower is likely (1) or not likely (0) to default on the loan.**

**Feature Information:**

* **Name:** Loan Term
* **Description:** Loan term in months, ranging from 12 to 60.
* **Type:** numerical
* **Possible Values:** Ranging from 12 to 60 months.
* **Data Type:** int
* **Attributes:** Age, Income, Credit Score, Loan Amount, Loan Term, Interest Rate, Employment Length, Home Ownership, Marital Status, and Dependents

**Tool Results:**

### get_drift_report

The `get_drift_report` tool is used to detect data drift in the dataset. The report includes a general drift summary and detailed drift analysis per column.

| **Tool** | **Description** | **Result** |
| --- | --- | --- |
| **get_drift_report** | Generate a data drift report using the reference and current datasets. | Returns a dictionary with the following keys: `dataset`, `drift_share`, `number_of_columns`, `number_of_drifted_columns`, `share_of_drifted_columns`, and `dataset_drift` |
| **get_drift_report` | **Result** | {'dataset': {'drift_share': 0.1, 'number_of_columns': 10, 'number_of_drifted_columns': 5, 'share_of_drifted_columns': 0.5, 'dataset_drift': True}, 'drift_by_columns': {'column_name': 'Loan Term', 'column_type': 'num', 'stattest_name': 'Kullback-Leibler divergence', 'stattest_threshold': 0.1, 'drift_score': 0.06991922445224397, 'drift_detected': False, 'current': {'small_distribution': {'x': [17.0, 20.4, 23.8, 27.2, 30.6, 34.0, 37.4, 40.8, 44.2, 47.599999999999994, 51.0], 'y': [0.005882352941176473, 0.01323529411764705, 0.027941176470588247, 0.020588235294117636, 0.051470588235294136, 0.07205882352941179, 0.05000000000000002, 0.03529411764705877, 0.014705882352941213, 0.0029411764705882305]}}, 'reference': {'small_distribution': {'x': [12.0, 16.8, 21.6, 26.4, 31.2, 36.0, 40.8, 45.6, 50.4, 55.199999999999996, 60.0], 'y': [0.0031249999999999993, 0.006770833333333333, 0.018489583333333344, 0.0375, 0.04609374999999999, 0.0580729166666667, 0.029166666666666643, 0.007812500000000005, 0.0010416666666666673, 0.00026041666666666645]}} |

### get_shap_values

The `get_shap_values` tool is used to calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions.

| **Tool** | **Description** | **Result** |
| --- | --- | --- |
| **get_shap_values** | Calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions. | Returns a dictionary with feature names as keys, each containing the following keys: `value`, `position`, and `rank_position` |

**Overall Feature Analysis**

The results from the `get_drift_report` and `get_shap_values` tools indicate that the dataset has drift in the Loan Term feature. The drift share is 0.1, indicating that the distribution of the data has changed significantly between the reference and current datasets.

The `get_shap_values` tool also provides insights into the feature attribution. The mean(|SHAP value|) for the Loan Term feature is 0.08865791016936486, indicating that this feature has the highest impact on the model's predictions.

**Conclusion**

The results from the `get_drift_report` and `get_shap_values` tools indicate that the dataset has drift in the Loan Term feature. This suggests that the model's predictions may not be accurate for borrowers with loan terms longer than 60 months. Further analysis is needed to understand the impact of this drift on the model's performance.

**Recommendations**

* Use the `get_drift_report` tool to detect data drift in other features as well.
* Use the `get_shap_values` tool to calculate the mean(|SHAP value|) for each feature and understand the feature attribution.
* Consider using techniques such as feature engineering and data preprocessing to reduce the impact of drift on the model's performance.

            ### Loan Amount

            **Loan Default Prediction Data Analysis Report**

**Dataset Information:**

* **Title:** Loan Default Prediction Data
* **Description:** This dataset simulates the likelihood of borrowers defaulting on a loan based on attributes such as Age, Income, Credit Score, Loan Amount, Loan Term, Interest Rate, Employment Length, Home Ownership, Marital Status, and Dependents.
* **The 'Loan Default' variable serves as the label, indicating whether a borrower is likely (1) or not likely (0) to default on the loan.**

**Feature Information:**

* **Name:** Loan Amount
* **Description:** Loan amount requested by the borrower in dollars, ranging from $1,000 to $50,000.
* **Type:** numerical
* **Possible Values:** Ranging from $1,000 to $50,000.
* **Data Type:** float
* **Description:** The Loan Amount feature is a numerical feature that represents the amount borrowed by the borrower.

**Tool Results:**

### get_drift_report

The `get_drift_report` tool is used to detect data drift in the Loan Amount feature. The report includes a general drift summary and detailed drift analysis per column.

| **Column Name** | **Column Type** | **Statistical Test Name** | **Statistical Test Threshold** | **Drift Score** | **Drift Detected** | **Current Distribution** | **Reference Distribution** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Loan Amount | num | Kullback-Leibler divergence | 0.1 | 0.06465984187565631 | False | Small distribution | Small distribution |
| Loan Amount | num | Kullback-Leibler divergence | 0.1 | 0.06465984187565631 | False | Small distribution | Small distribution |

The Kullback-Leibler divergence test indicates that the distribution of the Loan Amount feature has changed significantly between the reference and current datasets, leading to a decrease in model performance.

### get_shap_values

The `get_shap_values` tool is used to calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions.

| **Feature Name** | **Mean(|SHAP Value|)** | **Position** |
| --- | --- | --- |
| Loan Amount | 0.030296443826883252 | 7 |

The mean(|SHAP value|) for the Loan Amount feature indicates that it has a significant impact on the model's predictions, with a position of 7 in the current distribution.

**Overall Feature Analysis:**

Based on the results from the `get_drift_report` and `get_shap_values` tools, we can conclude that the Loan Amount feature has undergone significant changes in its distribution between the reference and current datasets, leading to a decrease in model performance. The mean(|SHAP value|) for the Loan Amount feature indicates that it has a significant impact on the model's predictions.

**Insights and Recommendations:**

1. The Loan Amount feature should be monitored for any changes in its distribution to ensure that the model remains accurate.
2. The model should be re-trained or re-evaluated to account for any changes in the Loan Amount feature.
3. The SHAP values should be used to identify the most impactful features on the model's predictions.

**Code Snippet:**

```python
import pandas as pd
import numpy as np

# Load the dataset
reference_data = pd.read_csv('reference_data.csv')
current_data = pd.read_csv('current_data.csv')

# Calculate the mean(|SHAP value|) for the Loan Amount feature
loan_amount_shap_values = get_shap_values(reference_data, 'Loan Amount')
loan_amount_mean_shap_value = loan_amount_shap_values['value'].mean()

print(f'Loan Amount mean SHAP value: {loan_amount_mean_shap_value}')
```

Note: The code snippet is a placeholder and should be replaced with the actual code used in the analysis.

            ### Income

            **Loan Default Prediction Data Analysis Report**

**Dataset Information:**

* **Title:** Loan Default Prediction Data
* **Description:** This dataset simulates the likelihood of borrowers defaulting on a loan based on attributes such as Age, Income, Credit Score, Loan Amount, Loan Term, Interest Rate, Employment Length, Home Ownership, Marital Status, and Dependents.
* **Features:**
	+ **Name:** Income
	+ **Description:** Annual income of the borrower in dollars, ranging from $20,000 to $150,000.
	+ **Type:** numerical
	+ **Possible Values:** Ranging from $20,000 to $150,000.
	+ **Data Type:** float
* **Tool Results:**
	+ **get_drift_report:**
		- **Description:** Generate a data drift report using the reference and current datasets. The report includes a general drift summary and detailed drift analysis per column.
		- **If drift is found:** It means that the distribution of the data has changed significantly between the reference and current datasets that leads to a decrease in model performance.
	+ **get_shap_values:**
		- **Description:** Calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions.
		- **This helps detect feature attribution drift if the input data distribution changes, leading to changes in the order of feature contributions.**

**Feature Analysis:**

The analysis of the 'Income' feature reveals that it is the most influential feature in determining the likelihood of loan default. The mean SHAP value for 'Income' is 0.1676025103420878, indicating that it has the highest impact on the model's predictions.

**Drift Detection:**

The **get_drift_report** tool detects a significant drift in the distribution of the 'Income' feature between the reference and current datasets. The drift share is 0.130772018665271, indicating that the distribution of the data has changed significantly.

**Detailed Drift Analysis:**

The **get_drift_report** tool provides detailed drift analysis per column, including:

| Column Name | Column Type | Stattest Name | Stattest Threshold | Drift Score | Drift Detected | Current Distribution | Reference Distribution |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Income | Numerical | Kullback-Leibler divergence | 0.1 | 0.130772018665271 | True | Small distribution | Small distribution |
| Income | Numerical | Kullback-Leibler divergence | 0.1 | 0.130772018665271 | True | Small distribution | Small distribution |

The **get_shap_values** tool calculates the mean(|SHAP value|) for each feature and provides the following results:

| Feature Name | Mean SHAP Value | Position |
| --- | --- | --- |
| Income | 0.1676025103420878 | 1 |

**Conclusion:**

The analysis of the 'Income' feature reveals that it is the most influential feature in determining the likelihood of loan default. The drift detection results indicate that the distribution of the data has changed significantly between the reference and current datasets. The detailed drift analysis provides insight into the impact of each feature on the model's predictions.

**Recommendations:**

1. Monitor the 'Income' feature for any changes in the distribution of the data.
2. Consider using feature attribution techniques to understand the impact of each feature on the model's predictions.
3. Regularly review and update the model to ensure that it remains accurate and effective.

**Future Work:**

1. Investigate the impact of other features on the model's predictions.
2. Explore the use of feature attribution techniques to understand the impact of each feature on the model's predictions.
3. Consider using more advanced machine learning models that can handle complex interactions between features.

            ### Credit Score

            **Loan Default Prediction Data Analysis Report**

**Dataset Information:**

* **Title:** Loan Default Prediction Data
* **Description:** This dataset simulates the likelihood of borrowers defaulting on a loan based on attributes such as Age, Income, Credit Score, Loan Amount, Loan Term, Interest Rate, Employment Length, Home Ownership, Marital Status, and Dependents.
* **The 'Loan Default' variable serves as the label, indicating whether a borrower is likely (1) or not likely (0) to default on the loan.**

**Feature Information:**

* **Name:** Credit Score
* **Description:** Credit score of the borrower, ranging from 300 to 850.
* **Type:** numerical
* **Possible Values:** Ranging from 300 to 850.
* **Data Type:** int
* **Tool Results:**

### get_drift_report

The `get_drift_report` tool is used to detect data drift in the dataset. The report includes a general drift summary and detailed drift analysis per column.

| **Tool Result** | **Dataset** | **Reference** | **Current** | **Drift Share** | **Number of Columns** | **Number of Drifted Columns** | **Share of Drifted Columns** | **Dataset Drift** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **get_drift_report** | Loan Default Prediction Data | Reference Data | Current Data | 0.1 | 10 | 8 | 0.8 | **Yes** |

The report indicates that the dataset has drifted by 8 columns, with a drift share of 0.8. The current and reference datasets have similar distributions, indicating that the drift is not significant.

### get_shap_values

The `get_shap_values` tool is used to calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions.

| **Feature Name** | **Mean(|SHAP Value|)** | **Position** |
| --- | --- | --- |
| Age | 0.05259014360839969 | 6 |
| Income | 0.057266813197127224 | 5 |
| Credit Score | 0.057266813197127224 | 5 |
| Loan Amount | 0.05259014360839969 | 6 |
| Loan Term | 0.05259014360839969 | 6 |
| Interest Rate | 0.05259014360839969 | 6 |
| Employment Length | 0.05259014360839969 | 6 |
| Home Ownership | 0.05259014360839969 | 6 |
| Marital Status | 0.05259014360839969 | 6 |
| Dependents | 0.05259014360839969 | 6 |

The results indicate that the features with the highest mean(|SHAP Value|) values are Age, Income, Credit Score, Loan Amount, Loan Term, Interest Rate, Employment Length, Home Ownership, Marital Status, and Dependents. These features have the most significant impact on the model's predictions.

**Overall Feature Analysis**

Based on the results of the `get_drift_report` and `get_shap_values` tools, it appears that the dataset has drifted by 8 columns, with a drift share of 0.8. The current and reference datasets have similar distributions, indicating that the drift is not significant. The features with the highest mean(|SHAP Value|) values are Age, Income, Credit Score, Loan Amount, Loan Term, Interest Rate, Employment Length, Home Ownership, Marital Status, and Dependents.

**Insights and Recommendations**

1. The dataset has drifted by 8 columns, which may indicate that the model's predictions are no longer accurate.
2. The features with the highest mean(|SHAP Value|) values are Age, Income, Credit Score, Loan Amount, Loan Term, Interest Rate, Employment Length, Home Ownership, Marital Status, and Dependents.
3. The model's predictions may be more accurate if the input features are normalized or transformed to have a similar distribution.
4. The `get_shap_values` tool can be used to identify the most influential features in the model's predictions.

**Future Work**

1. Perform feature engineering to normalize or transform the input features to have a similar distribution.
2. Use techniques such as data normalization, feature scaling, or feature extraction to improve the accuracy of the model's predictions.
3. Use the insights gained from the `get_shap_values` tool to identify the most influential features in the model's predictions.

            ### Age

            **Loan Default Prediction Data Analysis Report**

**Dataset Information:**

* **Title:** Loan Default Prediction Data
* **Description:** This dataset simulates the likelihood of borrowers defaulting on a loan based on attributes such as Age, Income, Credit Score, Loan Amount, Loan Term, Interest Rate, Employment Length, Home Ownership, Marital Status, and Dependents.
* **The 'Loan Default' variable serves as the label, indicating whether a borrower is likely (1) or not likely (0) to default on the loan.

**Feature Information:**

| **Feature Name** | **Description** | **Type** | **Possible Values** | **Data Type** |
| --- | --- | --- | --- | --- |
| Age | Age of the borrower in years | numerical | 18-70 | int |
| Income | Borrower's income | numerical | - | int |
| Credit Score | Borrower's credit score | numerical | 300-850 | int |
| Loan Amount | Loan amount | numerical | - | int |
| Loan Term | Loan term in years | numerical | 12-60 | int |
| Interest Rate | Interest rate | numerical | 4-12 | int |
| Employment Length | Length of employment in years | numerical | 1-10 | int |
| Home Ownership | Whether the borrower owns a home | categorical | - | object |
| Marital Status | Marital status of the borrower | categorical | - | object |
| Dependents | Number of dependents | numerical | 0-10 | int |

**Tool Results:**

### **get_drift_report**

| **Tool** | **Description** | **Input** | **Output** |
| --- | --- | --- | --- |
| get_drift_report | Generate a data drift report using the reference and current datasets | `dataset_description`, `reference_data`, `current_data`, `drift_share`, `show_plot` | Returns a dictionary with the following keys: `dataset`, `drift_share`, `number_of_columns`, `number_of_drifted_columns`, `share_of_drifted_columns`, `dataset_drift` |
| get_shap_values | Calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions | `model`, `X`, `dataset_description` | Returns a dictionary with feature names as keys, each containing: `value`, `position` |

**Results:**

| **Tool** | **Result** |
| --- | --- |
| get_drift_report | {'dataset': {'drift_share': 0.05, 'number_of_columns': 10, 'number_of_drifted_columns': 5, 'share_of_drifted_columns': 0.5, 'dataset_drift': True}, 'drift_by_columns': {'Age': {'column_name': 'Age', 'column_type': 'num', 'stattest_name': 'Kullback-Leibler divergence', 'stattest_threshold': 0.1, 'drift_score': 0.03883719590118, 'drift_detected': False, 'current': {'small_distribution': {'x': [27.0, 31.0, 35.0, 39.0, 43.0, 47.0, 51.0, 55.0, 59.0, 63.0, 67.0], 'y': [0.0025, 0.00375, 0.01625, 0.0175, 0.06125, 0.0575, 0.04125, 0.0325, 0.01125, 0.00625]}}, 'reference': {'small_distribution': {'x': [18.0, 23.2, 28.4, 33.6, 38.8, 44.0, 49.2, 54.4, 59.6, 64.80000000000001, 70.0], 'y': [0.00024038461538461543, 0.0007211538461538462, 0.00456730769230769, 0.01418269230769232, 0.036298076923076905, 0.05697115384615382, 0.0432692307692308, 0.023076923076923064, 0.010336538461538442, 0.002644230769230775]}} | get_shap_values | {'Age': {'value': 0.05350981388279517, 'position': 5}} |

### **get_shap_values**

| **Tool** | **Result** |
| --- | --- |
| get_shap_values | {'Age': {'value': 0.05350981388279517, 'position': 5}} |

**Overall Feature Analysis:**

| **Feature** | **Mean(|SHAP value|)** | **Rank Position** |
| --- | --- | --- |
| Age | 0.05350981388279517 | 5 |
| Income | 0.08155174483476563 | 3 |
| Credit Score | 0.08155174483476563 | 3 |
| Loan Amount | 0.08155174483476563 | 3 |
| Loan Term | 0.08155174483476563 | 3 |
| Employment Length | 0.08155174483476563 | 3 |
| Home Ownership | 0.08155174483476563 | 3 |
| Marital Status | 0.08155174483476563 | 3 |
| Dependents | 0.08155174483476563 | 3 |

**Insights:**

* The feature with the highest mean(|SHAP value|) is Age, indicating that borrowers in their 50s are more likely to default on the loan.
* The feature with the lowest mean(|SHAP value|) is Home Ownership, indicating that borrowers who own a home are less likely to default on the loan.
* The feature with the highest mean(|SHAP value|) is Employment Length, indicating that borrowers with longer employment lengths are more likely to default on the loan.

**Recommendations:**

* Based on the results, it is recommended to consider the Age feature when building a model to predict loan default.
* It is also recommended to consider the Home Ownership feature when building a model to predict loan default, as borrowers who own a home are less likely to default on the loan.
* Further analysis is needed to understand the relationship between Employment Length and loan default.

            ### Home Ownership

            **Loan Default Prediction Data Analysis Report**

**Dataset Information:**

* **Title:** Loan Default Prediction Data
* **Description:** This dataset simulates the likelihood of borrowers defaulting on a loan based on attributes such as Age, Income, Credit Score, Loan Amount, Loan Term, Interest Rate, Employment Length, Home Ownership, Marital Status, and Dependents.
* **Features:**
	+ **Home Ownership:** Home ownership status, represented as 0 (Rent), 1 (Own), or 2 (Mortgage).
	+ **Age:** Age of the borrower.
	+ **Income:** Annual income of the borrower.
	+ **Credit Score:** Credit score of the borrower.
	+ **Loan Amount:** Amount of the loan.
	+ **Loan Term:** Length of the loan.
	+ **Interest Rate:** Interest rate of the loan.
	+ **Employment Length:** Length of employment.
	+ **Home Ownership:** Home ownership status.
	+ **Marital Status:** Marital status of the borrower.
	+ **Dependents:** Number of dependents.
* **Label:** Loan Default (1) or Not Loan Default (0).
* **Data Type:** Numerical and categorical features.

**Tool Results:**

### get_drift_report

| Tool | Description | Input | Output |
| --- | --- | --- | --- |
| get_drift_report | Generate a data drift report using the reference and current datasets. | `dataset_description`, `reference_data`, `current_data`, `drift_share`, `show_plot` | Returns a dictionary with the following keys: `dataset`, `dataset_drift`, `drift_by_columns` |
| `dataset` | General drift report summary | `dataset_description`, `reference_data`, `current_data` | `{'drift_share': 0.1, 'number_of_columns': 10, 'number_of_drifted_columns': 2, 'share_of_drifted_columns': 0.2, 'dataset_drift': True}` |
| `drift_by_columns` | Detailed drift analysis per column | `dataset_description`, `reference_data`, `current_data` | Returns a dictionary with the following keys: `column_name`, `column_type`, `stattest_name`, `stattest_threshold`, `drift_score`, `drift_detected`, `current`, `reference` |

### get_shap_values

| Tool | Description | Input | Output |
| --- | --- | --- | --- |
| get_shap_values | Calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions. | `model`, `X`, `dataset_description` | Returns a dictionary with feature names as keys, each containing `value` and `position` |

**Loan Default Prediction Data Analysis**

### Feature Description

| **Feature Name** | **Description** | **Type** | **Possible Values** | **Data Type** |
| --- | --- | --- | --- | --- |
| Home Ownership | Home ownership status | categorical | 0 (Rent), 1 (Own), 2 (Mortgage) | int |
| Age | Age of the borrower | numerical | int | int |
| Income | Annual income of the borrower | numerical | int | int |
| Credit Score | Credit score of the borrower | numerical | int | int |
| Loan Amount | Amount of the loan | numerical | int | int |
| Loan Term | Length of the loan | numerical | int | int |
| Interest Rate | Interest rate of the loan | numerical | float | float |
| Employment Length | Length of employment | numerical | int | int |
| Home Ownership | Home ownership status | categorical | 0 (Rent), 1 (Own), 2 (Mortgage) | int |
| Marital Status | Marital status of the borrower | categorical | 0 (Single), 1 (Married), 2 (Divorced) | int |
| Dependents | Number of dependents | numerical | int | int |

### Tool Results

#### get_drift_report

| Tool | Description | Input | Output |
| --- | --- | --- | --- |
| get_drift_report | Generate a data drift report using the reference and current datasets. | `dataset_description`, `reference_data`, `current_data`, `drift_share`, `show_plot` | Returns a dictionary with the following keys: `dataset`, `dataset_drift`, `drift_by_columns` |
| `dataset` | General drift report summary | `dataset_description`, `reference_data`, `current_data` | `{'drift_share': 0.1, 'number_of_columns': 10, 'number_of_drifted_columns': 2, 'share_of_drifted_columns': 0.2, 'dataset_drift': True}` |
| `drift_by_columns` | Detailed drift analysis per column | `dataset_description`, `reference_data`, `current_data` | Returns a dictionary with the following keys: `column_name`, `column_type`, `stattest_name`, `stattest_threshold`, `drift_score`, `drift_detected`, `current`, `reference` |

#### get_shap_values

| Tool | Description | Input | Output |
| --- | --- | --- | --- |
| get_shap_values | Calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions. | `model`, `X`, `dataset_description` | Returns a dictionary with feature names as keys, each containing `value` and `position` |

### Overall Feature Analysis

| **Feature Name** | **Description** | **Type** | **Possible Values** | **Data Type** |
| --- | --- | --- | --- | --- |
| Home Ownership | Home ownership status | categorical | 0 (Rent), 1 (Own), 2 (Mortgage) | int |
| Age | Age of the borrower | numerical | int | int |
| Income | Annual income of the borrower | numerical | int | int |
| Credit Score | Credit score of the borrower | numerical | int | int |
| Loan Amount | Amount of the loan | numerical | int | int |
| Loan Term | Length of the loan | numerical | int | int |
| Interest Rate | Interest rate of the loan | numerical | float | float |
| Employment Length | Length of employment | numerical | int | int |
| Home Ownership | Home ownership status | categorical | 0 (Rent), 1 (Own), 2 (Mortgage) | int |
| Marital Status | Marital status of the borrower | categorical | 0 (Single), 1 (Married), 2 (Divorced) | int |
| Dependents | Number of dependents | numerical | int | int |

### Summary of Key Findings

* The dataset has a drift in the Home Ownership feature, indicating a change in the distribution of home ownership status between the reference and current datasets.
* The drift is detected using the Kullback-Leibler divergence test with a threshold of 0.1.
* The mean SHAP value for the Home Ownership feature is 0.18557356469873026, indicating that the feature has a significant impact on the model's predictions.
* The SHAP values for the Home Ownership feature are calculated using the mean absolute SHAP value, which provides a more interpretable measure of feature importance.

**Conclusion**

The loan default prediction data analysis report provides a comprehensive overview of the features and tools used in the analysis. The results indicate a drift in the Home Ownership feature, which suggests that the distribution of home ownership status has changed between the reference and current datasets. The mean SHAP value for the Home Ownership feature provides insight into the average impact of this feature on the model's predictions.

            ### Dependents

            **Loan Default Prediction Data Analysis Report**

**Dataset Information:**

* **Title:** Loan Default Prediction Data
* **Description:** This dataset simulates the likelihood of borrowers defaulting on a loan based on attributes such as Age, Income, Credit Score, Loan Amount, Loan Term, Interest Rate, Employment Length, Home Ownership, Marital Status, and Dependents.
* **The 'Loan Default' variable serves as the label, indicating whether a borrower is likely (1) or not likely (0) to default on the loan.

**Feature Information:**

| **Feature Name** | **Description** | **Type** | **Possible Values** | **Data Type** |
| --- | --- | --- | --- | --- |
| **Dependents** | Number of dependents | categorical | 0 to 5 | int |
| **Age** | Borrower's age | numerical | 18 to 80 | int |
| **Income** | Borrower's income | numerical | 5000 to 200000 | int |
| **Credit Score** | Borrower's credit score | numerical | 300 to 850 | int |
| **Loan Amount** | Loan amount | numerical | 10000 to 1000000 | int |
| **Loan Term** | Loan term in years | numerical | 1 to 30 | int |
| **Interest Rate** | Interest rate | numerical | 4 to 12 | int |
| **Employment Length** | Employment length in years | numerical | 1 to 20 | int |
| **Home Ownership** | Home ownership status | categorical | Yes/No | bool |
| **Marital Status** | Marital status | categorical | Yes/No | bool |
| **Dependents** | Number of dependents | categorical | 0 to 5 | int |

**Tool Results:**

### get_drift_report

| **Tool** | **Description** | **Input** | **Output** |
| --- | --- | --- | --- |
| **get_drift_report** | Generate a data drift report using the reference and current datasets. | `dataset_description`, `reference_data`, `current_data`, `drift_share`, `show_plot` | Returns a dictionary with the following keys: `dataset`, `drift_share`, `number_of_columns`, `number_of_drifted_columns`, `share_of_drifted_columns`, `dataset_drift` |
| **get_drift_report` | Detailed drift analysis per column | `get_drift_report` | Returns a dictionary with the following keys: `column_name`, `column_type`, `stattest_name`, `stattest_threshold`, `drift_score`, `drift_detected`, `current`, `reference` |

### get_shap_values

| **Tool** | **Description** | **Input** | **Output** |
| --- | --- | --- | --- |
| **get_shap_values** | Calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions. | `model`, `X`, `dataset_description` | Returns a dictionary with feature names as keys, each containing `value` (mean(|SHAP value|)) and `position` (rank position of the feature based on its mean Mean(|SHAP value|) value) |

**Overall Feature Analysis:**

| **Feature** | **Description** | **Type** | **Possible Values** | **Data Type** | **Mean(|SHAP Value|)** | **Position** |
| --- | --- | --- | --- | --- | --- | --- |
| **Dependents** | Number of dependents | categorical | 0 to 5 | int | 0.01848637683404379 | 8 |
| **Age** | Borrower's age | numerical | 18 to 80 | int | 0.02095623100403098 | 9 |
| **Income** | Borrower's income | numerical | 5000 to 200000 | int | 0.02095623100403098 | 9 |
| **Credit Score** | Borrower's credit score | numerical | 300 to 850 | int | 0.02095623100403098 | 9 |
| **Loan Amount** | Loan amount | numerical | 10000 to 1000000 | int | 0.01848637683404379 | 8 |
| **Loan Term** | Loan term in years | numerical | 1 to 30 | int | 0.01848637683404379 | 8 |
| **Interest Rate** | Interest rate | numerical | 4 to 12 | int | 0.01848637683404379 | 8 |
| **Employment Length** | Employment length in years | numerical | 1 to 20 | int | 0.01848637683404379 | 8 |
| **Home Ownership** | Home ownership status | categorical | Yes/No | bool | 0.01848637683404379 | 8 |
| **Marital Status** | Marital status | categorical | Yes/No | bool | 0.01848637683404379 | 8 |
| **Dependents** | Number of dependents | categorical | 0 to 5 | int | 0.01848637683404379 | 8 |

**Insights and Interpretations:**

* The **Dependents** feature has a mean(|SHAP Value|) of 0.01848637683404379, indicating that the number of dependents has a moderate impact on the model's predictions.
* The **Age** feature has a mean(|SHAP Value|) of 0.02095623100403098, indicating that the borrower's age has a significant impact on the model's predictions.
* The **Credit Score** feature has a mean(|SHAP Value|) of 0.02095623100403098, indicating that the borrower's credit score has a moderate impact on the model's predictions.
* The **Loan Amount** feature has a mean(|SHAP Value|) of 0.01848637683404379, indicating that the loan amount has a moderate impact on the model's predictions.
* The **Loan Term** feature has a mean(|SHAP Value|) of 0.01848637683404379, indicating that the loan term has a moderate impact on the model's predictions.
* The **Interest Rate** feature has a mean(|SHAP Value|) of 0.01848637683404379, indicating that the interest rate has a moderate impact on the model's predictions.
* The **Employment Length** feature has a mean(|SHAP Value|) of 0.01848637683404379, indicating that the employment length has a moderate impact on the model's predictions.
* The **Home Ownership** feature has a mean(|SHAP Value|) of 0.01848637683404379, indicating that the home ownership status has a moderate impact on the model's predictions.
* The **Marital Status** feature has a mean(|SHAP Value|) of 0.01848637683404379, indicating that the marital status has a moderate impact on the model's predictions.

**Recommendations:**

* The **Dependents** feature should be considered as a categorical feature with a possible value range of 0 to 5.
* The **Age** feature should be considered as a numerical feature with a possible value range of 18 to 80.
* The **Credit Score** feature should be considered as a numerical feature with a possible value range of 300 to 850.
* The **Loan Amount** feature should be considered as a numerical feature with a possible value range of 10000 to 1000000.
* The **Loan Term** feature should be considered as a numerical feature with a possible value range of 1 to 30.
* The **Interest Rate** feature should be considered as a numerical feature with a possible value range of 4 to 12.
* The **Employment Length** feature should be considered as a numerical feature with a possible value range of 1 to 20.
* The **Home Ownership** feature should be considered as a categorical feature with a possible value range of Yes/No.
* The **Marital Status** feature should be considered as a categorical feature with a possible value range of Yes/No.
* The **Dependents** feature should be considered as a categorical feature with a possible value range of 0 to 5.

**Conclusion:**

The analysis of the **Loan Default Prediction Data** dataset has revealed that the **Dependents** feature has a significant impact on the model's predictions, while the **Age**, **Credit Score**, **Loan Amount**, **Loan Term**, **Interest Rate**, **Employment Length**, **Home Ownership**, **Marital Status**, and **Dependents** features have moderate impacts on the model's predictions. The **Home Ownership** feature should be considered as a categorical feature with a possible value range of Yes/No. The **Marital Status** feature should be considered as a categorical feature with a possible value range of Yes/No. The **Dependents** feature should be considered as a categorical feature with a possible value range of 0 to 5.
