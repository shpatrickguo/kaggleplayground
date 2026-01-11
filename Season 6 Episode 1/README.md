# Student Test Score Prediction

This notebook predicts student exam scores using synthetic data generated from a deep learning model trained on real student performance records. The dataset includes demographic, academic, and behavioral features for regression modeling with RMSE evaluation.

## About the Data

[Competition data](https://www.kaggle.com/competitions/playground-series-s6e1/data) comes from Playground Series S6E1, generated to mimic the original [Exam Score Prediction](https://www.kaggle.com/datasets/kundanbedmutha/exam-score-prediction-dataset) dataset.​

- Rows: 630000 train samples
- Features: 12 (mix of numeric and categorical)

| **Column Name**     | **Description**                                                                 |
|----------------------|---------------------------------------------------------------------------------|
| `id`                | A unique identifier assigned to each student record.                            |
| `age`               | The age of the student, represented in years.                                   |
| `gender`            | The gender of the student (e.g., male, female, non-binary, unspecified).        |
| `course`            | The course or academic program the student is enrolled in.                      |
| `study_hours`       | Average number of hours the student studies per day.                            |
| `class_attendance`  | Percentage of attended classes over the total number of scheduled classes.       |
| `internet_access`   | Indicates whether the student has reliable internet access (e.g., yes/no or scale). |
| `sleep_hours`       | Average number of hours of sleep the student gets per night.                    |
| `sleep_quality`     | Perceived quality of sleep, often measured on a numerical or categorical scale.  |
| `study_method`      | The primary study approach used by the student (e.g., solo, group, mixed).       |
| `facility_rating`   | Rating of the institution’s facilities as perceived by the student.              |
| `exam_difficulty`   | The perceived or assigned difficulty level of the exam attempted.                |
| `exam_score`        | The final exam score achieved by the student, ranging from 0 to 100.            |

### Target Variable

Exam score (continuous, typically 0-100 range). Higher scores correlate with more study hours and test prep.

## Modelling

CatBoost Regressor was used as the primary model due to its native handling of categorical features without preprocessing and ordered boosting that reduces overfitting, delivering high accuracy with minimal tuning.
