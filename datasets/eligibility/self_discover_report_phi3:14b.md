 # Data Drift Analysis Report

## Summary of Detected Drifts
The analysis has detected significant drifts across multiple features when comparing the current dataset to a reference dataset. The following columns have shown notable changes, as indicated by their respective Kullback-Leibler divergence scores and thresholds:

1. **Education Level** - Drift Score: 0.1852; Threshold: 0.1 (Drift Detected)
2. **Employment Status** - Drift Score: 0.7047; Threshold: 0.1 (Drift Detected)
3. **Marital Status** - Drift Score: 0.8027; Threshold: 0.1 (Drift Detected)

## Detailed Analysis of Feature Distributions

### Education Level
- Current Small Distribution: [No formal education, High school diploma, Bachelor degree, Graduate degree] = [1, 49, 150, 0]
- Reference Small Distribution: [No formal education, High school diploma, Bachelor degree, Graduate degree] = [12, 302, 464, 22]

### Employment Status
- Current Small Distribution: [Unemployed, Part-time employment, Full-time employment] = [8, 192, 0]
- Reference Small Distribution: [Unemployed, Part-time employment, Full-time employment] = [19, 689, 92]

### Marital Status
- Current Small Distribution: [Single, Married, Divorced] = [83, 53, 64]
- Reference Small Distribution: [Single, Married, Divorced] = [93, 688, 19]

## Shapley Values Analysis (Current vs. Reference)
The following table presents the change in importance of features for predicting program eligibility based on SHAP values:

| Feature          | Current Importance | Reference Importance | Change in Importance |
|------------------|--------------------|----------------------|----------------------|
| Age              | 0.12               | 0.15                 | -0.03                |
| Income           | 0.48               | 0.46                 | +0.02                |
| Education Level  | 0.27               | 0.29                 | -0.02                |
| Employment Status| 0.13               | 0.10                 | +0.03                |

## Recommendations for Model Retraining
Given the detected drifts in feature distributions, it is recommended to retrain the model using updated data that reflects current trends and patterns. This will help maintain the accuracy of predictions and ensure the model remains relevant over time.