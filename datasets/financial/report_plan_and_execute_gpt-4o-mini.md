# Comprehensive Monitoring Report on Dataset Changes

## Overview
This report provides an analysis of the changes in the dataset based on the results from the drift detection and SHAP (SHapley Additive exPlanations) value analysis. The focus is on identifying significant changes in the distributions of key features and their impact on model predictions.

## Drift Detection Results
Drift detection was performed using the Kullback-Leibler divergence method. The following features were analyzed:

### 1. **Age**
- **Drift Score**: 0.0388
- **Drift Detected**: No
- **Current Distribution**: 
  - Values: [27.0, 31.0, 35.0, 39.0, 43.0, 47.0, 51.0, 55.0, 59.0, 63.0, 67.0]
  - Frequencies: [0.0025, 0.00375, 0.01625, 0.0175, 0.06125, 0.0575, 0.04125, 0.0325, 0.01125, 0.00625]
- **Reference Distribution**: 
  - Values: [18.0, 23.2, 28.4, 33.6, 38.8, 44.0, 49.2, 54.4, 59.6, 64.8, 70.0]
  - Frequencies: [0.000240, 0.000721, 0.004567, 0.014183, 0.036298, 0.056971, 0.043269, 0.023077, 0.010337, 0.002644]

### 2. **Credit Score**
- **Drift Score**: 0.0778
- **Drift Detected**: No
- **Current Distribution**: 
  - Values: [302.0, 356.8, 411.6, 466.4, 521.2, 576.0, 630.8, 685.6, 740.4, 795.2, 850.0]
  - Frequencies: [0.000365, 0.000821, 0.001734, 0.002372, 0.003102, 0.003558, 0.003102, 0.001916, 0.000912, 0.000365]
- **Reference Distribution**: 
  - Values: [300.0, 355.0, 410.0, 465.0, 520.0, 575.0, 630.0, 685.0, 740.0, 795.0, 850.0]
  - Frequencies: [0.000045, 0.000364, 0.000545, 0.001636, 0.003477, 0.004500, 0.003727, 0.002545, 0.001045, 0.000295]

### 3. **Employment Length**
- **Drift Score**: 0.1042
- **Drift Detected**: Yes
- **Current Distribution**: 
  - Values: [0.0, 4.0, 8.0, 12.0, 16.0, 20.0, 24.0, 28.0, 32.0, 36.0, 40.0]
  - Frequencies: [0.0025, 0.00375, 0.03, 0.0525, 0.06375, 0.04375, 0.03125, 0.0175, 0.00375, 0.00125]
- **Reference Distribution**: 
  - Values: [1.0, 4.9, 8.8, 12.7, 16.6, 20.5, 24.4, 28.3, 32.2, 36.1, 40.0]
  - Frequencies: [0.001603, 0.004808, 0.014103, 0.038141, 0.072115, 0.067308, 0.038141, 0.014103, 0.004808, 0.001282]

### 4. **Income**
- **Drift Score**: 0.1308
- **Drift Detected**: Yes
- **Current Distribution**: 
  - Values: [25501.46, 37951.31, 50401.16, 62851.02, 75300.87, 87750.73, 100200.58, 112650.44, 125100.29, 137550.15, 150000.0]
  - Frequencies: [8.03e-07, 6.02e-06, 6.02e-06, 1.81e-05, 1.41e-05, 1.04e-05, 9.64e-06, 6.83e-06, 4.02e-06, 4.42e-06]
- **Reference Distribution**: 
  - Values: [20000.0, 32745.30, 45490.60, 58235.89, 70981.19, 83726.49, 96471.79, 109217.09, 121962.39, 134707.68, 147452.98]
  - Frequencies: [3.92e-07, 1.96e-06, 7.94e-06, 1.48e-05, 1.94e-05, 1.94e-05, 9.42e-06, 3.73e-06, 1.18e-06, 1.96e-07]

### 5. **Interest Rate**
- **Drift Score**: 0.1221
- **Drift Detected**: Yes
- **Current Distribution**: 
  - Values: [6.41, 8.27, 10.13, 11.99, 13.85, 15.70, 17.56, 19.42, 21.28, 23.14, 25.0]
  - Frequencies: [0.0161, 0.0484, 0.0672, 0.0807, 0.0914, 0.1022, 0.0565, 0.0403, 0.0188, 0.0161]
- **Reference Distribution**: 
  - Values: [3.5, 5.65, 7.8, 9.95, 12.1, 14.25, 16.4, 18.55, 20.7, 22.85, 25.0]
  - Frequencies: [0.0041, 0.0093, 0.0355, 0.0698, 0.1110, 0.1203, 0.0762, 0.0343, 0.0041, 0.0006]

### 6. **Loan Amount**
- **Drift Score**: 0.0647
- **Drift Detected**: No
- **Current Distribution**: 
  - Values: [3141.11, 7827.00, 12512.89, 17198.78, 21884.67, 26570.56, 31256.45, 35942.33, 40628.22, 45314.11, 50000.0]
  - Frequencies: [1.07e-06, 1.07e-05, 2.24e-05, 3.95e-05, 5.34e-05, 3.84e-05, 3.20e-05, 1.17e-05, 1.07e-06, 3.20e-06]
