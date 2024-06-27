# Comprehensive Report

## Executive Summary

This report provides a detailed analysis of a dataset used to predict the likelihood of individuals developing a chronic condition based on various features. The analysis includes distribution drift and feature attribution using SHAP values to understand the influence of each feature on the prediction model. The report highlights key findings and provides insights into the stability and relevance of the features over time.

## Dataset Synopsis
**Title**: Chronic Condition Prediction Data  
**Features Analyzed**: Age, BMI, Blood Pressure, Cholesterol, Physical Activity, Smoking Status, Diet Quality, Family History, Income, Education Level
**Label Variable**: ChronicCondition  

This dataset simulates the likelihood of individuals developing a chronic condition based on attributes such as Age, BMI, Blood Pressure, Cholesterol, Physical Activity, Smoking Status, Diet Quality, Family History, Income, and Education Level. The 'ChronicCondition' variable serves as the label, indicating whether an individual is likely (1) or not likely (0) to develop the chronic condition. 

## Label Description
**ChronicCondition**: Indicates the likelihood of developing a chronic condition, with 0 representing no chronic condition and 1 representing chronic condition.
The label appears to be well-defined with no issues, as it clearly differentiates between the presence and absence of a chronic condition.

## Feature Analysis

### Feature name: Age
- **Description**: Age of the individual in years, ranging from 18 to 90.
- **Type**: Numerical
- **Possible Values**: Ranging from 18 to 90 years.
- **Data Type**: int

#### Distribution Drift Analysis
- **Statistical Test**: Kullback-Leibler divergence
- **Drift Score**: 0.03778629771302727
- **Detection**: No drift detected
- **Current vs. Reference Distribution**:
  - Current: {'small_distribution': {'x': [31.0, 36.5, 42.0, 47.5, 53.0, 58.5, 64.0, 69.5, 75.0, 80.5, 86.0], 'y': [0.002727272727272727, 0.0036363636363636364, 0.013636363636363636, 0.016363636363636365, 0.045454545454545456, 0.035454545454545454, 0.03363636363636364, 0.02090909090909091, 0.005454545454545454, 0.004545454545454545]}}
  - Reference: {'small_distribution': {'x': [18.0, 25.2, 32.4, 39.6, 46.8, 54.0, 61.2, 68.4, 75.6, 82.8, 90.0], 'y': [0.00017361111111111112, 0.0005208333333333333, 0.00329861111111111, 0.010416666666666671, 0.02690972222222221, 0.0392361111111111, 0.03229166666666665, 0.016840277777777805, 0.007291666666666664, 0.0019097222222222215]}}
  - Interpretation: The distributions of age in both the current and reference datasets are similar, indicating no significant changes over time. Minor variations in frequencies are observed, but they do not indicate any substantial drift.

#### Feature Attribution Analysis
  - Method: Tree SHAP
  - Training Data: 0.08906002648096621 (Rank 3)
  - Current Data: 0.050937679805919664 (Rank 5)
  - Interpretation: The SHAP values for age have decreased in the current data compared to the training data, suggesting that age has become slightly less influential in predicting chronic conditions over time.

#### Overall Interpretation**: 
  Age remains an important feature but its influence has decreased slightly in the current dataset compared to the training dataset.

### Feature name: BMI
- **Description**: Body Mass Index of the individual, ranging from 18.5 to 40.0.
- **Type**: Numerical
- **Possible Values**: Ranging from 18.5 to 40.0.
- **Data Type**: float

