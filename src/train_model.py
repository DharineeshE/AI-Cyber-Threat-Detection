import os
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

from model_utils import build_threat_model


DATA_PATH = "data/sample_network_traffic.csv"


def train_model():
    """Train and evaluate the cyber threat detection model."""

    data = pd.read_csv(DATA_PATH)

    X = data.drop(columns=["label"])
    y = data["label"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=42,
        stratify=y
    )

    model = build_threat_model()

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    print(f"Model Accuracy: {accuracy:.2%}")

    print("\nClassification Report:")
    print(
        classification_report(
            y_test,
            predictions,
            zero_division=0
        )
    )

    return model


if __name__ == "__main__":
    print("🛡️ AI Cyber Threat Detection")
    print("Training model...")

    trained_model = train_model()

    print("\n✅ Model training completed successfully.")
