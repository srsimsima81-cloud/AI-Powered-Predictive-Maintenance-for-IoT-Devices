"""Data validation and feature engineering."""
import pandas as pd
from .data import FEATURES, TARGET

def prepare_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    required = FEATURES + [TARGET]
    missing = [col for col in required if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    for col in FEATURES + [TARGET]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.dropna(subset=required)
    df = df.drop_duplicates()
    df = df[df[TARGET].isin([0, 1])]
    # Basic, conservative range validation; adjust for the actual equipment.
    df = df[
        df["rotational_speed_rpm"].between(0, 10000)
        & df["tool_wear_min"].between(0, 100000)
    ]
    if df.empty:
        raise ValueError("No usable rows remain after cleaning.")
    return df.reset_index(drop=True)

def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """Add simple interpretable features from the available sensor fields."""
    result = df.copy()
    result["temperature_difference_k"] = (
        result["process_temperature_k"] - result["air_temperature_k"]
    )
    result["power_proxy"] = result["torque_nm"] * result["rotational_speed_rpm"]
    result["wear_per_1000_rpm"] = (
        result["tool_wear_min"] / result["rotational_speed_rpm"].clip(lower=1)
    ) * 1000
    return result
