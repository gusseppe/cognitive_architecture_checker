
        # Loan Default Prediction Data - Deep Insight Report

        ## Overview
        Here's a brief overview of the key findings and main points:

* **Age**: No significant drift in the distribution of ages between the reference and current datasets.
* **Income**: Significant drift in the distribution of income values, with a higher mean(|SHAP value|) in the current dataset.
* **Credit Score**: No significant drift in the distribution of credit scores between the reference and current datasets.
* **Loan Amount**: No significant drift in the distribution of loan amounts between the reference and current datasets.
* **Loan Term**: No significant drift in the distribution of loan terms between the reference and current datasets.
* **Interest Rate**: Significant drift in the distribution of interest rates, with a higher drift score in the current dataset.
* **Employment Length**: Significant drift in the distribution of employment lengths, with a higher drift score in the current dataset.
* **Home Ownership**: Significant drift in the distribution of home ownership statuses, with a higher drift score in the current dataset.
* **Marital Status**: Significant drift in the distribution of marital statuses, with a higher drift score in the current dataset.
* **Dependents**: Significant drift in the distribution of dependents, with a higher drift score in the current dataset.
* **Label**: No issues with the label 'Loan Default', with no apparent changes in its distribution between the reference and current datasets.

        ## Details

        ### Label Insight
        **Label Explanation: Loan Default**

The label 'Loan Default' is a categorical variable used to indicate the likelihood of a borrower defaulting on a loan. This label is a binary classification, meaning it has two possible values: 0 and 1.

**Value Interpretation:**

- **Value 0 (No default):** This value represents a borrower who is not likely to default on the loan. In other words, the borrower has a low risk of defaulting.
- **Value 1 (Default):** This value represents a borrower who is likely to default on the loan. In other words, the borrower has a high risk of defaulting.

**Data Type:**

The label 'Loan Default' is an integer, denoted by the 'data_type' field as 'int'. This indicates that the label is a numerical value, where 0 and 1 are used to represent the two possible outcomes.

**Possible Values:**

The label 'Loan Default' has two possible values: 0 and 1. These values are explicitly defined in the 'possible_values' field, where 0 corresponds to 'No default' and 1 corresponds to 'Default'.

**Categorical Nature:**

Although the label 'Loan Default' is an integer, it is classified as a categorical variable due to its binary nature. This means that the label is treated as a category or a class, rather than a continuous numerical value.

**No Issues:**

Based on the provided information, there are no apparent issues with the label 'Loan Default'. The label clearly indicates the likelihood of loan default, and its binary nature makes it suitable for binary classification models.


            ### Age

            **Feature 'Age' Analysis**

The 'Age' feature is a numerical feature representing the age of the borrower in years, ranging from 18 to 70. 

**Distribution Analysis**

The distribution of the 'Age' feature in the reference dataset is represented by a small distribution, which shows the probability density of the ages in the dataset. The x-axis represents the ages, and the y-axis represents the corresponding probabilities.

In the reference dataset, the ages range from 18 to 70, with a peak at 59.6 years. The distribution is skewed to the right, indicating that most borrowers are older.

In the current dataset, the distribution of the 'Age' feature is also represented by a small distribution, which shows the probability density of the ages in the current dataset. The x-axis represents the ages, and the y-axis represents the corresponding probabilities.

The current distribution is similar to the reference distribution, but with some differences. The peak of the distribution has shifted slightly to the right, indicating that the current dataset has a slightly older population.

**Drift Analysis**

The 'get_drift_report' tool was used to analyze the drift of the 'Age' feature between the reference and current datasets. The result shows that the drift score is 0.03883719590118, which is below the threshold of 0.1. This indicates that the distribution of the 'Age' feature has not changed significantly between the reference and current datasets.

The 'drift_detected' flag is set to False, indicating that no drift is detected for the 'Age' feature.

**SHAP Values**

The 'get_shap_values' tool was used to calculate the mean(|SHAP value|) for the 'Age' feature. The result shows that the mean(|SHAP value|) for the 'Age' feature is 0.05350981388279517, which is lower than the mean(|SHAP value|) for the reference dataset (0.08155174483476563).

The 'position' of the 'Age' feature is 5, indicating that it is the 5th most important feature in terms of its contribution to the model's predictions.

            ### Income

            **Feature 'Income' Analysis**

The 'Income' feature represents the annual income of the borrower in dollars, ranging from $20,000 to $150,000. It is a numerical feature with a data type of float.

**Drift Analysis**

The 'get_drift_report' tool indicates that the 'Income' feature has drifted, with a drift score of 0.130772018665271. This suggests that the distribution of income values in the current dataset has changed significantly compared to the reference dataset. The Kullback-Leibler divergence statistical test was used to detect drift, with a threshold of 0.1.

**Distribution Information**

The current distribution of 'Income' values is represented by a small distribution, which shows the 10 most frequent values. The reference distribution is also shown, with a similar but not identical set of values.

