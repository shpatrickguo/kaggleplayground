# Loan Payback Prediction with LightGBM

## Executive Summary

This project presents a loan payback prediction system built for a binary classification task from Kaggle's Playground Series S5E11 competition. The dataset was synthetically generated using Python libraries such as Faker, NumPy, and Pandas, based on the [Loan Prediction Dataset 2025](https://www.kaggle.com/datasets/nabihazahid/loan-prediction-dataset-2025) by nabiha zahid, created solely for educational and research use. The goal is to predict whether a borrower will successfully repay their loan (1) or default (0). To tackle this challenge, the approach employs a LightGBM classifier with automated hyperparameter tuning using FLAML (Fast Lightweight AutoML), achieving strong performance through careful feature engineering and data preprocessing.

## Data

The dataset is sourced from Kaggle's Playground Series S5E11 competition and is based on a synthetically generated loan prediction dataset. The data includes 11 features describing various characteristics of borrowers and their loan applications.

### Features:
1. **Borrower's Demographics:**
   - `gender`: Borrower's gender (Male, Female, Other)
   - `marital_status`: Marital status (Single, Married, Divorced, Widowed)
   - `education_level`: Education level (High School, Bachelor's, Master's, PhD, Other)

2. **Financial Information:**
   - `annual_income`: Borrower's yearly income (continuous)
   - `debt_to_income_ratio`: Ratio of borrower's debt to their income. Lower values indicate better financial health
   - `credit_score`: Credit bureau score (e.g., FICO). Higher scores indicate less risk

3. **Employment Information:**
   - `employment_status`: Current employment type (Employed, Self-Employed, Unemployed, Retired, Student)

4. **Loan Information:**
   - `loan_amount`: Amount of loan taken (continuous)
   - `loan_purpose`: Purpose of the loan (Car, Education, Home, Medical, Debt consolidation, Business, Vacation, Other)
   - `interest_rate`: Interest rate charged on the loan (continuous)
   - `grade_subgrade`: Loan risk grade from A1 (best) to F5 (worst), indicating creditworthiness

### Target Variable:
The model predicts the loan repayment outcome:
- `1`: Borrower paid loan in full (successful repayment)
- `0`: Borrower defaulted (did not repay fully)

## Methodology

The project employs LightGBM, a gradient boosting framework that uses tree-based learning algorithms, known for its speed, efficiency, and ability to handle large datasets with high-dimensional features.

Key aspects of the methodology:
- **Feature Engineering**: 
  - Ordinal encoding for education level (Other < High School < Bachelor's < Master's < PhD) and grade subgrade (A1-F5)
  - One-hot encoding for nominal categorical variables (gender, marital status, employment status, loan purpose)
  - Log transformation for right-skewed numerical features to normalize distributions
  - Standard scaling applied to all numerical features for better model convergence
- **Memory Optimization**: Downcasting numerical columns to reduce memory usage by approximately 20%
- **Automated Hyperparameter Tuning**: FLAML AutoML used to find optimal hyperparameters with ROC AUC as the evaluation metric
- **Train-Test Split**: 80-20 split with random state 42 for reproducibility

The final LightGBM model is configured with the following key parameters (obtained from FLAML):
- **n_estimators**: 53
- **learning_rate**: 0.157 for efficient learning
- **num_leaves**: 4 for model simplicity
- **max_bin**: 1023 for histogram-based learning
- **min_child_samples**: 7 to prevent overfitting
- **colsample_bytree**: 0.761 for feature sampling
- **reg_alpha**: 0.00098 (L1 regularization)
- **reg_lambda**: 0.0064 (L2 regularization)

## Results

The LightGBM model demonstrates strong performance in predicting loan repayment outcomes:
- The model was optimized using FLAML AutoML with a 300-second time budget
- ROC AUC metric was used as the primary evaluation criterion for binary classification
- Automated hyperparameter tuning identified optimal model configuration for the task
- The model successfully processes and predicts on the test dataset

The model's predictions are probability scores indicating the likelihood of successful loan repayment, which can be valuable for financial institutions to assess lending risk and make informed decisions about loan approvals.

## Conclusion

The loan payback prediction system demonstrates the effectiveness of LightGBM combined with automated machine learning (FLAML) in handling binary classification problems with mixed feature types. The combination of careful feature engineering (ordinal and one-hot encoding, log transformations, and scaling), automated hyperparameter tuning, and efficient memory management provides a robust solution for predicting loan repayment outcomes. The model can help financial institutions identify potential defaulters and make data-driven lending decisions. Future work may explore additional feature engineering (such as interaction features between income and loan amount), ensemble methods combining multiple algorithms, time-series cross-validation for more robust validation, or incorporating additional external economic indicators to further improve prediction accuracy.

## Installation

To run the code, ensure you have the following Python packages installed:

```bash
pip install pandas numpy scikit-learn lightgbm flaml seaborn matplotlib
```