#### Distribution Drift Analysis
- **Statistical Test**: Kullback-Leibler divergence
- **Drift Score**: 0.11257326919665277
- **Detection**: Drift detected
- **Current vs. Reference Distribution**:
  - Current: {'small_distribution': {'x': [18.41029156979427, 21.42048565665614, 24.43067974351801, 27.44087383037988, 30.451067917241744, 33.46126200410362, 36.47145609096548, 39.48165017782735, 42.49184426468922, 45.50203835155109, 48.51223243841296], 'y': [0.004983067392720021, 0.029898404356320126, 0.08139010074776035, 0.08471214567624047, 0.06644089856960021, 0.03322044928480018, 0.023254314499360128, 0.004983067392720016, 0.001661022464240005, 0.0016610224642400093]}}
  - Reference: {'small_distribution': {'x': [18.5, 20.61, 22.72, 24.830000000000002, 26.94, 29.05, 31.160000000000004, 33.27, 35.38, 37.49, 39.6], 'y': [0.0023696682464454982, 0.01184834123222749, 0.04798578199052126, 0.09063981042654032, 0.1167061611374408, 0.11670616113744059, 0.05627962085308059, 0.02251184834123223, 0.00770142180094787, 0.0011848341232227491]}}
  - Interpretation: The BMI distribution shows noticeable differences, with the current data having higher frequencies in certain BMI ranges compared to the reference data. This indicates changes in the population's BMI distribution over time.

#### Feature Attribution Analysis
  - Method: Tree SHAP
  - Training Data: 0.14121425129867368 (Rank 1)
  - Current Data: 0.16781096493974235 (Rank 1)
  - Interpretation: BMI remains the most influential feature in predicting chronic conditions, with its SHAP value increasing in the current data, indicating its growing importance.

#### Overall Interpretation**: 
  BMI is a crucial feature with significant influence on the prediction model, and its importance has increased over time.

### Feature name: Blood Pressure
- **Description**: Systolic blood pressure of the individual in mmHg, ranging from 80 to 180.
- **Type**: Numerical
- **Possible Values**: Ranging from 80 to 180 mmHg.
- **Data Type**: int

#### Distribution Drift Analysis
- **Statistical Test**: Kullback-Leibler divergence
- **Drift Score**: 0.3295963763250584
- **Detection**: Drift detected
- **Current vs. Reference Distribution**:
  - Current: {'small_distribution': {'x': [77.42647761458834, 93.60024655055858, 109.77401548652881, 125.94778442249904, 142.12155335846927, 158.29532229443953, 174.46909123040976, 190.64286016638, 206.81662910235025, 222.99039803832045, 239.1641669742907], 'y': [0.0015457126968347085, 0.0021639977755685937, 0.008346848562907433, 0.009892561259742144, 0.014838841889613187, 0.01112913141720991, 0.008965133641641317, 0.003400567933036356, 0.0012365701574677701, 0.0003091425393669414]}}
  - Reference: {'small_distribution': {'x': [80.0, 90.0, 100.0, 110.0, 120.0, 130.0, 140.0, 150.0, 160.0, 170.0, 180.0], 'y': [0.000125, 0.001875, 0.003, 0.00875, 0.018500000000000003, 0.025625, 0.020125, 0.014125, 0.006, 0.001875]}}
  - Interpretation: There are significant differences between the current and reference distributions of blood pressure, with the current data showing higher variability and frequencies at different ranges.

#### Feature Attribution Analysis
  - Method: Tree SHAP
  - Training Data: 0.07114418923716576 (Rank 4)
  - Current Data: 0.053554968593565636 (Rank 4)
  - Interpretation: The importance of blood pressure in predicting chronic conditions has decreased slightly in the current data, as indicated by the lower SHAP value.

#### Overall Interpretation**: 
  Blood pressure remains an important feature, but its influence has slightly decreased in the current dataset.

### Feature name: Cholesterol
- **Description**: Total cholesterol level of the individual in mg/dL, ranging from 150 to 300.
- **Type**: Numerical
- **Possible Values**: Ranging from 150 to 300 mg/dL.
- **Data Type**: int

