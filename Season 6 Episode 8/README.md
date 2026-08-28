# Predicting Smartphone Addiction
Playground Series - Season 6 Episode 8

Predicting the smartphone addiction helps identify students whose digital habits may be putting them at risk, allowing earlier intervention and support. By modeling patterns across behaviors like screen time, sleep hours, and stress level, we can uncover which lifestyle factors most strongly contribute to unhealthy usage. These insights enable more targeted wellness strategies and help institutions better understand how daily routines shape long‑term digital well‑being.

Yao Yan, Walter Reade, Elizabeth Park. Predicting Smartphone Addiction. https://kaggle.com/competitions/playground-series-s6e8, 2026. Kaggle.

## About the Data


The data consists of `691369` students generated from the [Smartphone Addiction Prediction Dataset](https://www.kaggle.com/datasets/algozee/smartphone-addiction-prediction-data). Each record represents a describing lifestyle behaviors like screen time, sleep hours, and stress level. The dataset includes 12 feature columns and `1` target column `addicted_label`.

| **Field** | **Description** |
| --- | --- |
| **age** | Student’s age in years. |
| **daily_screen_time_hours** | Total screen time per day across all devices. |
| **social_media_hours** | Hours spent on social media daily. |
| **gaming_hours** | Hours spent gaming each day. |
| **work_study_hours** | Time spent on work or studying per day. |
| **sleep_hours** | Total hours of sleep per night. |
| **notifications_per_day** | Number of notifications received daily. |
| **app_opens_per_day** | How many times apps are opened per day. |
| **weekend_screen_time** | Total screen time accumulated over the weekend. |
| **gender** | Reported gender category. |
| **stress_level** | Self‑reported stress rating. |
| **academic_work_impact** | Whether screen habits affect academic performance. |
| **addicted_label** | Target variable indicating digital addiction (0/1). |

## Preprocessing

Handling missing values:
- Continuous variables were imputed using median substitution, ensuring robustness against skewed distributions
- Categorical fields were imputed using the most‑frequent category, preserving dominant class structure without introducing synthetic categories.

All categorical attributes were label‑encoded to convert nominal values into integer representations. This encoding approach maintains deterministic mappings and is well‑suited for tree‑based learners.

## Modelling

XGBoost was chosen because gradient‑boosted trees consistently excel on structured tabular data and can model complex non‑linear interactions across behavioral features such as screen time, notifications, and social media activity. Its regularization and boosting framework allow it to learn subtle patterns without overfitting. Combined with robust preprocessing and Stratified K‑Fold cross‑validation, XGBoost provides a stable, high‑performing approach.