**SHAP Values**

The 'get_shap_values' tool calculates the mean(|SHAP value|) for the 'Income' feature, which represents the average impact of this feature on the model's predictions. The current value is 0.1676025103420878, indicating that the 'Income' feature has a moderate impact on the model's predictions. The reference value is 0.13983600738410132, which is similar but not identical.

Overall, the 'Income' feature appears to have drifted in the current dataset, with changes in its distribution and impact on the model's predictions.

            ### Credit Score

            **Credit Score Feature Analysis**

The 'Credit Score' feature is a numerical feature with a range of 300 to 850. It is used to assess the creditworthiness of borrowers.

**Drift Analysis**

The 'get_drift_report' tool was used to analyze the distribution of the 'Credit Score' feature in the reference and current datasets. The results show that the distribution of the 'Credit Score' feature has not changed significantly between the reference and current datasets, with a drift score of 0.0778. This indicates that the feature has not drifted, and the dataset does not have data drift.

**SHAP Values**

The 'get_shap_values' tool was used to calculate the mean(|SHAP value|) for the 'Credit Score' feature. The results show that the mean(|SHAP value|) for the 'Credit Score' feature is 0.0573, which is lower than the reference value of 0.0573. This suggests that the feature attribution has changed slightly, but the change is not significant.

**Feature Importance**

The 'Credit Score' feature is an important feature in the model, as it has a relatively high mean(|SHAP value|) value. This suggests that the feature has a significant impact on the model's predictions.

**Conclusion**

The 'Credit Score' feature has not drifted significantly between the reference and current datasets. However, there is a slight change in the feature attribution, which may indicate a slight change in the importance of the feature. Overall, the 'Credit Score' feature remains an important feature in the model.

            ### Loan Amount

            **Feature 'Loan Amount' Analysis**

The 'Loan Amount' feature is a numerical feature with a range of $1,000 to $50,000. It represents the amount borrowed by the borrower.

**Distribution Analysis**

The distribution of 'Loan Amount' in the reference dataset is skewed to the right, with most values concentrated between $10,000 and $30,000. The distribution is relatively uniform, with a mean value of approximately $20,000.

In the current dataset, the distribution of 'Loan Amount' is also skewed to the right, but with a slightly different shape than the reference dataset. The mean value is slightly lower, at approximately $19,500.

**Drift Analysis**

The Kullback-Leibler divergence test indicates that there is no significant drift in the distribution of 'Loan Amount' between the reference and current datasets. The drift score is 0.06465984187565631, which is below the threshold of 0.1.

**SHAP Values**

The mean(|SHAP value|) for the 'Loan Amount' feature is 0.030296443826883252 in the current dataset, which is slightly lower than the reference dataset (0.03091725874540736). This suggests that the feature attribution may have changed slightly due to the shift in the distribution of 'Loan Amount'. However, the difference is relatively small, and the feature remains an important contributor to the model's predictions.

            ### Loan Term

            The 'Loan Term' feature is a numerical feature representing the loan term in months, ranging from 12 to 60. 

The 'get_drift_report' tool analyzed the 'Loan Term' feature and found that there is no significant drift in the distribution of this feature between the reference and current datasets. The calculated drift score is 0.06991922445224397, which is below the threshold of 0.1. Therefore, the 'dataset_drift' flag is set to False, indicating that no dataset drift is detected for this feature.

The 'get_drift_report' tool also provided detailed distribution information for the 'Loan Term' feature in both the current and reference datasets. The distribution is represented as a 'small_distribution' dictionary, which contains the 'x' and 'y' values for a small sample of data points. The 'x' values represent the loan terms, and the 'y' values represent the corresponding probabilities.

The distribution of the 'Loan Term' feature in the current dataset is slightly skewed to the right, with a mean value of 37.4 months and a standard deviation of 10.8 months. In contrast, the distribution of the 'Loan Term' feature in the reference dataset is also skewed to the right, but with a mean value of 40.8 months and a standard deviation of 11.2 months.

The 'get_shap_values' tool analyzed the 'Loan Term' feature and found that the mean(|SHAP value|) for this feature is 0.08865791016936486. This value represents the average impact of the 'Loan Term' feature on the model's predictions. The 'position' of the 'Loan Term' feature is 2, indicating that it is the second most important feature in terms of its impact on the model's predictions.

            ### Interest Rate

            The 'Interest Rate' feature is a numerical feature with a range of 3.5% to 25%. It represents the interest rate of the loan in percentage. The distribution of this feature in the reference dataset is skewed to the right, with most values concentrated between 5% and 15%. In contrast, the distribution of this feature in the current dataset is also skewed to the right, but with a slightly different shape and more values concentrated between 6% and 12%.

