"""CLI entry point. Run from the project root."""
import argparse
import json
from pathlib import Path
from src.data import load_dataset
from src.features import prepare_data, engineer_features
from src.train import train_model
from src.predict import predict_one
from src.visualize import create_plots

ROOT = Path(__file__).resolve().parent

def main():
    parser = argparse.ArgumentParser(description="AI-Powered Predictive Maintenance demo")
    parser.add_argument("command", choices=["train", "predict", "all"], help="Action to run")
    parser.add_argument("--csv", default=None, help="Optional path to a UCI AI4I-compatible CSV")
    parser.add_argument("--air-temp", type=float, default=300.0)
    parser.add_argument("--process-temp", type=float, default=312.0)
    parser.add_argument("--rpm", type=float, default=1200.0)
    parser.add_argument("--torque", type=float, default=65.0)
    parser.add_argument("--wear", type=float, default=220.0)
    args = parser.parse_args()

    if args.command in ("train", "all"):
        raw = load_dataset(args.csv)
        cleaned = prepare_data(raw)
        model, metrics, test_predictions = train_model(raw)
        create_plots(cleaned, test_predictions)
        print("\nTRAINING COMPLETE")
        print(json.dumps({k: v for k, v in metrics.items() if k != "classification_report"}, indent=2))
        print("\nSaved model: models/predictive_maintenance_model.joblib")
        print("Saved metrics: outputs/metrics.json")
        print("Saved plots: images/")
    if args.command in ("predict", "all"):
        result = predict_one(
            args.air_temp, args.process_temp, args.rpm, args.torque, args.wear
        )
        print("\nPREDICTION")
        print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
