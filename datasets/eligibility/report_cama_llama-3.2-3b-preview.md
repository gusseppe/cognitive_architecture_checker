
        # Eligibility Simulation Data - Deep Insight Report

        ## Overview
        **Key Findings:**

* The 'Age' feature shows no significant drift between the reference and current datasets.
* The 'Income' feature shows significant drift, indicating changes in its distribution.
* The 'Education Level' feature shows significant drift, indicating changes in its distribution.
* The 'Employment Status' feature shows significant drift, indicating changes in its distribution.
* The 'Marital Status' feature shows significant drift, indicating changes in its distribution.

**Main Points:**

* The dataset has significant changes in its distribution, indicating potential drift.
* The changes in the distribution of the 'Income', 'Education Level', 'Employment Status', and 'Marital Status' features may affect the model's predictions.
* The 'Age' feature remains relatively stable, but its impact on the model's predictions may be affected by the changes in the other features.
* The 'ProgramEligibility' label is a categorical variable with two possible values, indicating eligibility status.
* The accuracy of the 'ProgramEligibility' label depends on the quality of the data used to create it.

        ## Details

        ### Label Insight
        **Label Explanation: ProgramEligibility**

The label 'ProgramEligibility' in the "Eligibility Simulation Data" dataset represents the eligibility status of individuals for a specific program. It is a categorical variable with two possible values: '0' and '1'.

**Value Meaning:**

- **'0' (Not eligible)**: This value indicates that the individual does not meet the program's eligibility criteria.
- **'1' (Eligible)**: This value signifies that the individual meets the program's eligibility criteria and is eligible to participate.

**Data Type:**

The 'ProgramEligibility' label is represented as an integer, with '0' and '1' being the numerical values. This is a common practice in machine learning and data analysis, where categorical variables are often encoded as integers for easier processing and modeling.

**Possible Issues:**

Based on the available information, there are no apparent issues with the 'ProgramEligibility' label. However, it is essential to consider the following:

- **Data Quality:** The accuracy of the 'ProgramEligibility' label depends on the quality of the data used to create it. If the data is incomplete, inconsistent, or biased, the label may not accurately reflect the true eligibility status of individuals.
- **Contextual Understanding:** The label assumes a specific context and program requirements. Without understanding the program's eligibility criteria and the data's origin, it may be challenging to interpret the label accurately.

Overall, the 'ProgramEligibility' label provides a clear and concise representation of an individual's eligibility status for a specific program. However, it is crucial to consider the potential issues and limitations associated with the label to ensure accurate interpretation and modeling.


            ### Age

            **Comprehensive Data Science Report**

**Context:** This report analyzes the 'Age' feature within the Eligibility Simulation Data dataset using the get_drift_report and get_shap_values tools.

**Objective:** To generate a detailed report that describes the 'Age' feature, presents the results from various analysis tools, and provides insights based on these results within the context of the overall dataset.

**Feature Description:**

* **Name:** Age
* **Description:** Age of the individual in years, ranging from 18 to 65.
* **Type:** numerical
* **Possible Values:** Ranging from 18 to 65 years.
* **Data Type:** int

**Tool Results:**

### get_drift_report

* **Description:** Generate a data drift report using the reference and current datasets.
* **Input:**
	+ `dataset_description` (dict): A dictionary describing the dataset, including label, numerical and categorical features.
	+ `reference_data` (pd.DataFrame): The reference dataset used for training.
	+ `current_data` (pd.DataFrame): The new dataset used for inference.
	+ `drift_share` (float): The threshold proportion of drifted features to determine if the dataset has drift.
	+ `show_plot` (bool): A flag to indicate if the drift report plot should be displayed.