The Kullback-Leibler divergence statistical test was used to detect drift in this feature, and the result indicates that there is a significant drift (drift score = 0.12211093048448328) between the reference and current datasets. This suggests that the distribution of the 'Interest Rate' feature has changed significantly between the two datasets, which may lead to a decrease in model performance.

The mean(|SHAP value|) for the 'Interest Rate' feature in the reference dataset is 0.02195194757664086, and in the current dataset is 0.017982049611167866. This indicates that the average impact of the 'Interest Rate' feature on the model's predictions has decreased slightly in the current dataset compared to the reference dataset.

            ### Employment Length

            The feature 'Employment Length' is a numerical feature that represents the number of years the borrower has been employed, ranging from 0 to 40. It is classified as a numerical feature due to its quantitative nature.

The results of the 'get_drift_report' tool indicate that the distribution of 'Employment Length' has changed significantly between the reference and current datasets, leading to a decrease in model performance. The Kullback-Leibler divergence statistical test was used to detect drift, and the threshold was set at 0.1. The calculated drift score is 0.10422809774139326, indicating that the distribution of 'Employment Length' has drifted.

The distribution information for the current and reference datasets shows that the current distribution is skewed towards lower values, with a mode at 0 years of employment. In contrast, the reference distribution is more evenly distributed, with a mode at 8 years of employment.

The 'get_shap_values' tool was used to calculate the mean(|SHAP value|) for each feature, including 'Employment Length'. The result shows that 'Employment Length' has a mean(|SHAP value|) of 0.07723764793746474, indicating that it has a moderate impact on the model's predictions. The rank position of 'Employment Length' is 3, indicating that it is one of the top features contributing to the model's predictions.

            ### Home Ownership

            The 'Home Ownership' feature is a categorical variable with three possible values: 0 (Rent), 1 (Own), and 2 (Mortgage). This feature represents the status of the borrower's home ownership.

The 'get_drift_report' tool has analyzed this feature and found that there is a significant drift in the distribution of this feature between the reference and current datasets. The Kullback-Leibler divergence statistical test has been used to detect this drift, and the threshold used was 0.1. The calculated drift score is 0.18557356469873026, indicating that the distribution of this feature has changed significantly.

The distribution information for the current and reference datasets shows that the current dataset has a more concentrated distribution, with 16% of the data points in the 'Rent' category, 184% in the 'Own' category, and 0% in the 'Mortgage' category. In contrast, the reference dataset has a more balanced distribution, with 62% in the 'Rent' category, 708% in the 'Own' category, and 30% in the 'Mortgage' category.

This drift in the 'Home Ownership' feature may indicate changes in the behavior or characteristics of the borrowers in the current dataset, which could impact the performance of the model.

            ### Marital Status

            **Feature 'Marital Status'**

The 'Marital Status' feature is a categorical variable with four possible values: 0 (Single), 1 (Married), 2 (Divorced), and 3 (Widowed). This feature is represented as an integer, indicating the marital status of the borrower.

**Drift Analysis**

The 'get_drift_report' tool has analyzed the 'Marital Status' feature and detected drift. The Kullback-Leibler divergence statistical test has been used to detect drift, with a threshold of 0.1. The calculated drift score is 5.655843738731566, indicating that the distribution of the 'Marital Status' feature has changed significantly between the reference and current datasets.

**Distribution Information**

The current distribution of the 'Marital Status' feature is represented by a small distribution, which shows the proportion of each value in the current dataset. The reference distribution is also shown, which represents the proportion of each value in the reference dataset.

**SHAP Values**

The 'get_shap_values' tool has calculated the mean(|SHAP value|) for the 'Marital Status' feature. The reference value is 0.041422401537971096, indicating the average impact of the 'Marital Status' feature on the model's predictions in the reference dataset. The current value is 0.07354211915327408, indicating the average impact of the 'Marital Status' feature on the model's predictions in the current dataset. The current value is higher than the reference value, indicating that the 'Marital Status' feature has a greater impact on the model's predictions in the current dataset.

            ### Dependents

            The 'Dependents' feature is a categorical feature representing the number of dependents, ranging from 0 to 5. It is an integer type, meaning it can take on a specific set of discrete values.

The 'Dependents' feature has undergone a statistical test for data drift, specifically the Kullback-Leibler divergence test. The test revealed that there is a significant drift in the distribution of this feature between the reference and current datasets. The drift score is 0.129, which is above the threshold of 0.1. This indicates that the distribution of 'Dependents' has changed significantly between the two datasets.

The distribution information for 'Dependents' in both the reference and current datasets is also provided. The reference dataset shows a distribution with a small range of values, while the current dataset shows a more spread out distribution. This suggests that the number of dependents is not as evenly distributed in the current dataset as it was in the reference dataset.

The 'Dependents' feature has a mean SHAP value of 0.0185, which is lower than the mean SHAP value of the reference dataset (0.0209). This suggests that the contribution of 'Dependents' to the model's predictions has decreased in the current dataset compared to the reference dataset.