#### Distribution Drift Analysis
- **Statistical Test**: Kullback-Leibler divergence
- **Drift Score**: 0.23450676168929094
- **Detection**: Drift detected
- **Current vs. Reference Distribution**:
  - Current: {'small_distribution': {'x': [153.16247399274783, 172.59032864659406, 192.01818330044026, 211.44603795428648, 230.87389260813268, 250.3017472619789, 269.7296019158251, 289.15745656967135, 308.5853112235176, 328.0131658773638, 347.44102053121], 'y': [0.001544174616009944, 0.006176698464039786, 0.006691423336043091, 0.011838672056076256, 0.01158130962007458, 0.008492960388054692, 0.0033457116680215455, 0.0005147248720033148, 0.0005147248720033148, 0.0007720873080049744]}}
  - Reference: {'small_distribution': {'x': [150.0, 165.0, 180.0, 195.0, 210.0, 225.0, 240.0, 255.0, 270.0, 285.0, 300.0], 'y': [0.00025, 0.002, 0.005583333333333333, 0.01375, 0.017, 0.018000000000000002, 0.007666666666666667, 0.0019166666666666668, 0.00041666666666666664, 8.333333333333333e-05]}}
  - Interpretation: The cholesterol distribution in the current dataset shows more variability and higher frequencies in certain ranges compared to the reference data, indicating changes over time.

#### Feature Attribution Analysis
  - Method: Tree SHAP
  - Training Data: 0.03926329553692529 (Rank 6)
  - Current Data: 0.04945714499086426 (Rank 6)
  - Interpretation: The SHAP values for cholesterol have increased, indicating a slight increase in its importance in predicting chronic conditions.

#### Overall Interpretation**: 
  Cholesterol remains a significant feature, with its importance slightly increasing in the current dataset.

### Feature name: Physical Activity
- **Description**: Number of days per week the individual engages in physical activity, ranging from 0 to 7.
- **Type**: Numerical
- **Possible Values**: Ranging from 0 to 7 days per week.
- **Data Type**: int

#### Distribution Drift Analysis
- **Statistical Test**: Kullback-Leibler divergence
- **Drift Score**: 7.48442577690803
- **Detection**: Drift detected
- **Current vs. Reference Distribution**:
  - Current: {'small_distribution': {'x': [0.8292978352142784, 1.3040489151174648, 1.778799995020651, 2.2535510749238377, 2.7283021548270234, 3.20305323473021, 3.6778043146333967, 4.1525553945365825, 4.627306474439769, 5.102057554342956, 5.576808634246142], 'y': [0.10531834916562222, 0.10531834916562227, 0.22116853324780653, 0.2317003681643692, 0.38967789191280205, 0.3475505522465532, 0.358082387163116, 0.22116853324780653, 0.09478651424905994, 0.03159550474968671]}}
  - Reference: {'small_distribution': {'x': [0.0, 0.7, 1.4, 2.0999999999999996, 2.8, 3.5, 4.199999999999999, 4.8999999999999995, 5.6, 6.3, 7.0], 'y': [0.014285714285714285, 0.0625, 0.22678571428571437, 0.0, 0.5089285714285713, 0.466071428571429, 0.0, 0.13749999999999996, 0.010714285714285711, 0.0017857142857142852]}}
  - Interpretation: There is significant drift in the physical activity distribution, with the current data showing higher engagement in physical activity compared to the reference data.

#### Feature Attribution Analysis
  - Method: Tree SHAP
  - Training Data: 0.09817662833236682 (Rank 2)
  - Current Data: 0.07730394004727022 (Rank 3)
  - Interpretation: The SHAP values for physical activity have decreased, indicating that its influence on predicting chronic conditions has diminished over time.

#### Overall Interpretation**: 
  Physical activity shows significant drift and its influence on the prediction model has decreased, suggesting changes in the population's behavior over time.

### Feature name: Smoking Status
- **Description**: Current smoking status, represented as 0 (non-smoker), 1 (former smoker), or 2 (current smoker).
- **Type**: Categorical
- **Possible Values**: {'0': 'Non-smoker', '1': 'Former smoker', '2': 'Current smoker'}
- **Data Type**: int

