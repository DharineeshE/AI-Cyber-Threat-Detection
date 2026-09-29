import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

from src.unsw_model import (
    load_unsw_dataset,
    prepare_unsw_dataset,
    build_unsw_model
)


DATA_PATH = "data/UNSW_NB15_training-set.csv"
MODEL_PATH = "models/unsw_nb15_model.pkl"


def train_unsw_model():

    print("🛡️ Loading UNSW-NB15 dataset...")

    data = load_unsw_dataset(DATA_PATH)

    print(f"Original dataset shape: {data.shape}")

    # Use a manageable stratified sample
    if len(data) > 30000:
        data, _ = train_test_split(
            data,
            train_size=30000,
            random_state=42,
            stratify=data["attack_cat"]
        )

    print(f"Training dataset shape: {data.shape}")

    X, y, preprocessor = prepare_unsw_dataset(data)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    print("Building machine learning pipeline...")

    model = build_unsw_model(preprocessor)

    print("Training Random Forest model...")

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    print("\n==============================")
    print("UNSW-NB15 MODEL RESULTS")
    print("==============================")

    print(f"Accuracy: {accuracy:.2%}")

    print("\nClassification Report:")

    print(
        classification_report(
            y_test,
            predictions,
            zero_division=0
        )
    )

    os.makedirs("models", exist_ok=True)

    joblib.dump(
        model,
        MODEL_PATH
    )

    print(
        f"\n✅ Model saved to: {MODEL_PATH}"
    )


if __name__ == "__main__":
    train_unsw_model()
