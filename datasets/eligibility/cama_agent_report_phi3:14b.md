
        # Eligibility Simulation Data - Deep Insight Report

        ## Overview
         ### Summary:
The provided data analysis reveals significant drift for two features, "Employment Status" and "Marital Status," between reference and current datasets. The Kullback-Leibler divergence scores indicate substantial differences in their distributions over time. Additionally, SHAP values show that these features have varying impacts on model predictions across the datasets.

### Conclusion:
The observed data drift for "Employment Status" and "Marital Status" suggests changes in socioeconomic factors or demographic trends affecting their distributions. This may influence model performance, necessitating updates to maintain accuracy with new data. The increased impact of these features on predictions highlights the importance of monitoring feature influences over time.

        ## Details

        ### Label Insight
         The label "ProgramEligibility" in the dataset is a categorical variable that serves as an indicator of whether individuals are eligible for a specific program or not. It has two possible values: 0 and amoeba, which represent 'Not Eligible' and 'Eligible', respectively. The label plays a crucial role in predicting the outcome of the model by classifying each individual as either eligible (1) or non-eligible (0).

The data type for this variable is an integer, which allows for efficient computation during model training and prediction processes. As a categorical variable with only two possible values, it simplifies the classification task and makes it easier to interpret results. The label "ProgramEligibility" can be used as the target variable in supervised learning algorithms such as logistic regression or decision trees, which aim to predict whether an individual is eligible for a specific program based on their attributes like age, income, education level, employment status, and marital status.

In summary, "ProgramEligibility" serves as the label variable in this dataset that indicates if individuals are eligible or not eligible for a particular program. It is an integer-type categorical variable with two possible values: 0 (Not Eligible) and 1 (Eligible). This label plays a vital role in training predictive models to classify individuals based on their attributes, ultimately helping decision-makers determine who qualifies for the specific program.


            ### Age

             The provided dataset drift detection result indicates that there is no significant drift detected between the current and reference datasets for the feature "Age". This conclusion is based on the Kullback-Leibler divergence statistic, which measures how one probability distribution differs from a second, expected probability distribution.

Here's an explanation of each part of the result:

1. Feature Name: The drift detection was performed for the feature "Age". This is likely a numerical (numeric) feature as indicated by 'column_type': 'num'.

2. Statistic Used: Kullback-Leibler divergence was used to measure the difference between the two distributions of the current and reference datasets. The threshold value set for this statistic is 0.1, which means that if the calculated KL divergence exceeds this value, it would indicate a significant drift.

3. Drift Score: The actual Kullback-Leibler divergence score between the current and reference distributions of "Age" was found to be 0.06325575780482698. This value is below the threshold (0.1), indicating that there's no significant drift detected for this feature.

4. Drift Detected: Based on the KL divergence score, it was determined that 'drift_detected' is False. In other words, the distributions of "Age" in both datasets are considered to be similar enough not to indicate a significant change or drift.

5. Distribution Information: The result provides detailed distribution information for both current and reference datasets. For example, it shows that the 'small_distribution' (which might represent quantiles) contains values of x and corresponding y probabilities for each dataset. These distributions can be used to visualize how similar or different they are.

