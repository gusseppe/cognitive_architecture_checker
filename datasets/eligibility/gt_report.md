# Comprehensive Report

## Executive Summary

This report analyzes the eligibility simulation data to determine how different features such as Age, Income, Education Level, Employment Status, and Marital Status affect the ProgramEligibility. By utilizing distribution drift analysis and SHAP values, we aim to identify changes in the data distribution and the significance of each feature in predicting eligibility.

## Dataset Synopsis
**Title**: Eligibility Simulation Data  
**Features Analyzed**: Age, Income, Education Level, Employment Status, Marital Status
**Label Variable**: ProgramEligibility  

This dataset simulates the eligibility of individuals for a specific program, focusing on attributes such as Age, Income, Education Level, Employment Status, and Marital Status. The 'ProgramEligibility' variable serves as the label, indicating whether an individual is eligible (1) or not eligible (0) for the program. 

## Label Description
**ProgramEligibility**: Indicates eligibility for a specific program, with 0 representing not eligible and 1 representing eligible, serving as the label variable for predictions.

The label does not exhibit issues in this analysis. However, it is important to note that the label was not included in the drift analysis and SHAP values, focusing solely on feature behavior and influence.

## Feature Analysis

### Feature name: Age
- **Description**: Age of the individual in years, ranging from 18 to 65.
- **Type**: Numerical
- **Possible Values**: Ranging from 18 to 65 years.
- **Data Type**: int

#### Distribution Drift Analysis
- **Statistical Test**: Kullback-Leibler divergence
- **Drift Score**: 0.06325575780482698
- **Detection**: No drift detected
- **Current vs. Reference Distribution**:
  - Current: {'small_distribution': {'x': [24.0, 27.4, 30.8, 34.2, 37.6, 41.0, 44.4, 47.8, 51.2, 54.599999999999994, 58.0], 'y': [0.010294117647058827, 0.0264705882352941, 0.03970588235294115, 0.038235294117647076, 0.039705882352941195, 0.06911764705882356, 0.027941176470588247, 0.02499999999999996, 0.01029411764705885, 0.007352941176470575]}}
  - Reference: {'small_distribution': {'x': [18.0, 22.7, 27.4, 32.1, 36.8, 41.5, 46.2, 50.9, 55.6, 60.300000000000004, 65.0], 'y': [0.0007978723404255321, 0.0053191489361702135, 0.02313829787234041, 0.03085106382978726, 0.05265957446808508, 0.04893617021276593, 0.025265957446808533, 0.018351063829787222, 0.005851063829787231, 0.0015957446808510653]}}
  - Interpretation: The current distribution shows higher frequencies in the middle age ranges (30-50 years) compared to the reference distribution, which has a more even spread across the age range. This suggests a slight shift in the population's age composition, although no significant drift is detected.

#### Feature Attribution Analysis
  - Method: Tree SHAP
  - Training Data: 0.1675692700443467 (Rank 2)
  - Current Data: 0.10098040394127042 (Rank 2)
  - Interpretation: The SHAP values indicate that Age is consistently the second most important feature in predicting program eligibility. However, its importance has slightly decreased in the current data compared to the training data.

#### Overall Interpretation**: 
  Age remains a crucial factor in determining program eligibility, with no significant distribution drift detected. The slight decrease in SHAP value suggests a minor reduction in its predictive power in the current data.

### Feature name: Income
- **Description**: Annual income of the individual in thousands of dollars, indicating economic status, ranging from 20k to 70k.
- **Type**: Numerical
- **Possible Values**: Ranging from $20,000 to $70,000.
- **Data Type**: float

#### Distribution Drift Analysis
- **Statistical Test**: Kullback-Leibler divergence
- **Drift Score**: 0.7978008461594442
- **Detection**: Drift detected
- **Current vs. Reference Distribution**:
  - Current: {'small_distribution': {'x': [-3508.2364074368093, 10667.570547951202, 24843.377503339212, 39019.18445872722, 53194.99141411523, 67370.79836950325, 81546.60532489125, 95722.41228027927, 109898.21923566727, 124074.02619105528, 138249.8331464433], 'y': [1.4108544270489167e-06, 4.5852768879089795e-06, 8.465126562293502e-06, 1.6577539517824768e-05, 1.8693821158398144e-05, 1.022869459610465e-05, 5.643417708195664e-06, 2.468995247335605e-06, 1.7635680338111466e-06, 7.05427213524458e-07]}}
  - Reference: {'small_distribution': {'x': [21687.0, 26395.8, 31104.6, 35813.4, 40522.2, 45231.0, 49939.8, 54648.6, 59357.4, 64066.200000000004, 68775.0], 'y': [2.389143730886851e-06, 1.964407067618077e-05, 5.707398912674138e-05, 6.211773700305817e-05, 3.4775314305130796e-05, 1.672400611620794e-05, 6.901970778117574e-06, 9.025654094461428e-06, 2.654604145429832e-06, 1.0618416581719344e-06]}}
  - Interpretation: The current distribution of Income shows significant differences compared to the reference distribution, with the current data having more extreme values and higher variability. This indicates a substantial drift in income levels among the population.

#### Feature Attribution Analysis
  - Method: Tree SHAP
  - Training Data: 0.16902756259348087 (Rank 1)
  - Current Data: 0.24910130910592299 (Rank 1)
  - Interpretation: Income remains the most important feature for predicting program eligibility. The increase in SHAP value in the current data indicates that Income has become even more influential in determining eligibility.

