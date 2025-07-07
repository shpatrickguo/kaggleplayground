# Extrovert vs. Introvert Behavior Data
## Summary
This project analyzes personality traits using a dataset derived from both original survey responses and deep learning-generated samples based on the Extrovert vs. Introvert Behavior dataset. The combined data includes 21,424 rows (18,524 generated, 2,900 original) and 7 features related to social habits, event attendance, and self-reported behaviors. A stacked model of supervised classifers was used for prediction, achieving an accuracy of 0.974898 on the test set.

## About the data
The data for this competition was generated using a deep learning model trained on the [Extrovert vs. Introvert Behavior dataset](https://www.kaggle.com/datasets/rakeshkapilavai/extrovert-vs-introvert-behavior-data/data). While the feature distributions closely resemble the original dataset, they are not identical.

The original dataset, provided by Rakesh Kapilavayi, was collected through Google Forms as part of a college research project exploring personality traits and behavioral tendencies among students. Participants answered survey questions using a 0–10 scale, which ensured consistency and simplicity in the responses.
For more details, see the [discussion here](https://www.kaggle.com/datasets/rakeshkapilavai/extrovert-vs-introvert-behavior-data/discussion/583203#3218290).

- Competition data: [Playground Series S5E7 Data](https://www.kaggle.com/competitions/playground-series-s5e7/data)
- Original dataset: [Extrovert vs. Introvert Behavior Data](https://www.kaggle.com/datasets/rakeshkapilavai/extrovert-vs-introvert-behavior-data/data)

- **Rows:** 21424 (18524 generated, 2900 original)
- **Features:** 7

### Features:
- Time_spent_Alone (numeric, hours per week)
- Stage_fear (categorical, Yes/No)
- Social_event_attendance (numeric, events per month)
- Going_outside (numeric, outings per week)
- Drained_after_socializing (categorical, Yes/No)
- Friends_circle_size (numeric)
- Post_frequency (numeric, posts per week)

### Missing Values
Since the **missing percentage for all columns falls within the moderate range of 5–30%**, the best approach is to **impute missing values** rather than drop rows or columns. 

### Target Variable
**Target Variable Distribution** is imbalanced with significantly more extroverts than introverts.

## Train Test Split

Emplyed **stratified k-fold cross-validation** because the**dataset has class imbalance**, and this method ensures that each fold maintains the same class proportions as the overall dataset, providing a more reliable and unbiased estimate of model performance.

## Pre-processing

### Missing Values
For numeric columns, I used the median or mean to fill in missing values, while for categorical columns, I used the mode. This strategy **preserves the size and integrity of the dataset**, ensuring it does not lose valuable information due to moderate missingness.

### Normalization
Since the **numeric columns do not have outliers**, **Min-Max normalization** is a suitable choice. It scales features to a fixed range, typically , preserving the original distribution shape and making features comparable.

### Encoding
I used encoding techniques such as **label encoding** to transform categorical variables (Stage_fear, Drained_after_socializing) into numeric values, making them suitable for machine learning algorithms that require numerical input. 

### Feature Engineering
Polynomial features are created by raising existing numerical features to higher powers and by forming interaction terms between features, which enables linear models to capture complex, non-linear relationships in the data.

## Modeling
This is a supervised binary classification problem, so I will start with models suited for tabular binary classification:
- Logistic Regression
- Random Forest Classifier
- Gradient Boosting Machines (e.g., XGBoost, LightGBM, CatBoost)
- Support Vector Machine (SVM)
- Neural Networks (MLPClassifier for tabular data)
  
Since the gradient boosting machines achieved the highest performances, I selected them for further hyperparameter tuning.

### Tuning
Hyperparameter tuning directly impacts a model’s structure, learning process, and final performance, allowing me to optimize accuracy, generalization, and training efficiency. I chose Bayesian optimization because it reduces the number of evaluations needed to find strong hyperparameter settings, saving both time and computational resources.

## Blending
Used stacking, which is an ensemble technique that combines the predictions of multiple base models using a meta-model. I use it to leverage the strengths of diverse models and allows the meta-model to capture complex relationships between their predictions, resulting in 0.974898 accuracy. 