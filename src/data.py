"""Dataset loading and a clearly labelled synthetic sensor-data generator."""
from pathlib import Path
import numpy as np
import pandas as pd

FEATURES = [
    "air_temperature_k",
    "process_temperature_k",
    "rotational_speed_rpm",
    "torque_nm",
    "tool_wear_min",
]
TARGET = "machine_failure"

def make_synthetic_data(n_rows: int = 10000, seed: int = 42) -> pd.DataFrame:
    """
    Generate illustrative machine telemetry for a reproducible demo.
    This is synthetic data, not real sensor measurements.
    The target is generated from a risk rule plus noise, so performance on it
    must not be represented as real-world industrial performance.
    """
    rng = np.random.default_rng(seed)
    air = rng.normal(300.0, 2.0, n_rows).clip(294, 306)
    process = air + rng.normal(10.0, 1.5, n_rows)
    rpm = rng.normal(1500, 180, n_rows).clip(900, 2300)
    torque = rng.normal(40, 10, n_rows).clip(5, 80)
    wear = rng.integers(0, 251, n_rows)

    # Illustrative risk score: high wear/torque and unusual speed/temperature
    # raise failure probability. This is a teaching simulator, not physics.
    score = (
        0.018 * (wear - 125)
        + 0.045 * (torque - 40)
        + 0.012 * (process - 310)
        + 0.004 * (np.abs(rpm - 1500) - 100)
        - 1.1
    )
    probability = 1 / (1 + np.exp(-score))
    labels = rng.binomial(1, probability)

    return pd.DataFrame({
        "air_temperature_k": air,
        "process_temperature_k": process,
        "rotational_speed_rpm": rpm,
        "torque_nm": torque,
        "tool_wear_min": wear,
        TARGET: labels,
        "data_source": "synthetic_demo",
    })

def load_dataset(path: str | Path | None = None) -> pd.DataFrame:
    """
    Load an optional UCI AI4I CSV if supplied; otherwise create demo data.
    UCI AI4I column names are mapped to the common feature names.
    """
    if path:
        df = pd.read_csv(path)
        rename = {
            "Air temperature [K]": "air_temperature_k",
            "Process temperature [K]": "process_temperature_k",
            "Rotational speed [rpm]": "rotational_speed_rpm",
            "Torque [Nm]": "torque_nm",
            "Tool wear [min]": "tool_wear_min",
            "Machine failure": "machine_failure",
        }
        df = df.rename(columns=rename)
        required = FEATURES + [TARGET]
        missing = [c for c in required if c not in df.columns]
        if missing:
            raise ValueError(f"CSV is missing required columns: {missing}")
        df = df[required].copy()
        df["data_source"] = "uci_ai4i"
        return df
    return make_synthetic_data()