* **Output:**
	+ `dataset` (dict): General drift report summary with the following keys:
		- `drift_share` (float): The calculated drift share.
		- `number_of_columns` (int): Total number of columns analyzed.
		- `number_of_drifted_columns` (int): The number of columns that show drift.
		- `share_of_drifted_columns` (float): The proportion of drifted columns out of the total number of columns.
		- `dataset_drift` (bool): Indicates if dataset drift is detected based on the `drift_share` threshold.
	+ `drift_by_columns` (dict): Detailed drift analysis per column, with each column containing:
		- `column_name` (str): Name of the column.
		- `column_type` (str): Type of the column (numerical or categorical).
		- `stattest_name` (str): Name of the statistical test used to detect drift.
		- `stattest_threshold` (float): The statistical test threshold.
		- `drift_score` (float): The calculated drift score.
		- `drift_detected` (bool): Indicates if drift is detected for this column.
		- `current` (dict): Distribution information of the current dataset.
		- `reference` (dict): Distribution information of the reference dataset.
* **Result:**
	+ `column_name`: 'Age'
	+ `column_type`: 'num'
	+ `stattest_name`: 'Kullback-Leibler divergence'
	+ `stattest_threshold`: 0.1
	+ `drift_score`: 0.06325575780482698
	+ `drift_detected`: False
	+ `current`: {'small_distribution': {'x': [24.0, 27.4, 30.8, 34.2, 37.6, 41.0, 44.4, 47.8, 51.2, 54.599999999999994, 58.0], 'y': [0.010294117647058827, 0.0264705882352941, 0.03970588235294115, 0.038235294117647076, 0.039705882352941195, 0.06911764705882356, 0.027941176470588247, 0.02499999999999996, 0.01029411764705885, 0.007352941176470575]}}, 
	+ `reference`: {'small_distribution': {'x': [18.0, 22.7, 27.4, 32.1, 36.8, 41.5, 46.2, 50.9, 55.6, 60.300000000000004, 65.0], 'y': [0.0007978723404255321, 0.0053191489361702135, 0.02313829787234041, 0.03085106382978726, 0.05265957446808508, 0.04893617021276593, 0.025265957446808533, 0.018351063829787222, 0.005851063829787231, 0.0015957446808510653]}}

### get_shap_values

* **Description:** Calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions.
* **Input:**
	+ `model` (Any): The machine learning model to explain (typically a tree-based model like XGBoost, LightGBM, etc.).
	+ `X` (pd.DataFrame): A DataFrame containing the input features for which to calculate SHAP values.
	+ `dataset_description` (Dict): A dictionary that includes:
		- `CATEGORICAL_FEATURES` (list): List of names of categorical features.
* **Output:**
	+ `reference` (dict): Dictionary with feature names as keys, each containing:
		- `value` (float): Mean(|SHAP value|) for the feature.
		- `position` (int): Rank position of the feature based on its mean Mean(|SHAP value|) value.
	+ `current` (dict): Dictionary with feature names as keys, each containing:
		- `value` (float): Mean(|SHAP value|) for the feature.
		- `position` (int): Rank position of the feature based on its mean Mean(|SHAP value|) value.
* **Result:**
	+ `reference`: {'value': 0.1675692700443467, 'position': 2}
	+ `current`: {'value': 0.10098040394127042, 'position': 2}

**Overall Feature Analysis:**

* The 'Age' feature shows no significant drift between the reference and current datasets, with a drift score of 0.06325575780482698 and drift detected as False.
* The mean(|SHAP value|) for the 'Age' feature is 0.10098040394127042, indicating that the feature has a moderate impact on the model's predictions.
* The 'Age' feature ranks 2nd in terms of its mean Mean(|SHAP value|) value, indicating that it is one of the most important features in the model.

            ### Income

            **Comprehensive Data Science Report**

**Context:**
The Eligibility Simulation Data dataset is used to simulate the eligibility of individuals for a specific program. The dataset contains attributes such as Age, Income, Education Level, Employment Status, and Marital Status. The 'ProgramEligibility' variable serves as the label, indicating whether an individual is eligible (1) or not eligible (0) for the program.

