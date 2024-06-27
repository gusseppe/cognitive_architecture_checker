 # Eligibility Simulation Data Analysis Report

## Executive Summary:
This report presents an analysis of a simulated dataset designed to evaluate individual eligibility for a specific program based on various demographic and socioeconomic factors such as Age, Income, Education Level, Employment Status, and Marital Status. The label variable 'ProgramEligibility' indicates whether each individual is eligible (1) or not eligible (
0). Our analysis includes a comprehensive examination of the dataset characteristics, feature importance using SHAP values, and an assessment for potential data drift over time.

## Dataset Overview:
The Eligibility Simulation Data comprises 1000 samples with six features and one label variable. The numerical features are 'Age' (ranging from 18 to 65 years) and 'Income' (ranging from $20,000 to $70,000). Categorical features include 'Education Level', 'Employment Status', and 'Marital Status'.

### Feature Descriptions:
- **Age**: Represents the age of individuals in years.
- **Income**: Reflects annual income in thousands of dollars, indicating economic status.
- **Education Level**: Indicates highest education level attained (0 to 3).
- **Employment Status**: Shows current job market participation (unemployed, part-time, full-time).
- **Marital Status**: Provides demographic insights into marital status.

### Label Description:
'ProgramEligibility': Determines eligibility for the program with 0 as not eligible and 1 as eligible.

## Data Drift Analysis:
Our analysis detected a significant data drift in the 'Marital Status' feature, which may impact model performance over time. The divergence score is high at 0.8026944167960824, exceeding our threshold of 0.1 and indicating that this feature has changed significantly between the reference dataset and current data.

### SHAP Values Analysis:
SHAP values were calculated to understand the impact of each feature on model predictions for eligibility. The results are as follows:
- **Income**: Highest importance in both reference (0.24910130910592299) and current data (0.16902756259348087).
- **Age**: Slightly less important in the current dataset compared to the reference.
- **Education Level, Employment Status, Marital Status**: All show a decrease in importance from the reference to the current data.

## Recommendations:
Given the detected drift in 'Marital Status', it is recommended that we retrain our model periodically or implement strategies for handling concept drift. Additionally, monitoring SHAP values over time can help us understand changing feature importance and adjust our model accordingly.