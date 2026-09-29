import os
import joblib
import pandas as pd

from src.model_utils import build_threat_model


DATA_PATH = "data/sample_network_traffic.csv"
MODEL_PATH = "models/threat_detection_model.pkl"


def save_trained_model():
    """Train the model and save it to the models directory."""

    data = pd.read_csv(DATA_PATH)

    X = data.drop(columns=["label"])
    y = data["label"]

    model = build_threat_model()
    model.fit(X, y)

    os.makedirs("models", exist_ok=True)

    joblib.dump(model, MODEL_PATH)

    print(f"✅ Model saved to: {MODEL_PATH}")


if __name__ == "__main__":
    save_trained_model()