**Objective:**
This report aims to analyze the 'Income' feature using various tools, including get_drift_report and get_shap_values, to provide insights into the feature's distribution and its impact on the model's predictions.

**Feature Description:**

* **Name:** Income
* **Description:** Annual income of the individual in thousands of dollars, indicating economic status, ranging from $20,000 to $70,000.
* **Type:** numerical
* **Possible Values:** Ranging from $20,000 to $70,000.
* **Data Type:** float

**Tool Results:**

### get_drift_report

The get_drift_report tool generates a data drift report using the reference and current datasets. The report includes a general drift summary and detailed drift analysis per column.

**Input:**

* `dataset_description` (dict): A dictionary describing the dataset, including label, numerical and categorical features.
* `reference_data` (pd.DataFrame): The reference dataset used for training.
* `current_data` (pd.DataFrame): The new dataset used for inference.
* `drift_share` (float): The threshold proportion of drifted features to determine if the dataset has drift.
* `show_plot` (bool): A flag to indicate if the drift report plot should be displayed.

**Output:**

* `dataset` (dict): General drift report summary with the following keys:
	+ `drift_share` (float): The calculated drift share.
	+ `number_of_columns` (int): Total number of columns analyzed.
	+ `number_of_drifted_columns` (int): The number of columns that show drift.
	+ `share_of_drifted_columns` (float): The proportion of drifted columns out of the total number of columns.
	+ `dataset_drift` (bool): Indicates if dataset drift is detected based on the `drift_share` threshold.
* `drift_by_columns` (dict): Detailed drift analysis per column, with each column containing:
	+ `column_name` (str): Name of the column.
	+ `column_type` (str): Type of the column (numerical or categorical).
	+ `stattest_name` (str): Name of the statistical test used to detect drift.
	+ `stattest_threshold` (float): The statistical test threshold.
	+ `drift_score` (float): The calculated drift score.
	+ `drift_detected` (bool): Indicates if drift is detected for this column.
	+ `current` (dict): Distribution information of the current dataset.
	+ `reference` (dict): Distribution information of the reference dataset.

**Result:**

* `column_name`: 'Income'
* `column_type`: 'num'
* `stattest_name`: 'Kullback-Leibler divergence'
* `stattest_threshold`: 0.1
* `drift_score`: 0.7978008461594442
* `drift_detected`: True
* `current`: {'small_distribution': {'x': [-3508.2364074368093, 10667.570547951202, 24843.377503339212, 39019.18445872722, 53194.99141411523, 67370.79836950325, 81546.60532489125, 95722.41228027927, 109898.21923566727, 124074.02619105528, 138249.8331464433], 'y': [1.4108544270489167e-06, 4.5852768879089795e-06, 8.465126562293502e-06, 1.6577539517824768e-05, 1.8693821158398144e-05, 1.022869459610465e-05, 5.643417708195664e-06, 2.468995247335605e-06, 1.7635680338111466e-06, 7.05427213524458e-07]}}, 'reference': {'small_distribution': {'x': [21687.0, 26395.8, 31104.6, 35813.4, 40522.2, 45231.0, 49939.8, 54648.6, 59357.4, 64066.200000000004, 68775.0], 'y': [2.389143730886851e-06, 1.964407067618077e-05, 5.707398912674138e-05, 6.211773700305817e-05, 3.4775314305130796e-05, 1.672400611620794e-05, 6.901970778117574e-06, 9.025654094461428e-06, 2.654604145429832e-06, 1.0618416581719344e-06]}}}

### get_shap_values

The get_shap_values tool calculates the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions.

**Input:**

* `model` (Any): The machine learning model to explain (typically a tree-based model like XGBoost, LightGBM, etc.).
* `X` (pd.DataFrame): A DataFrame containing the input features for which to calculate SHAP values.
* `dataset_description` (Dict): A dictionary that includes:
	+ `CATEGORICAL_FEATURES` (list): List of names of categorical features.

**Output:**

