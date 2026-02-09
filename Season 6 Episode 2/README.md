# Predicting Heart Disease

Predicting heart disease likelihood enables early interventions that save lives and ease healthcare burdens. By analyzing key clinical indicators like age, chest pain type, blood pressure, cholesterol, and stress test results, etc., models can assist identifying high-risk patients for targeted prevention. These insights guide personalized care plans and optimize population-level cardiovascular outcomes.

Yao Yan, Walter Reade, Elizabeth Park. Predicting Heart Disease. https://kaggle.com/competitions/playground-series-s6e2, 2026. Kaggle.

## About the data

| Column | Description |
|--------|-------------|
| **Age** 🧓 | Age of the patient (in years) |
| **Sex** 🚹 | Gender of the patient (1 = Male, 0 = Female) |
| **Chest pain type** 💔 | Type of chest pain: 1=Typical angina, 2=Atypical angina, 3=Non-anginal pain, 4=Asymptomatic |
| **BP** 💉 | Resting blood pressure (mm Hg) |
| **Cholesterol** 🧈 | Serum cholesterol level (mg/dL) |
| **FBS over 120** 🍬 | Fasting blood sugar > 120 mg/dL (1 = True, 0 = False) |
| **EKG results** 📈 | Resting electrocardiogram results: 0=Normal, 1=ST-T wave abnormality, 2=Left ventricular hypertrophy |
| **Max HR** ❤️ | Maximum heart rate achieved |
| **Exercise angina** 🏃 | Exercise-induced angina (1 = Yes, 0 = No) |
| **ST depression** 📉 | ST depression induced by exercise relative to rest |
| **Slope of ST** ⛰️ | Slope of the peak exercise ST segment |
| **Number of vessels fluro** 🩸 | Number of major vessels (0–3) colored by fluoroscopy |
| **Thallium** 🧬 | Thallium stress test result (categorical medical indicator) |
| **Heart Disease** 🎯 | Target: Presence (❤️) or Absence (💚) of heart disease |

### Target Variable

Heart disease (boolean, presence = 1, absence = 0). 

## Modelling

For this classification task, we're using XGBoost because tree-based gradient boosting models excel at capturing nonlinear relationships and complex feature interactions in tabular data Its built-in regularization and early stopping also make it robust against overfitting. 

To push accuracy further, we're ensembling it with LightGBM and CatBoost. Their complementary splitting strategies and inductive biases reduce variance and blind spots, giving us a more stable, high-performing prediction.
