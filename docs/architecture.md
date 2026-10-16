# Architecture and design notes

## Data flow
1. A synthetic sensor generator creates rows of machine operating conditions, or the user supplies an AI4I CSV.
2. Validation removes unusable records and checks target labels.
3. Feature engineering adds temperature difference, a torque-speed power proxy, and a wear-to-speed ratio.
4. A stratified train/test split holds out 20% of records.
5. A scikit-learn pipeline imputes missing numeric values and fits a Random Forest.
6. Metrics and test predictions are written to `outputs/`.
7. Plot images are generated in `images/`.
8. The CLI or Streamlit app scores a new sensor reading and shows a threshold-based alert.

## Why Random Forest?
It handles nonlinear feature relationships, requires little scaling, and offers a reasonable baseline for tabular data. It is not automatically the best model; compare it with Logistic Regression and a gradient-boosted model in a future experiment.

## Target definition
`machine_failure` is a binary label on a row. In the synthetic mode it is generated from an illustrative risk function. In AI4I it is the dataset's machine-failure label. Neither source, by itself, guarantees a real-world prediction horizon such as “failure in the next 24 hours.”