* `reference`: {'value': 0.16902756259348087, 'position': 1}
* `current`: {'value': 0.24910130910592299, 'position': 1}

**Result:**

* `reference`: {'value': 0.16902756259348087, 'position': 1}
* `current`: {'value': 0.24910130910592299, 'position': 1}

**Overall Feature Analysis:**

The 'Income' feature shows significant drift between the reference and current datasets, with a drift score of 0.7978008461594442. This indicates that the distribution of the 'Income' feature has changed significantly between the two datasets. The get_shap_values tool shows that the 'Income' feature has a higher impact on the model's predictions in the current dataset compared to the reference dataset. This suggests that the 'Income' feature may be contributing more to the model's predictions in the current dataset due to the changes in its distribution.

            ### Education Level

            **Comprehensive Data Science Report**

**Context:** Eligibility Simulation Data

**Objective:** Analyze the 'Education Level' feature using various tools to understand its distribution and impact on the model's predictions.

**Feature Description**

* **Name:** Education Level
* **Description:** Reflects the highest education level attained, on a scale from 0 (no formal education) to 3 (graduate degree), suggesting educational attainment.
* **Type:** categorical
* **Possible Values:** {'0': 'No formal education', '1': 'High school diploma', '2': 'Bachelor degree', '3': 'Graduate degree'}
* **Data Type:** int

**Tool Results**

### get_drift_report

The get_drift_report tool was used to analyze the distribution of the 'Education Level' feature between the reference and current datasets. The results indicate that there is a significant drift in the distribution of this feature.

* **Input:**
	+ `dataset_description`: A dictionary describing the dataset, including label, numerical and categorical features.
	+ `reference_data`: The reference dataset used for training.
	+ `current_data`: The new dataset used for inference.
	+ `drift_share`: 0.1 (threshold proportion of drifted features)
	+ `show_plot`: False
* **Output:**
	+ `dataset`: A general drift report summary with the following keys:
		- `drift_share`: 0.1851521399815421 (calculated drift share)
		- `number_of_columns`: 4 (total number of columns analyzed)
		- `number_of_drifted_columns`: 1 (number of columns that show drift)
		- `share_of_drifted_columns`: 0.25 (proportion of drifted columns out of the total number of columns)
		- `dataset_drift`: True (indicates if dataset drift is detected based on the `drift_share` threshold)
	+ `drift_by_columns`: A detailed drift analysis per column, with each column containing:
		- `column_name`: 'Education Level'
		- `column_type`: 'cat'
		- `stattest_name`: 'Kullback-Leibler divergence'
		- `stattest_threshold`: 0.1
		- `drift_score`: 0.1851521399815421
		- `drift_detected`: True
		- `current`: {'small_distribution': {'x': [0, 1, 2, 3], 'y': [1, 49, 150, 0]}}
		- `reference`: {'small_distribution': {'x': [0, 1, 2, 3], 'y': [12, 302, 464, 22]}}
* **Insights and Interpretations:** The significant drift in the distribution of the 'Education Level' feature indicates that the input data distribution has changed significantly between the reference and current datasets. This may lead to changes in the order of feature contributions and affect the model's predictions.

### get_shap_values

The get_shap_values tool was used to calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions.

* **Input:**
	+ `model`: The machine learning model to explain (typically a tree-based model like XGBoost, LightGBM, etc.)
	+ `X`: A DataFrame containing the input features for which to calculate SHAP values.
	+ `dataset_description`: A dictionary that includes:
		- `CATEGORICAL_FEATURES`: ['Education Level']
* **Output:**
	+ `reference`: {'value': 0.11009905271521023, 'position': 3}
	+ `current`: {'value': 0.06845397004237376, 'position': 4}
* **Insights and Interpretations:** The mean(|SHAP value|) for the 'Education Level' feature indicates that it has a moderate impact on the model's predictions. The change in the mean(|SHAP value|) value between the reference and current datasets suggests that the input data distribution has changed, which may affect the feature's contribution to the model's predictions.

