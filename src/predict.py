"""Make one illustrative prediction from supplied sensor values."""
import pandas as pd
from .train import load_model
from .features import engineer_features

def predict_one(air_temperature_k: float, process_temperature_k: float,
                rotational_speed_rpm: float, torque_nm: float,
                tool_wear_min: float, threshold: float = 0.5) -> dict:
    row = pd.DataFrame([{
        "air_temperature_k": air_temperature_k,
        "process_temperature_k": process_temperature_k,
        "rotational_speed_rpm": rotational_speed_rpm,
        "torque_nm": torque_nm,
        "tool_wear_min": tool_wear_min,
    }])
    row = engineer_features(row)
    model, feature_names = load_model()
    probability = float(model.predict_proba(row[feature_names])[:, 1][0])
    label = int(probability >= threshold)
    if probability >= 0.70:
        alert = "HIGH RISK — inspect the machine promptly"
    elif probability >= 0.40:
        alert = "MEDIUM RISK — review condition and monitor"
    else:
        alert = "LOW RISK — continue routine monitoring"
    return {
        "failure_probability": probability,
        "predicted_failure": label,
        "prediction_label": "Failure risk" if label else "No failure risk",
        "alert": alert,
        "threshold": threshold,
        "disclaimer": "Model output is an educational estimate, not a safety decision."
    }