#### Distribution Drift Analysis
- **Statistical Test**: Kullback-Leibler divergence
- **Drift Score**: 0.20183373734484897
- **Detection**: Drift detected
- **Current vs. Reference Distribution**:
  - Current: {'small_distribution': {'x': [0, 1, 2], 'y': [14, 186, 0]}}
  - Reference: {'small_distribution': {'x': [0, 1, 2], 'y': [44, 724, 32]}}
  - Interpretation: The current data shows a significant decrease in current smokers and non-smokers compared to the reference data, with former smokers being the predominant group.

#### Feature Attribution Analysis
  - Method: Tree SHAP
  - Training Data: 0.006457749486556214 (Rank 10)
  - Current Data: 0.004061665409373835 (Rank 10)
  - Interpretation: The SHAP values for smoking status have decreased, indicating its reduced influence in predicting chronic conditions.

#### Overall Interpretation**: 
  Smoking status shows significant drift and its influence on the prediction model has decreased, likely due to changes in smoking behaviors over time.

### Feature name: Diet Quality
- **Description**: Quality of diet, represented as 0 (poor), 1 (average), or 2 (good).
- **Type**: Categorical
- **Possible Values**: {'0': 'Poor', '1': 'Average', '2': 'Good'}
- **Data Type**: int

#### Distribution Drift Analysis
- **Statistical Test**: Kullback-Leibler divergence
- **Drift Score**: 0.0018915553873695345
- **Detection**: No drift detected
- **Current vs. Reference Distribution**:
  - Current: {'small_distribution': {'x': [0, 1, 2], 'y': [10, 180, 10]}}
  - Reference: {'small_distribution': {'x': [0, 1, 2], 'y': [30, 727, 43]}}
  - Interpretation: The distribution of diet quality in the current data is similar to the reference data, with no significant changes observed.

#### Feature Attribution Analysis
  - Method: Tree SHAP
  - Training Data: 0.013835053054035294 (Rank 9)
  - Current Data: 0.011401517327642103 (Rank 9)
  - Interpretation: The SHAP values for diet quality have decreased slightly, indicating a minor reduction in its influence on predicting chronic conditions.

#### Overall Interpretation**: 
  Diet quality remains a relatively stable feature with minor changes in its influence on the prediction model.

### Feature name: Family History
- **Description**: Family history of chronic condition, represented as 0 (no family history) or 1 (family history).
- **Type**: Categorical
- **Possible Values**: {'0': 'No family history', '1': 'Family history'}
- **Data Type**: int

#### Distribution Drift Analysis
- **Statistical Test**: Kullback-Leibler divergence
- **Drift Score**: 0.005370730255683034
- **Detection**: No drift detected
- **Current vs. Reference Distribution**:
  - Current: {'small_distribution': {'x': [0, 1], 'y': [118, 82]}}
  - Reference: {'small_distribution': {'x': [0, 1], 'y': [431, 369]}}
  - Interpretation: The distribution of family history in the current data is similar to the reference data, with no significant changes observed.

#### Feature Attribution Analysis
  - Method: Tree SHAP
  - Training Data: 0.01724435122228072 (Rank 7)
  - Current Data: 0.018126868998631664 (Rank 7)
  - Interpretation: The SHAP values for family history have remained consistent, indicating its stable influence on predicting chronic conditions.

#### Overall Interpretation**: 
  Family history remains a stable and important feature with consistent influence on the prediction model.

### Feature name: Income
- **Description**: Annual income of the individual in thousands of dollars, ranging from 20k to 100k.
- **Type**: Numerical
- **Possible Values**: Ranging from $20,000 to $100,000.
- **Data Type**: float