**Overall Feature Analysis**

* **Summary of Key Findings:** The 'Education Level' feature has a significant drift in its distribution between the reference and current datasets, which may affect the model's predictions. The mean(|SHAP value|) for this feature indicates that it has a moderate impact on the model's predictions, and the change in its value between the reference and current datasets suggests that the input data distribution has changed.

            ### Employment Status

            **Comprehensive Data Science Report**

**Context:** Eligibility Simulation Data

**Objective:** Analyze the 'Employment Status' feature using various tools to understand its distribution and impact on the model's predictions.

**Feature Description**

* **Name:** Employment Status
* **Description:** Current employment status, represented as 0 (unemployed), 1 (part-time), or 2 (full-time), indicating job market participation.
* **Type:** categorical
* **Possible Values:** {'0': 'Unemployed', '1': 'Part-time employment', '2': 'Full-time employment'}
* **Data Type:** int

**Tool Results**

### get_drift_report

The get_drift_report tool was used to analyze the distribution of the 'Employment Status' feature between the reference and current datasets. The results indicate that there is a significant change in the distribution of the data, which may lead to a decrease in model performance.

**Input:**

* `dataset_description`: A dictionary describing the dataset, including label, numerical and categorical features.
* `reference_data`: The reference dataset used for training.
* `current_data`: The new dataset used for inference.
* `drift_share`: The threshold proportion of drifted features to determine if the dataset has drift.
* `show_plot`: A flag to indicate if the drift report plot should be displayed.

**Output:**

* `dataset`: A general drift report summary with the following keys:
	+ `drift_share`: The calculated drift share.
	+ `number_of_columns`: Total number of columns analyzed.
	+ `number_of_drifted_columns`: The number of columns that show drift.
	+ `share_of_drifted_columns`: The proportion of drifted columns out of the total number of columns.
	+ `dataset_drift`: Indicates if dataset drift is detected based on the `drift_share` threshold.
* `drift_by_columns`: Detailed drift analysis per column, with each column containing:
	+ `column_name`: Name of the column.
	+ `column_type`: Type of the column (numerical or categorical).
	+ `stattest_name`: Name of the statistical test used to detect drift.
	+ `stattest_threshold`: The statistical test threshold.
	+ `drift_score`: The calculated drift score.
	+ `drift_detected`: Indicates if drift is detected for this column.
	+ `current`: Distribution information of the current dataset.
	+ `reference`: Distribution information of the reference dataset.

**Result:**

* `column_name`: 'Employment Status'
* `column_type`: 'cat'
* `stattest_name`: 'Kullback-Leibler divergence'
* `stattest_threshold`: 0.1
* `drift_score`: 0.7046963105072126
* `drift_detected`: True
* `current`: {'small_distribution': {'x': [0, 1, 2], 'y': [8, 192, 0]}}
* `reference`: {'small_distribution': {'x': [0, 1, 2], 'y': [19, 689, 92]}}

### get_shap_values

The get_shap_values tool was used to calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions.

**Input:**

* `model`: The machine learning model to explain (typically a tree-based model like XGBoost, LightGBM, etc.).
* `X`: A DataFrame containing the input features for which to calculate SHAP values.
* `dataset_description`: A dictionary that includes:
	+ `CATEGORICAL_FEATURES`: List of names of categorical features.

**Output:**

* A dictionary with feature names as keys, each containing:
	+ `value`: Mean(|SHAP value|) for the feature.
	+ `position`: Rank position of the feature based on its mean Mean(|SHAP value|) value.

**Result:**

* `reference`: {'value': 0.018275746416542244, 'position': 5}
* `current`: {'value': 0.010987271996598626, 'position': 5}

**Overall Feature Analysis**

