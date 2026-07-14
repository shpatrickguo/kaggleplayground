# Predicting Student Health Risk

Monitoring and modeling student health trajectories is essential for advancing early risk detection and preventive care. The dataset provides longitudinal observations encompassing lifestyle behaviors, physiological indicators, and psychological factors, offering a multidimensional foundation for analyzing determinants of well‑being in college populations. By examining temporal variation in these attributes, predictive modeling can contribute to a deeper understanding of health disparities, behavioral influences, and intervention effectiveness.

Yao Yan, Walter Reade, Elizabeth Park. Predicting Student Health Risk. https://kaggle.com/competitions/playground-series-s6e7, 2026. Kaggle.

## About the data

The data consists of `690088` student health records generated from the [College Student Health Behavior Dataset](https://www.kaggle.com/datasets/ziya07/college-student-health-behavior-dataset), which is modeled on large‑scale health studies of college populations.  Each record represents a time‑stamped observation describing lifestyle behaviors, physiological measurements, and psychological indicators. The dataset includes `13` feature columns and `1` target column (`health_condition`), which classifies each student as fit, at‑risk, or unhealthy.

| **Field** | **Description** |
| --- | --- |
| **[health_condition](ca://s?q=Explain_health_condition_label)** | Target label indicating overall health status (fit, at‑risk, unhealthy) |
| **[sleep_duration](ca://s?q=Explain_sleep_duration_feature)** | Total hours of sleep per day |
| **[heart_rate](ca://s?q=Explain_heart_rate_feature)** | Average resting heart rate (bpm) |
| **[bmi](ca://s?q=Explain_BMI_feature)** | Body Mass Index derived from height and weight |
| **[calorie_expenditure](ca://s?q=Explain_calorie_expenditure_feature)** | Estimated daily calories burned |
| **[step_count](ca://s?q=Explain_step_count_feature)** | Number of steps taken per day |
| **[exercise_duration](ca://s?q=Explain_exercise_duration_feature)** | Minutes spent exercising daily |
| **[water_intake](ca://s?q=Explain_water_intake_feature)** | Daily water consumption (liters) |
| **[diet_type](ca://s?q=Explain_diet_type_feature)** | Categorical diet classification (balanced, high‑carb, high‑fat, etc.) |
| **[stress_level](ca://s?q=Explain_stress_level_feature)** | Self‑reported stress score |
| **[sleep_quality](ca://s?q=Explain_sleep_quality_feature)** | Subjective sleep quality rating |
| **[physical_activity_level](ca://s?q=Explain_physical_activity_level_feature)** | Overall activity level category |
| **[smoking_alcohol](ca://s?q=Explain_smoking_alcohol_feature)** | Combined indicator of smoking and alcohol habits |
| **[gender](ca://s?q=Explain_gender_feature)** | Student gender category |

## Feature Engineering

Feature engineering was applied to convert raw behavioral and physiological measurements into more informative predictors of student health. I created composite indicators for sleep efficiency, activity intensity, hydration balance, and stress interactions, along with nonlinear BMI and heart‑rate transformations. Categorical attributes such as diet type and gender were encoded to ensure they could be effectively used by machine‑learning models.

## Evaluation Metric: Balanced Accuracy

Balanced accuracy measures how well a classifier performs across all classes by giving each class equal weight, regardless of class imbalance. It is defined as the average recall across all \(K\) classes:

$\text{Balanced Accuracy} = \frac{1}{K} \sum_{i=1}^{K} \text{Recall}_i$

where

$\text{Recall}_i = \frac{\text{TP}_i}{\text{TP}_i + \text{FN}_i}.$

This metric is more effective than standard accuracy for imbalanced datasets because it prevents majority classes from dominating the score and ensures that minority classes contribute equally to the evaluation.

## Modelling

I selected XGBoost, LightGBM, and CatBoost because gradient‑boosted tree models are the strongest choice for structured tabular data, especially when nonlinear relationships and engineered interaction features are present. These methods handle mixed numeric and categorical inputs, are robust to outliers, and work well without feature scaling. Each model adds a different strength: XGBoost provides stability and strong regularization, LightGBM trains quickly and captures deep feature interactions, and CatBoost handles categorical structure effectively and produces well‑calibrated probabilities. Together, they form a reliable and complementary ensemble for this task.