- **Reference Distribution**: 
  - Values: [1000.0, 5900.0, 10800.0, 15700.0, 20600.0, 25500.0, 30400.0, 35300.0, 40200.0, 45100.0, 50000.0]
  - Frequencies: [7.65e-07, 6.12e-06, 1.81e-05, 4.23e-05, 5.28e-05, 5.41e-05, 2.24e-05, 6.12e-06, 1.02e-06, 2.55e-07]

### 7. **Loan Term**
- **Drift Score**: 0.0699
- **Drift Detected**: No
- **Current Distribution**: 
  - Values: [17.0, 20.4, 23.8, 27.2, 30.6, 34.0, 37.4, 40.8, 44.2, 47.6, 51.0]
  - Frequencies: [0.0059, 0.0132, 0.0279, 0.0206, 0.0515, 0.0721, 0.0500, 0.0353, 0.0147, 0.0029]
- **Reference Distribution**: 
  - Values: [12.0, 16.8, 21.6, 26.4, 31.2, 36.0, 40.8, 45.6, 50.4, 55.2, 60.0]
  - Frequencies: [0.0031, 0.0068, 0.0185, 0.0375, 0.0461, 0.0581, 0.0292, 0.0078, 0.0010, 0.0003]

### 8. **Home Ownership**
- **Drift Score**: 0.1856
- **Drift Detected**: Yes
- **Current Distribution**: 
  - Categories: [0, 1, 2]
  - Frequencies: [16, 184, 0]
- **Reference Distribution**: 
  - Categories: [0, 1, 2]
  - Frequencies: [62, 708, 30]

### 9. **Marital Status**
- **Drift Score**: 5.6558
- **Drift Detected**: Yes
- **Current Distribution**: 
  - Categories: [0, 1, 2, 3]
  - Frequencies: [2, 1, 0, 197]
- **Reference Distribution**: 
  - Categories: [0, 1, 2, 3]
  - Frequencies: [20, 538, 237, 5]

### 10. **Dependents**
- **Drift Score**: 0.1291
- **Drift Detected**: Yes
- **Current Distribution**: 
  - Categories: [0, 1, 2, 3, 4, 5]
  - Frequencies: [0, 2, 29, 78, 69, 22]
- **Reference Distribution**: 
  - Categories: [0, 1, 2, 3, 4, 5]
  - Frequencies: [2, 20, 178, 385, 207, 8]

## SHAP Values Analysis
The SHAP values provide insights into the importance of each feature in the model's predictions. The following changes were observed:

### Key Features
- **Income**: 
  - **Current SHAP Value**: 0.1676 (Position: 1)
  - **Reference SHAP Value**: 0.1398 (Position: 1)
  - **Change**: Increased importance.

- **Loan Term**: 
  - **Current SHAP Value**: 0.0887 (Position: 2)
  - **Reference SHAP Value**: 0.1079 (Position: 2)
  - **Change**: Decreased importance.

- **Age**: 
  - **Current SHAP Value**: 0.0535 (Position: 5)
  - **Reference SHAP Value**: 0.0816 (Position: 3)
  - **Change**: Decreased importance.

- **Employment Length**: 
  - **Current SHAP Value**: 0.0772 (Position: 3)
  - **Reference SHAP Value**: 0.0775 (Position: 4)
  - **Change**: Slight decrease in importance.

- **Credit Score**: 
  - **Current SHAP Value**: 0.0526 (Position: 6)
  - **Reference SHAP Value**: 0.0573 (Position: 5)
  - **Change**: Decreased importance.

- **Marital Status**: 
  - **Current SHAP Value**: 0.0735 (Position: 4)
  - **Reference SHAP Value**: 0.0414 (Position: 6)
  - **Change**: Increased importance.

- **Loan Amount**: 
  - **Current SHAP Value**: 0.0303 (Position: 7)
  - **Reference SHAP Value**: 0.0309 (Position: 7)
  - **Change**: Slight decrease in importance.

- **Interest Rate**: 
  - **Current SHAP Value**: 0.0180 (Position: 9)
  - **Reference SHAP Value**: 0.0219 (Position: 8)
  - **Change**: Decreased importance.

- **Dependents**: 
  - **Current SHAP Value**: 0.0185 (Position: 8)
  - **Reference SHAP Value**: 0.0210 (Position: 9)
  - **Change**: Decreased importance.

- **Home Ownership**: 
  - **Current SHAP Value**: 0.0033 (Position: 10)
  - **Reference SHAP Value**: 0.0036 (Position: 10)
  - **Change**: Slight decrease in importance.

## Conclusion
The analysis indicates that significant drift has been detected in the following features: Employment Length, Income, Interest Rate, Home Ownership, Marital Status, and Dependents. The SHAP values suggest that while some features have increased in importance (e.g., Income, Marital Status), others have decreased (e.g., Age, Loan Term). 

It is recommended to further investigate the causes of drift in the detected features and consider retraining the model to ensure its performance remains optimal.