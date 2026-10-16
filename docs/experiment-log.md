# Experiment log

Record each experiment rather than reporting only the best score.

| Date | Dataset | Features | Model | Split strategy | Threshold | Precision | Recall | F1 | Notes |
|---|---|---|---|---|---:|---:|---:|---:|---|
| YYYY-MM-DD | synthetic demo | engineered numeric | Random Forest | stratified random | 0.50 | | | | baseline |

## Questions to investigate
- How does recall change when the decision threshold moves from 0.5 to 0.3?
- Does Logistic Regression perform differently from Random Forest?
- What happens when the data contains missing values or noisy readings?
- Does performance change when a model is tested on a different machine or time period?
