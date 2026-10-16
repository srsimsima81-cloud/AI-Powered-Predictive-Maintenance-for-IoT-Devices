"""Train, evaluate, and save a baseline predictive-maintenance model."""
from pathlib import Path
import json
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report, roc_auc_score
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

from .data import FEATURES, TARGET
from .features import prepare_data, engineer_features

ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = ROOT / "models" / "predictive_maintenance_model.joblib"
METRICS_PATH = ROOT / "outputs" / "metrics.json"
PREDICTIONS_PATH = ROOT / "outputs" / "test_predictions.csv"

MODEL_FEATURES = FEATURES + [
    "temperature_difference_k", "power_proxy", "wear_per_1000_rpm"
]

def train_model(raw_df: pd.DataFrame):
    df = engineer_features(prepare_data(raw_df))
    X = df[MODEL_FEATURES]
    y = df[TARGET]

    if y.nunique() < 2:
        raise ValueError("Training data must contain both failure labels (0 and 1).")

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("model", RandomForestClassifier(
            n_estimators=250,
            max_depth=12,
            min_samples_leaf=2,
            class_weight="balanced",
            random_state=42,
            n_jobs=-1,
        )),
    ])
    pipeline.fit(X_train, y_train)

    predictions = pipeline.predict(X_test)
    probabilities = pipeline.predict_proba(X_test)[:, 1]
    metrics = {
        "rows_after_cleaning": int(len(df)),
        "train_rows": int(len(X_train)),
        "test_rows": int(len(X_test)),
        "failure_rate": float(y.mean()),
        "accuracy": float(accuracy_score(y_test, predictions)),
        "precision": float(precision_score(y_test, predictions, zero_division=0)),
        "recall": float(recall_score(y_test, predictions, zero_division=0)),
        "f1_score": float(f1_score(y_test, predictions, zero_division=0)),
        "roc_auc": float(roc_auc_score(y_test, probabilities)) if y_test.nunique() == 2 else None,
        "confusion_matrix_labels_0_1": confusion_matrix(y_test, predictions, labels=[0, 1]).tolist(),
        "classification_report": classification_report(
            y_test, predictions, labels=[0, 1],
            target_names=["no_failure", "failure"],
            output_dict=True, zero_division=0
        ),
        "note": "Synthetic-demo metrics are not evidence of real-world performance."
    }

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    METRICS_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump({"pipeline": pipeline, "feature_names": MODEL_FEATURES}, MODEL_PATH)
    METRICS_PATH.write_text(json.dumps(metrics, indent=2))
    out = X_test.copy()
    out["actual_failure"] = y_test.to_numpy()
    out["predicted_failure"] = predictions
    out["failure_probability"] = probabilities
    out.to_csv(PREDICTIONS_PATH, index=False)

    return pipeline, metrics, out

def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError("Model not found. Run `python main.py train` first.")
    saved = joblib.load(MODEL_PATH)
    return saved["pipeline"], saved["feature_names"]