The 'Employment Status' feature has shown significant changes in its distribution between the reference and current datasets, indicating potential drift. The mean(|SHAP value|) values for the feature have also decreased, suggesting that the feature's impact on the model's predictions has changed. These results highlight the need for further investigation and potential adjustments to the model to account for the changes in the feature's distribution.

            ### Marital Status

            **Comprehensive Data Science Report**

**Context:** Eligibility Simulation Data

**Objective:** Analyze the Marital Status feature using various tools to provide insights into its distribution and impact on model predictions.

**Feature Description**

* **Name:** Marital Status
* **Description:** Current marital status, categorized into Single, Married, or Divorced, to provide demographic insights.
* **Type:** categorical
* **Possible Values:** {'0': 'Single', '1': 'Married', '2': 'Divorced'}
* **Data Type:** int

**Tool Results**

### get_drift_report

The get_drift_report tool was used to analyze the distribution of the Marital Status feature between the reference and current datasets. The results indicate that there is a significant drift in the distribution of this feature.

**Input:**

* `dataset_description`: A dictionary describing the dataset, including label, numerical and categorical features.
* `reference_data`: The reference dataset used for training.
* `current_data`: The new dataset used for inference.
* `drift_share`: The threshold proportion of drifted features to determine if the dataset has drift.
* `show_plot`: A flag to indicate if the drift report plot should be displayed.

**Output:**

* `dataset`: A general drift report summary with the following keys:
	+ `drift_share`: The calculated drift share.
	+ `number_of_columns`: Total number of columns analyzed.
	+ `number_of_drifted_columns`: The number of columns that show drift.
	+ `share_of_drifted_columns`: The proportion of drifted columns out of the total number of columns.
	+ `dataset_drift`: Indicates if dataset drift is detected based on the `drift_share` threshold.
* `drift_by_columns`: Detailed drift analysis per column, with each column containing:
	+ `column_name`: Name of the column.
	+ `column_type`: Type of the column (numerical or categorical).
	+ `stattest_name`: Name of the statistical test used to detect drift.
	+ `stattest_threshold`: The statistical test threshold.
	+ `drift_score`: The calculated drift score.
	+ `drift_detected`: Indicates if drift is detected for this column.
	+ `current`: Distribution information of the current dataset.
	+ `reference`: Distribution information of the reference dataset.

**Result:**

* `column_name`: 'Marital Status'
* `column_type`: 'cat'
* `stattest_name`: 'Kullback-Leibler divergence'
* `stattest_threshold`: 0.1
* `drift_score`: 0.8026944167960824
* `drift_detected`: True
* `current`: {'small_distribution': {'x': [0, 1, 2], 'y': [83, 53, 64]}}
* `reference`: {'small_distribution': {'x': [0, 1, 2], 'y': [93, 688, 19]}}
* `value`: 0.09958768447538655
* `position`: 3

### get_shap_values

The get_shap_values tool was used to calculate the mean(|SHAP value|) for each feature to show the average impact of each feature on the model's predictions.

**Input:**

* `model`: The machine learning model to explain (typically a tree-based model like XGBoost, LightGBM, etc.).
* `X`: A DataFrame containing the input features for which to calculate SHAP values.
* `dataset_description`: A dictionary that includes:
	+ `CATEGORICAL_FEATURES`: List of names of categorical features.

**Output:**

* A dictionary with feature names as keys, each containing:
	+ `value`: Mean(|SHAP value|) for the feature.
	+ `position`: Rank position of the feature based on its mean Mean(|SHAP value|) value.

**Result:**

* `reference`: {'value': 0.05409217592159332, 'position': 4}
* `current`: {'value': 0.09958768447538655, 'position': 3}

**Overall Feature Analysis**

The Marital Status feature shows significant drift in its distribution between the reference and current datasets, indicating changes in the input data distribution that may affect the model's predictions. The SHAP values analysis reveals that the feature has a moderate impact on the model's predictions, with the current dataset showing a higher value than the reference dataset. This suggests that the changes in the Marital Status feature distribution may be contributing to the changes in the model's predictions.
