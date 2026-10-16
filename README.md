# PREMAINT AI — Predictive Maintenance Intelligence

**An AI-powered predictive maintenance system that analyzes simulated industrial sensor data to estimate machine failure risk.**

PREMAINT AI is a Python-based machine learning project designed to demonstrate how sensor analytics and predictive modeling can support machine condition monitoring. It combines synthetic IoT sensor data, feature engineering, a Random Forest classifier, model evaluation, and an interactive Streamlit dashboard.

> **Disclaimer:** PREMAINT AI is an educational demonstration using simulated sensor data. It is not a certified industrial safety system, and its predictions must not be used to make real-world maintenance or safety decisions.

## Overview

Unexpected equipment failures can lead to downtime, maintenance costs, and operational disruption. Predictive maintenance approaches use equipment data to identify patterns associated with potential failures.

PREMAINT AI demonstrates this workflow by processing machine operating measurements and generating an estimated failure probability through a trained machine learning model.

The project includes a browser-based dashboard where users can adjust sensor readings, configure a classification threshold, and explore the resulting model predictions.

## Key Features

- **Synthetic IoT sensor data:** Generates a dataset of 10,000 machine observations for experimentation.
- **Data preprocessing:** Cleans sensor records and prepares data for modeling.
- **Feature engineering:** Derives additional variables from temperature, rotational speed, torque, and tool wear.
- **Machine learning:** Trains a Random Forest classifier to predict machine failure labels.
- **Risk estimation:** Produces a model-estimated failure probability for an input sample.
- **Adjustable classification threshold:** Allows users to change the probability cutoff used to classify predictions.
- **Interactive dashboard:** Provides sensor controls, diagnostic results, risk indicators, and prediction details.
- **Model evaluation:** Calculates accuracy, precision, recall, F1 score, ROC-AUC, and a confusion matrix.
- **Visual evidence:** Generates plots for failure-label distribution, predicted risk, and model evaluation.
- **Reproducible workflow:** Saves the trained model, evaluation metrics, predictions, and plots locally.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application and machine learning |
| Pandas | Data processing and manipulation |
| NumPy | Numerical operations |
| Scikit-learn | Preprocessing, model training, and evaluation |
| Matplotlib | Evaluation plots |
| Streamlit | Interactive dashboard |
| Joblib | Saving and loading the trained model |
| Git and GitHub | Version control and project hosting |

## Machine Learning Workflow

1. **Data generation:** Create simulated machine sensor measurements and corresponding failure labels.
2. **Data cleaning:** Validate the dataset and prepare the sensor features.
3. **Feature engineering:** Calculate derived features to represent additional relationships between operating measurements.
4. **Data splitting:** Divide the dataset into training and test sets using an 80:20 split.
5. **Model training:** Train a Random Forest classifier using the training dataset.
6. **Evaluation:** Evaluate predictions on the held-out test set.
7. **Model persistence:** Save the trained pipeline for subsequent predictions.
8. **Inference:** Accept sensor readings and estimate failure probability.
9. **Visualization:** Display diagnostic results and model evaluation plots.

### Sensor Features

The model uses the following input measurements:

| Feature | Description |
|---|---|
| Air temperature | Simulated surrounding air temperature, in kelvin |
| Process temperature | Simulated machine process temperature, in kelvin |
| Rotational speed | Machine rotational speed, in RPM |
| Torque | Simulated machine torque, in Nm |
| Tool wear | Accumulated tool wear, in minutes |

Derived features include temperature difference, a torque-speed power proxy, and a wear-to-speed ratio.

These engineered variables are intended for experimentation and do not constitute validated physical measurements of machine health.

## Model Evaluation

The current training run produced the following results on a held-out test set of 2,000 synthetic observations.

| Metric | Result |
|---|---:|
| Training observations | 8,000 |
| Test observations | 2,000 |
| Accuracy | 74.60% |
| Precision | 61.62% |
| Recall | 69.67% |
| F1 score | 65.40% |
| ROC-AUC | 0.8022 |

### Interpretation

- **Accuracy:** The proportion of test observations classified correctly.
- **Precision:** The proportion of predicted failures that correspond to positive failure labels.
- **Recall:** The proportion of positive failure labels correctly identified.
- **F1 score:** The harmonic mean of precision and recall.
- **ROC-AUC:** Measures the model's ability to rank positive examples above negative examples across classification thresholds.

