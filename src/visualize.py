
"""Generate plots that can be committed as project evidence."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import ConfusionMatrixDisplay

ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = ROOT / "outputs"
IMAGES = ROOT / "images"


def create_plots(clean_df: pd.DataFrame, predictions: pd.DataFrame):
    OUTPUTS.mkdir(parents=True, exist_ok=True)
    IMAGES.mkdir(parents=True, exist_ok=True)

    # 1. Failure label distribution
    fig, ax = plt.subplots()

    clean_df["machine_failure"].value_counts().sort_index().plot(
        kind="bar", ax=ax
    )

    ax.set_xticks(
        [0, 1],
        ["No failure (0)", "Failure (1)"],
        rotation=0
    )
    ax.set_title("Failure Label Distribution")
    ax.set_ylabel("Number of Records")

    fig.tight_layout()
    fig.savefig(IMAGES / "failure_distribution.png", dpi=150)
    plt.close(fig)

    # 2. Predicted risk versus actual test labels
    fig, ax = plt.subplots()

    ax.scatter(
        predictions["actual_failure"],
        predictions["failure_probability"],
        alpha=0.45
    )
    ax.axhline(0.5, linestyle="--")
    ax.set_xlabel("Actual Label (0 = No Failure, 1 = Failure)")
    ax.set_ylabel("Predicted Failure Probability")
    ax.set_title("Predicted Risk versus Actual Test Labels")

    fig.tight_layout()
    fig.savefig(IMAGES / "risk_predictions.png", dpi=150)
    plt.close(fig)

    # 3. Confusion matrix
    true_labels = predictions["actual_failure"]
    predicted_labels = predictions["predicted_failure"]

    cm = [
        [
            int(((true_labels == 0) & (predicted_labels == 0)).sum()),
            int(((true_labels == 0) & (predicted_labels == 1)).sum())
        ],
        [
            int(((true_labels == 1) & (predicted_labels == 0)).sum()),
            int(((true_labels == 1) & (predicted_labels == 1)).sum())
        ]
    ]

    # Convert the Python list into a NumPy array.
    # Scikit-learn requires an array with a shape attribute.
    cm = np.array(cm)

    fig, ax = plt.subplots()

    ConfusionMatrixDisplay(
        confusion_matrix=cm,
        display_labels=["No Failure", "Failure"]
    ).plot(ax=ax, values_format="d")

    ax.set_title("Confusion Matrix — Held-Out Test Set")

    fig.tight_layout()
    fig.savefig(IMAGES / "confusion_matrix.png", dpi=150)
    plt.close(fig)