#### Overall Interpretation**: 
  Income shows significant distribution drift and has increased in importance for predicting eligibility. This suggests changes in the economic status of the population, making Income a critical factor in the current eligibility model.

### Feature name: Education Level
- **Description**: Reflects the highest education level attained, on a scale from 0 (no formal education) to 3 (graduate degree), suggesting educational attainment.
- **Type**: Categorical
- **Possible Values**: {'0': 'No formal education', '1': 'High school diploma', '2': 'Bachelor degree', '3': 'Graduate degree'}
- **Data Type**: int

#### Distribution Drift Analysis
- **Statistical Test**: Kullback-Leibler divergence
- **Drift Score**: 0.1851521399815421
- **Detection**: Drift detected
- **Current vs. Reference Distribution**:
  - Current: {'small_distribution': {'x': [0, 1, 2, 3], 'y': [1, 49, 150, 0]}}
  - Reference: {'small_distribution': {'x': [0, 1, 2, 3], 'y': [12, 302, 464, 22]}}
  - Interpretation: The current data shows a significant drop in the number of individuals with no formal education or a graduate degree. The majority of the current population falls within the high school diploma and bachelor's degree categories, indicating a drift towards mid-level education.

#### Feature Attribution Analysis
  - Method: Tree SHAP
  - Training Data: 0.11009905271521023 (Rank 3)
  - Current Data: 0.06845397004237376 (Rank 4)
  - Interpretation: The importance of Education Level in predicting eligibility has decreased in the current data, as indicated by the lower SHAP value and its rank dropping from 3 to 4.

#### Overall Interpretation**: 
  Education Level has experienced distribution drift and has decreased in importance for predicting eligibility. The current population shows a concentration in mid-level education, impacting its predictive power.

### Feature name: Employment Status
- **Description**: Current employment status, represented as 0 (unemployed), 1 (part-time), or 2 (full-time), indicating job market participation.
- **Type**: Categorical
- **Possible Values**: {'0': 'Unemployed', '1': 'Part-time employment', '2': 'Full-time employment'}
- **Data Type**: int

#### Distribution Drift Analysis
- **Statistical Test**: Kullback-Leibler divergence
- **Drift Score**: 0.7046963105072126
- **Detection**: Drift detected
- **Current vs. Reference Distribution**:
  - Current: {'small_distribution': {'x': [0, 1, 2], 'y': [8, 192, 0]}}
  - Reference: {'small_distribution': {'x': [0, 1, 2], 'y': [19, 689, 92]}}
  - Interpretation: The current distribution shows a significant drop in the number of full-time employees and an increase in part-time employment. This indicates a notable shift in employment status within the population.

#### Feature Attribution Analysis
  - Method: Tree SHAP
  - Training Data: 0.018275746416542244 (Rank 5)
  - Current Data: 0.010987271996598626 (Rank 5)
  - Interpretation: Employment Status remains the least important feature for predicting eligibility, with its SHAP value slightly decreasing, indicating a minor reduction in its influence.

#### Overall Interpretation**: 
  Employment Status shows significant distribution drift with a shift towards part-time employment. Its importance in predicting eligibility remains low and relatively unchanged.

### Feature name: Marital Status
- **Description**: Current marital status, categorized into Single, Married, or Divorced, to provide demographic insights.
- **Type**: Categorical
- **Possible Values**: {'0': 'Single', '1': 'Married', '2': 'Divorced'}
- **Data Type**: int

#### Distribution Drift Analysis
- **Statistical Test**: Kullback-Leibler divergence
- **Drift Score**: 0.8026944167960824
- **Detection**: Drift detected
- **Current vs. Reference Distribution**:
  - Current: {'small_distribution': {'x': [0, 1, 2], 'y': [83, 53, 64]}}
  - Reference: {'small_distribution': {'x': [0, 1, 2], 'y': [93, 688, 19]}}
  - Interpretation: The current distribution shows a decrease in the number of married individuals and an increase in the number of divorced individuals. This indicates a significant demographic shift in marital status.

#### Feature Attribution Analysis
  - Method: Tree SHAP
  - Training Data: 0.05409217592159332 (Rank 4)
  - Current Data: 0.09958768447538655 (Rank 3)
  - Interpretation: The SHAP values show that Marital Status has increased in importance for predicting eligibility, moving from rank 4 to rank 3. This indicates a growing influence of marital status on eligibility.

#### Overall Interpretation**: 
  Marital Status shows significant distribution drift and has become more important for predicting eligibility. The demographic shift towards more single and divorced individuals impacts its predictive power.

## Overall Analysis
The dataset exhibits noticeable distribution drift in several features: Income, Education Level, Employment Status, and Marital Status. Income and Marital Status have increased in importance for predicting program eligibility, while Education Level and Employment Status have decreased. Age remains a stable and important feature with no significant drift. These changes reflect demographic and economic shifts in the population, affecting the model's performance and feature importance.

## Conclusion
The analysis highlights the need for continuous monitoring of feature distributions and their impact on model predictions. Significant drifts in Income and Marital Status suggest socioeconomic changes that could affect program eligibility criteria. Adjustments to the model or eligibility rules may be necessary to maintain fairness and accuracy in eligibility determination.