#### Distribution Drift Analysis
- **Statistical Test**: Kullback-Leibler divergence
- **Drift Score**: 0.91626108741935
- **Detection**: Drift detected
- **Current vs. Reference Distribution**:
  - Current: {'small_distribution': {'x': [20000.0, 28000.0, 36000.0, 44000.0, 52000.0, 60000.0, 68000.0, 76000.0, 84000.0, 92000.0, 100000.0], 'y': [7.5e-06, 3.75e-06, 4.3750000000000005e-06, 8.125e-06, 9.375e-06, 8.750000000000001e-06, 1.3749999999999999e-05, 1.25e-05, 1.1874999999999999e-05, 4.4999999999999996e-05]}}
  - Reference: {'small_distribution': {'x': [20412.74114767384, 28371.467032906457, 36330.19291813907, 44288.91880337169, 52247.64468860431, 60206.370573836924, 68165.09645906955, 76123.82234430216, 84082.54822953478, 92041.27411476738, 100000.0], 'y': [4.7118094706064826e-07, 5.811231680414662e-06, 1.6020152200062035e-05, 2.9213218717760177e-05, 3.6280932923669935e-05, 2.1674323564789792e-05, 1.115128241376869e-05, 3.926507892172067e-06, 7.853015784344147e-07, 3.141206313737654e-07]}}
  - Interpretation: The income distribution shows significant drift, with higher variability and different frequencies in the current data compared to the reference data, indicating changes in income levels over time.

#### Feature Attribution Analysis
  - Method: Tree SHAP
  - Training Data: 0.06594070343394506 (Rank 5)
  - Current Data: 0.12549868716954315 (Rank 2)
  - Interpretation: The SHAP values for income have increased significantly, indicating its growing importance in predicting chronic conditions.

#### Overall Interpretation**: 
  Income has become a more influential feature, reflecting its increasing importance in the prediction model.

### Feature name: Education Level
- **Description**: Highest education level attained, represented as 0 (no formal education) to 3 (graduate degree).
- **Type**: Categorical
- **Possible Values**: {'0': 'No formal education', '1': 'High school diploma', '2': 'Bachelor degree', '3': 'Graduate degree'}
- **Data Type**: int

#### Distribution Drift Analysis
- **Statistical Test**: Kullback-Leibler divergence
- **Drift Score**: 1.6716891527291513
- **Detection**: Drift detected
- **Current vs. Reference Distribution**:
  - Current: {'small_distribution': {'x': [0, 1, 2, 3], 'y': [2, 44, 11, 143]}}
  - Reference: {'small_distribution': {'x': [0, 1, 2, 3], 'y': [3, 197, 560, 40]}}
  - Interpretation: There is significant drift in the education level distribution, with the current data showing different education attainment frequencies compared to the reference data.

#### Feature Attribution Analysis
  - Method: Tree SHAP
  - Training Data: 0.016434074575538762 (Rank 8)
  - Current Data: 0.01641983309158441 (Rank 8)
  - Interpretation: The SHAP values for education level have remained consistent, indicating its stable influence on predicting chronic conditions.

#### Overall Interpretation**: 
  Education level shows significant drift but maintains a consistent influence on the prediction model.

## Overall Analysis
The dataset shows varying degrees of distribution drift across different features, with significant drift detected in BMI, Blood Pressure, Physical Activity, Smoking Status, Income, and Education Level. These drifts indicate changes in the population's characteristics over time. Feature attribution analysis using SHAP values reveals that BMI remains the most influential feature, with its importance increasing over time. Income has also become more significant, reflecting its growing role in predicting chronic conditions. Other features like Physical Activity and Smoking Status have seen a decrease in their influence. Overall, the dataset highlights the dynamic nature of the factors contributing to chronic conditions, necessitating continuous monitoring and adjustment of prediction models to maintain accuracy.

## Conclusion
The analysis underscores the importance of regularly updating and validating prediction models to account for changes in the population's characteristics. While BMI and Income have become more influential, other features like Physical Activity and Smoking Status have diminished in importance. These insights can guide healthcare professionals and policymakers in targeting interventions more effectively to prevent chronic conditions.
