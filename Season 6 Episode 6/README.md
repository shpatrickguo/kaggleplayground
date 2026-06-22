# Predicting Stellar Class

Stellar classification is the process of identifying objects by the spectral patterns in their light. By examining properties such as temperature, composition, and distance, we gain insight into how stars, galaxies, and quasars form and evolve. Effective classification lets us map large surveys, compare objects consistently, and study the structure and history of the universe.

## About the data

The data consists of `577347` generated from [observations of space taken by the SDSS (Sloan Digital Sky Survey)](https://www.kaggle.com/datasets/fedesoriano/stellar-classification-dataset-sdss17/data). Every observation is described by `10` feature columns and 1 class column which identifies it to be either a star, galaxy or quasar.

| **Field** | **Description** |
| --- | --- |
| **alpha** | Right Ascension angle (J2000 epoch) |
| **delta** | Declination angle (J2000 epoch) |
| **u** | Ultraviolet filter magnitude in the SDSS photometric system |
| **g** | Green filter magnitude |
| **r** | Red filter magnitude |
| **i** | Near‑infrared filter magnitude |
| **z** | Infrared filter magnitude |
| **redshift** | Redshift value based on wavelength stretching |
| **spectral_type** | Spectral classification derived from the object’s spectrum |
| **galaxy_population** | Galaxy population category (e.g., early‑type, late‑type) |
| **class** | Object class label (galaxy, star, or quasar) |

## EDA 

To understand how each feature relates to the target class, I used Cramér’s V for the categorical features and Mutual Information (MI) for the numeric features. 

The results show two very strong categorical predictors (`galaxy_population`, `spectral_type`) and one very strong numeric predictor (`redshift`, while the photometric magnitudes (`u`, `g`, `r`, `i`, `z`) provide moderate signal and sky coordinates (`alpha`, `delta`) contribute weak signal. This pattern is typical of SDSS‑style astronomy datasets.

These findings guide the feature engineering:

- Color indices and magnitude ratios strengthen the moderate photometric features by capturing nonlinear color–color relationships.
- Sin/cos encodings for alpha and delta avoid angular discontinuities and extract positional structure.
- Log‑scaled and zero‑flag variants of redshift capture both continuous and discrete behavior.

## Feature Engineering

- Transform raw photometric measurements into color indices and magnitude ratios to capture nonlinear spectral and temperature differences between object types.
- Encode sky coordinates using sin/cos transformations to handle angular circularity and preserve positional structure.
- Add log‑scaled and zero‑flag variants of redshift to separate stellar objects from extragalactic ones and model both continuous and discrete behavior.

## Modeling

1. Selected tree‑based models because they are well‑suited to structured tabular data and can naturally capture nonlinear relationships present in the engineered astronomical features. Methods such as Random Forest, XGBoost, and LightGBM handle mixed feature types, are robust to outliers, and perform strongly without requiring feature scaling.

2. Applied hyperparameter tuning to optimize model complexity, regularization, and sampling parameters, ensuring that each model generalized well under the balanced‑accuracy metric.

3. Combined the tuned models using a weighted soft‑voting ensemble, allowing models with higher validation balanced accuracy to contribute more strongly to the final prediction and improving overall robustness.

## Evaluation Metric: Balanced Accuracy

Balanced accuracy measures how well a classifier performs across all classes by giving each class equal weight, regardless of class imbalance. It is defined as the average recall across all \(K\) classes:

$\text{Balanced Accuracy} = \frac{1}{K} \sum_{i=1}^{K} \text{Recall}_i$

where

$\text{Recall}_i = \frac{\text{TP}_i}{\text{TP}_i + \text{FN}_i}.$

This metric is more effective than standard accuracy for imbalanced datasets because it prevents majority classes from dominating the score and ensures that minority classes contribute equally to the evaluation.
