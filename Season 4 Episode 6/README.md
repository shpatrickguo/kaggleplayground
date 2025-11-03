# Academic Success Prediction with LightGBM

## Executive Summary

This project presents an academic success prediction system built for a multi-class classification task derived from the Predict Students' Dropout and Academic Success dataset from [UCI](https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success). The dataset was generated using a deep learning model trained on the original UCI dataset and includes features related to student demographics, academic performance, and socioeconomic factors. The goal is to predict the student's academic outcome among three categories: Graduate, Dropout, or Enrolled. To tackle this challenge, the approach employs a LightGBM classifier with K-Fold cross-validation, achieving strong accuracy through careful hyperparameter tuning and data augmentation with the original dataset.

## Data

The dataset is sourced from Kaggle's Playground Series S4E6 competition and is based on the [Predict Students' Dropout and Academic Success dataset](https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success) from UCI. The data includes 36 features describing various characteristics of students and their academic journey.

### Features:
1. **Demographic Features:**
   - `Marital status`: Marital status of the student (1 = single, 2 = married, 3 = widower, 4 = divorced, 5 = facto union, 6 = legally separated)
   - `Gender`: Gender of the student (0 = female, 1 = male)
   - `Age_at_enrollment`: Age of the student at enrollment
   - `Nationality`: Nationality of the student
   - `International`: Whether the student is international (1 = yes, 0 = no)
   - `Displaced`: Whether the student is displaced (1 = yes, 0 = no)

2. **Academic Background Features:**
   - `Previous qualification`: Previous qualification of the student
   - `Previous qualification (grade)`: Previous qualification grade of the student
   - `Application mode`: Application mode for the student
   - `Application order`: Order of the application
   - `Course`: Course enrolled by the student
   - `Daytime evening attendance`: Whether the student attends daytime or evening classes (1 = daytime, 0 = evening)

3. **Parental Background Features:**
   - `Mother qualification`: Qualification of the student's mother
   - `Father qualification`: Qualification of the student's father
   - `Mother_occupation`: Occupation of the student's mother
   - `Father_occupation`: Occupation of the student's father

4. **Financial and Support Features:**
   - `Educational_special_needs`: Whether the student has educational special needs (1 = yes, 0 = no)
   - `Debtor`: Whether the student is a debtor (1 = yes, 0 = no)
   - `Tuition_fees_up_to_date`: Whether the student's tuition fees are up to date (1 = yes, 0 = no)
   - `Scholarship_holder`: Whether the student is a scholarship holder (1 = yes, 0 = no)

5. **First Semester Performance Features:**
   - `Curricular units 1st sem (credited)`: Number of curricular units credited in the first semester
   - `Curricular_units_1st_sem_enrolled`: Number of curricular units enrolled in the first semester
   - `Curricular_units_1st_sem_evaluations`: Number of evaluations in the first semester
   - `Curricular_units_1st_sem_approved`: Number of approved units in the first semester
   - `Curricular_units_1st_sem_grade`: Grade in the first semester
   - `Curricular units 1st sem (without evaluations)`: Number of curricular units in the first semester without evaluations

6. **Second Semester Performance Features:**
   - `Curricular units 2nd sem (credited)`: Number of curricular units credited in the second semester
   - `Curricular_units_2nd_sem_enrolled`: Number of curricular units enrolled in the second semester
   - `Curricular_units_2nd_sem_evaluations`: Number of evaluations in the second semester
   - `Curricular_units_2nd_sem_approved`: Number of approved units in the second semester
   - `Curricular_units_2nd_sem_grade`: Grade in the second semester
   - `Curricular units 2nd sem (without evaluations)`: Number of curricular units in the second semester without evaluations

7. **Economic Indicators:**
   - `Unemployment_rate`: Unemployment rate
   - `Inflation_rate`: Inflation rate
   - `GDP`: Gross Domestic Product

### Target Classes:
The model predicts the academic outcome for each student among three categories:
- `Graduate`: Student successfully completed their program
- `Dropout`: Student discontinued their studies
- `Enrolled`: Student is currently enrolled and continuing their studies

## Methodology

The project employs LightGBM, a gradient boosting framework that uses tree-based learning algorithms, known for its speed, efficiency, and ability to handle large datasets with high-dimensional features.

Key aspects of the methodology:
- **Data Augmentation**: The training data is augmented by combining the competition dataset with the original UCI dataset to improve model generalization
- **Hyperparameter Tuning**: Carefully tuned LightGBM parameters including learning rate (0.05), max depth (25), and number of leaves (80) for optimal performance
- **Cross-Validation**: K-Fold cross-validation with 10 splits is employed to ensure robust performance estimates and prevent overfitting
- **Early Stopping**: Training uses early stopping with 50 rounds to prevent overfitting and reduce training time
- **Multi-class Classification**: The model uses multi-class log loss as the objective function to optimize for three-class prediction

The LightGBM model is configured with the following key parameters:
- **n_estimators**: 9000 (with early stopping)
- **learning_rate**: 0.05 for gradual learning
- **max_depth**: 25 to capture complex patterns
- **num_leaves**: 80 for model complexity
- **subsample**: 0.70 for regularization
- **min_child_samples**: 50 to prevent overfitting

## Results

The LightGBM model demonstrates strong performance in predicting student academic outcomes:
- Overall validation accuracy of approximately **83.1%** across all folds
- Consistent performance across different folds, with validation accuracies ranging from 82.5% to 84.0%
- The model was validated using 10-fold cross-validation to ensure robustness and generalizability
- Individual fold accuracies demonstrate stable model performance across different data splits

The cross-validation results show that the model generalizes well to unseen data and maintains consistent prediction quality across various student populations.

## Conclusion

The academic success prediction system demonstrates the effectiveness of LightGBM in handling multi-class classification problems with high-dimensional features. The combination of careful hyperparameter tuning, data augmentation with the original dataset, and rigorous cross-validation provides a robust solution for predicting student academic outcomes. The model achieves strong accuracy (83.1%) in distinguishing between graduates, dropouts, and enrolled students, which can be valuable for educational institutions to identify at-risk students and provide timely interventions. Future work may explore additional feature engineering (such as interaction features between academic performance and financial factors), ensemble methods combining multiple algorithms, or incorporating temporal patterns in student performance to further improve prediction accuracy.

## Installation

To run the code, ensure you have the following Python packages installed:

```bash
pip install pandas numpy scikit-learn lightgbm
```
