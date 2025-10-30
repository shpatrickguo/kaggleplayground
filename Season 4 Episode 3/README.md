# Steel Plate Defect Prediction with Ensemble Learning

## Executive Summary

This project presents a steel plate defect prediction system built for a multi-label classification task derived from the Steel Plates Faults dataset from UCI. The dataset was generated using a deep learning model trained on the original UCI dataset and includes features related to steel plate characteristics and defect locations. The goal is to predict the probability of seven different types of defects that can occur in steel plates. To tackle this challenge, the approach integrates an ensemble of XGBoost and LightGBM models using a weighted voting classifier, with individual ROC AUC scores calculated for each defect class and then averaged together to get an overall AUC score. This evaluation metric was chosen to emphasize the accurate ranking of defects across multiple categories.

## Data

The dataset is sourced from Kaggle's Playground Series S4E3 competition and is based on the [Steel Plates Faults dataset](https://archive.ics.uci.edu/dataset/198/steel+plates+faults) from UCI. The data includes 27 features describing various characteristics of steel plates and their defects.

### Features:
1. **Location Features:**
   - `X_Minimum`: The minimum x-coordinate of the fault
   - `X_Maximum`: The maximum x-coordinate of the fault
   - `Y_Minimum`: The minimum y-coordinate of the fault
   - `Y_Maximum`: The maximum y-coordinate of the fault

2. **Size Features:**
   - `Pixels_Areas`: Area of the fault in pixels
   - `X_Perimeter`: Perimeter along the x-axis of the fault
   - `Y_Perimeter`: Perimeter along the y-axis of the fault

3. **Luminosity Features:**
   - `Sum_of_Luminosity`: Sum of luminosity values in the fault area
   - `Minimum_of_Luminosity`: Minimum luminosity value in the fault area
   - `Maximum_of_Luminosity`: Maximum luminosity value in the fault area

4. **Material and Index Features:**
   - `TypeOfSteel_A300`: Type of steel (A300)
   - `TypeOfSteel_A400`: Type of steel (A400)
   - `Steel_Plate_Thickness`: Thickness of the steel plate
   - Various index values: `Edges_Index`, `Empty_Index`, `Square_Index`, `Outside_X_Index`, `Edges_X_Index`, `Edges_Y_Index`, `Outside_Global_Index`

5. **Logarithmic Features:**
   - `LogOfAreas`: Logarithm of the area of the fault
   - `Log_X_Index`, `Log_Y_Index`: Logarithmic indices related to X and Y coordinates

6. **Statistical Features:**
   - `Orientation_Index`: Index describing orientation
   - `Luminosity_Index`: Index related to luminosity
   - `SigmoidOfAreas`: Sigmoid function applied to areas

### Target Classes:
The model predicts probabilities for seven different types of steel plate defects:
- `Pastry`
- `Z_Scratch`
- `K_Scatch`
- `Stains`
- `Dirtiness`
- `Bumps`
- `Other_Faults`

## Methodology

The project employs an ensemble learning approach, combining the strengths of two gradient boosting models:

1. **XGBoost**: A gradient boosting framework that is efficient and effective for classification tasks, known for its regularization capabilities and handling of sparse data.

2. **LightGBM**: A gradient boosting framework that uses tree-based learning algorithms, known for its speed, efficiency, and ability to handle large datasets with categorical features.

For each of the seven defect types, separate models are trained and optimized:
- Hyperparameters for both XGBoost and LightGBM are tuned using Optuna for optimal performance
- Models are trained using Repeated Stratified K-Fold cross-validation (10 splits, 10 repeats) to ensure robust performance estimates
- The ensemble combines XGBoost and LightGBM predictions using a **VotingClassifier** with soft voting
- Weights for the voting classifier are calculated based on the mean ROC AUC scores of each model across all folds, ensuring that better-performing models have more influence

The ensemble approach allows the system to leverage the complementary strengths of both algorithms, resulting in more robust and accurate predictions across all defect categories.

## Results

The ensemble model demonstrates strong performance in predicting steel plate defects:
- Individual ROC AUC scores are calculated for each of the seven defect classes
- The mean ROC AUC scores across all folds are used to determine optimal model weights
- The weighted ensemble approach ensures that each model contributes proportionally to its performance
- The model's performance was validated using repeated stratified k-fold cross-validation to ensure robustness and generalizability

## Conclusion

The steel plate defect prediction system demonstrates the effectiveness of ensemble learning in handling multi-label classification problems. The combination of XGBoost and LightGBM with weighted soft voting provides a robust solution for identifying various types of steel plate defects. The use of repeated stratified k-fold cross-validation and hyperparameter optimization ensures that the models generalize well to unseen data. Future work may explore additional feature engineering, deep learning approaches, or incorporating domain-specific knowledge to further improve model performance.

## Installation

To run the code, ensure you have the following Python packages installed:

```bash
pip install pandas numpy scikit-learn xgboost lightgbm optuna matplotlib seaborn lazypredict h2o
```