These figures describe the current synthetic-data experiment only. They do not establish how the model would perform on actual industrial machinery. The probability estimates have not been validated or demonstrated to be calibrated for real-world failure probabilities.

## Project Structure

```text
AI-Predictive-Maintenance-IoT/
│
├── data/
│   └── raw/
│
├── docs/
│   ├── architecture.md
│   └── experiment-log.md
│
├── images/
│   ├── failure_distribution.png
│   ├── risk_predictions.png
│   └── confusion_matrix.png
│
├── models/
│   └── predictive_maintenance_model.joblib
│
│
├── outputs/
│   ├── metrics.json
│   └── test_predictions.csv
│
├── src/
│   ├── __init__.py
│   ├── data.py
│   ├── features.py
│   ├── predict.py
│   ├── train.py
│   └── visualize.py
│
├── dashboard.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

*Generated files may appear only after training. The exact contents of the folders can vary depending on the project configuration.*

## Installation and Setup

### Prerequisites

- Python 3.10 or a compatible Python version supported by the dependencies
- pip
- Git (optional, for cloning the repository)

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Predictive-Maintenance-IoT.git
cd AI-Predictive-Maintenance-IoT
```

Replace `YOUR_USERNAME` with your GitHub username and adjust the repository URL if you choose a different repository name.

### 2. Create a virtual environment

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Train the model

```bash
python main.py train
```

This command trains the model and generates the evaluation outputs and visualizations.

### 5. Run predictions

```bash
python main.py predict
```

### 6. Launch the dashboard

```bash
streamlit run dashboard.py
```

Open the local URL displayed in your terminal if the browser does not open automatically.

## Using the Dashboard

1. Start the Streamlit application.
2. Adjust the simulated sensor readings in the sidebar.
3. Set the desired classification threshold.
4. Select **RUN DIAGNOSTIC**.
5. Review the estimated failure probability, predicted class, and alert.
6. Inspect the prediction payload and inputs used.
7. Explore the model evaluation plots.

Changing the classification threshold changes the decision cutoff; it does not retrain the model or change the underlying probability estimate.

The displayed risk bands are interface conventions and should not be interpreted as validated industrial risk categories.

## Generated Outputs

| File | Description |
|---|---|
| `models/predictive_maintenance_model.joblib` | Saved trained model pipeline |
| `outputs/metrics.json` | Model evaluation metrics |
| `outputs/test_predictions.csv` | Test-set predictions and associated scores |
| `images/failure_distribution.png` | Distribution of failure labels |
| `images/risk_predictions.png` | Predicted probability versus actual test labels |
| `images/confusion_matrix.png` | Classification results on the test set |

## Data and Limitations

The default workflow uses synthetic sensor observations and labels generated by the project's data-generation logic.

Consequently:

- The model can learn patterns created by the simulation rather than generalizable industrial failure mechanisms.
- Performance metrics depend on the generated dataset, feature definitions, train/test split, and model configuration.
- Synthetic labels may not represent the complexity of actual machine failures.
- A high predicted probability does not guarantee a future failure.
- A low predicted probability does not guarantee safe operation.
- No real-time hardware integration or industrial deployment is established by this demonstration.

For further experimentation, the project can be extended to use an appropriately licensed, documented real-world dataset, with careful validation and a clearly defined evaluation protocol.

## Future Improvements

- Integrate a documented public industrial predictive-maintenance dataset.
- Compare Random Forest with gradient boosting and other suitable models.
- Add precision-recall curves and threshold analysis.
- Evaluate probability calibration and class-imbalance handling.
- Add time-series analysis and temporal validation where appropriate.
- Introduce model versioning and experiment tracking.
- Add automated tests for preprocessing and inference.
- Explore simulated streaming sensor inputs and anomaly-monitoring workflows.
- Improve accessibility, responsive layouts, and dashboard testing.

## Learning Outcomes

This project demonstrates practical experience with:

- Python-based machine learning workflows.
- Data cleaning and feature engineering.
- Binary classification and model evaluation.
- Model persistence and prediction pipelines.
- Interactive Streamlit application development.
- Data visualization and experiment documentation.
- Git-based project organization and reproducibility.


---

**PREMAINT AI — Exploring predictive maintenance through machine learning and simulated sensor analytics.**