6. SHAP Values: The result also includes a separate analysis using SHAP (SHapley Additive exPlanations) values, which is another method to understand feature importance in machine learning models. It calculates the mean absolute value of SHAP for each feature and ranks them based on their impact on model predictions. In this case, both reference and current datasets have similar rankings ('position': amoeba2') with a slight difference in 'value'. This suggests that there is no significant change in feature importance or attribution drift either.

In summary, the dataset drift detection result indicates that for the "Age" feature, there's no significant distributional shift between the current and reference datasets based on Kullback-Leibler divergence and SHAP values analysis.

            ### Income

             The provided result indicates that a feature attribution drift has been detected for the "Income" column in your dataset. This is based on the Kullback-Leibler divergence statistic which measures how one probability distribution differs from another reference probability distribution.

Here's an explanation of each part of the result:

1. `column_name`: The name of the feature where drift was detected, in this case "Income".
2. `column_type`: The type of data contained within the column; here it is numerical (`num`).
3. `stattest_name`: The statistical test used to detect the drift, which is Kullback-Leibler divergence. This test measures how much one distribution differs from another reference distribution.
4. `stattest_threshold`: A threshold value for determining if a change in distributions is significant enough to be considered as drift; here it's set at 0.1. The higher the Kullback-Leibler divergence, the more different the two distributions are from each other.
5. `drift_score`: A numerical value representing the degree of difference between the current and reference distribution for this feature. In your case, it's 0.7978008461594442 which is significantly higher than the threshold (0.1), indicating a drift has occurred.
6. `drift_detected`: A boolean value that indicates whether or not a drift was detected; here it's True, meaning there is indeed a feature attribution drift for this column.
7. `current` and `reference`: These dictionaries contain the distribution information of the current dataset (`X`) and reference dataset respectively. They include details about small distributions (x and y values) which represent different quantiles or bins in your data. The difference between these two distributions is what led to the detection of drift.
8. `result`: This dictionary contains the mean(|SHAP value|) for each feature, showing the average impact of each feature on the model's predictions. It also includes a position indicating the rank order based on its Mean(|SHAP value|). In your case, there is no difference in ranking between reference and current datasets (both have `position`: 1), but the mean(|SHAP value|) has increased from 0.169 to 0.249 which indicates that the feature's impact on model predictions has changed significantly.

In conclusion, both Kullback-Leibler divergence and SHAP values indicate a significant change in the distribution of "Income" data between your current dataset and reference dataset. This suggests there may have been changes to the input data over time that could affect the performance or interpretability of your model.

            ### Education Level

             The feature "Education Level" is a categorical variable that represents the highest level of education attained by an individual on a scale from 0 to 3, where each value corresponds to a specific educational milestone: no formal education (0), high school diploma (1), bachelor's degree (2), and graduate degree (3).

The tool results provided for this feature include two analyses: drift report using the `get_drift_report` function, and SHAP values analysis with the `get_shap_values` function.

**Drift Report Analysis**: The drift report indicates that there is a significant change in the distribution of "Education Level" between the reference dataset (used for training) and the current dataset (new data used for inference). This is determined using Kullback-Leibler divergence as the statistical test, with a threshold set at 0.1. The drift score calculated from this analysis is 0.1851521399815421, which exceeds the stattest_threshold of 0

The current distribution shows that there are more individuals without formal education (x=0) and fewer with high school diplomas (x=1), bachelor's degrees (x=2), or graduate degrees (x=3). In contrast, the reference dataset had a higher number of people with high school diplomas (x=1) and more individuals with bachelor's degrees (x=2) and graduate degrees (x=3).

This drift in "Education Level" distribution could potentially impact model performance if education level is an important feature for the predictions. It suggests that there has been a shift in the educational attainment of individuals within the population, which may require retraining or updating the model to maintain its accuracy and reliability.

**SHAP Values Analysis**: The SHAP values analysis provides insights into how much each feature contributes to the model's predictions on average. In this case, "Education Level" has a mean absolute SHAP value of 0.11009905271521023 in the reference dataset and 0.06845397004237376 in the current dataset. The position of "Education Level" has dropped from rank 3 to rank 

This change indicates that the feature's importance for model predictions has decreased between the two datasets, which could be due to changes in the distribution or relationships among features within the data. This shift may also suggest a need to reassess and potentially update the model to account for these changes in feature attribution.

            ### Employment Status

             The feature "Employment Status" is a categorical variable that represents an individual's current job market participation status. It has three possible values: 0 for unemployed, 1 for part-time employment, and 2 for full-time employment. This information can be crucial in understanding the socioeconomic factors influencing a person's life or predicting their behavior based on their job status.

According to the provided data analysis tools results:

1. **Get Drift Report**: The drift report indicates that there is significant drift detected for the "Employment Status" feature between the reference and current datasets, with a Kullback-Leibler divergence score of 0.7046963105072126. This high value suggests that the distribution of employment statuses in the new dataset differs significantly from the original training data. The drift detection is based on the Kullback-Leibler divergence test, which measures how one probability distribution diverges from a second expected probability distribution.

The current and reference distributions for "Employment Status" are as follows:
   - Reference dataset: 19 unemployed (0), 689 part-time employed (1), and 92 full-time employed (2).
   - Current dataset: 8 unemployed, 192 part-time employed, and no full-time employees.

The drift in the "Employment Status" feature could be due to various factors such as changes in economic conditions or shifts in employment policies that have affected job market participation rates over time. This change may impact model performance if it relies on this feature for predictions, and thus requires attention from data scientists and stakeholders.

2. **Get Shap Values**: The SHAP values analysis provides insights into the average impact of each feature on the model's predictions. For "Employment Status," both in reference and current datasets, it holds the 5th rank position based on its mean absolute SHAP value (0.018275746416542244 for reference and 0.010987271996598626 for current). This indicates that "Employment Status" is a moderately influential feature in the model's predictions, contributing to its decision-making process.

The change in SHAP values between reference and current datasets may also be attributed to the drift detected earlier. As the distribution of employment statuses has changed significantly, it could impact how this feature contributes to the model's predictions. This highlights the importance of monitoring data distributions over time and updating models accordingly to maintain their performance and accuracy.

            ### Marital Status

             The feature "Marital Status" is a categorical variable that represents the current marital status of individuals in the dataset and can take on three possible values: Single (0), Married (1), or Divorced (2). This information provides demographic insights into the population being studied, which could be crucial for various analyses such as market segmentation, policy-making, or social research.

According to the provided drift report result:

- The statistical test used is Kullback-Leibler divergence with a threshold of 0.1. This non-parametric measure quantifies how much one probability distribution differs from another reference probability distribution. A higher value indicates more significant differences between distributions, suggesting potential data drift.

- For the "Marital Status" feature, the calculated Kullback-Leibler divergence score is 0.8026944167960824, which exceeds the threshold of 0.1. This indicates that there has been a significant change in the distribution of marital statuses between the reference and current datasets.

- The drift detection result for this feature is True, confirming that data drift exists for "Marital Status."

The detailed distributions are as follows:

Reference Dataset (historical):
  - Single: 93 occurrences
  - Married: 688 occurrences
  - Divorced: 19 occurrences

Current Dataset (new data for inference):
  - Single: 83 occurrences
  - Married: n53 occurrences
  - Divorced: 64 occurrences

The changes in the distribution of marital statuses between datasets suggest that there has been a shift in the population's demographics. This could be due to various factors such as societal trends, policy changes, or other external influences affecting marriage and divorce rates. The presence of data drift for this feature may impact model performance if the model was trained on the reference dataset without accounting for these distributional shifts.

In terms of SHAP values:

- In the reference dataset, "Marital Status" has a mean absolute SHAP value of 0.05409217592159332 and is ranked at position 4 in terms of its impact on model predictions.

- In the current dataset, the mean absolute SHAP value for "Marital Status" increases to 0.09958768447538655 and moves up to position n3. This indicates that changes in marital statuses have become more influential on model predictions with the new data, which could be a result of the observed drift in this feature's distribution.

In conclusion, the "Marital Status" feature has experienced significant data drift between the reference and current datasets, as evidenced by changes in its probability distribution and increased impact on model predictions. This information should prompt further investigation into potential causes for these shifts and may necessitate updating or retraining models to maintain their performance with new data.
