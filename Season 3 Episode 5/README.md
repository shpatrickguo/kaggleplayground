# Season 3 Episode 5 Tabular Wine Quality Dataset

This project predicts wine quality based on physicochemical tests conducted during the wine certification process. Using a dataset of Portuguese vinho verde samples (both red and white), I built an ensemble of regression models—including Extra Trees, SVC, Random Forest, XGBoost, and LightGBM. Model performance was evaluated using the Quadratic Weighted Kappa (QWK) metric, achieving a final score of 0.53637.

## Data
The dataset consists of 3,199 wine samples sourced from the [UCI machine learning repositor](https://archive.ics.uci.edu/dataset/186/wine+quality) and [Kaggle](https://www.kaggle.com/competitions/playground-series-s3e5/data). It includes features related to both red and white variants of Portuguese "Vinho Verde" wines, originating from the north of Portugal. Each sample is described by 11 physicochemical properties:
- 1 - fixed acidity
- 2 - volatile acidity
- 3 - citric acid
- 4 - residual sugar
- 5 - chlorides
- 6 - free sulfur dioxide
- 7 - total sulfur dioxide
- 8 - density
- 9 - pH
- 10 - sulphates
- 11 - alcohol
Output variable (based on sensory data): 
- 12 - quality (score between 0 and 10)

## Model
The model is an ensemble of regression models, including:
- Extra Trees E(Extremely Randomized Trees) is an ensemble method that builds multiple decision trees using random splits for both features and thresholds, rather than seeking the optimal split at each node.
- Support Vector Classifier (SVC) captures complex, non-linear relationships in data through the use of kernel functions. 
- Random Forest uses an ensemble of decision trees that improves predictive accuracy and robustness by averaging the results of multiple trees built on random subsets of data and features.
- XGBoost is a sequential ensemble method that builds trees to correct the errors of previous trees, optimizing a loss function at each step.
- LightGBM is a gradient boosting framework that grows trees leaf-wise, optimizing for maximum loss reduction.
These models were chosen for their ability to handle complex relationships in the data and their robustness against overfitting. The ensemble approach combines the strengths of each model to improve overall prediction accuracy.

## Evaluation
Model performance was evaluated using the Quadratic Weighted Kappa (QWK) metric, which measures the agreement between predicted and actual quality scores. 

Quadratic Weighted Kappa (QWK) is computed as:

    κ = 1 - (∑₍i,j₎ W[i,j] * O[i,j]) / (∑₍i,j₎ W[i,j] * E[i,j])

Where:
- O[i,j] is the observed count of ratings with actual rating i and predicted rating j,
- E[i,j] is the expected count of ratings for i and j (by chance, given the histograms),
- W[i,j] is the quadratic weight:

      W[i,j] = ((i - j)²) / (N - 1)²

  with N being the number of possible rating categories.

QWK is ideal for evaluating ordinal regression problems like wine quality prediction because it not only measures accuracy but also incorporates the degree of disagreement, giving partial credit for near-misses and penalizing predictions that are far from the true value. The final QWK score achieved by the ensemble model was 0.53637.

## Future Work
Future work could involve:
- Implementing more advanced ensemble techniques or deep learning models to capture complex patterns in the data.
- Investigating the impact of feature engineering techniques, such as polynomial features or interaction terms.
