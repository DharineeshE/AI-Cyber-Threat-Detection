import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder


def train_threat_model(data, target_column):
    """Train a Random Forest model for cyber threat classification."""

    data = data.copy()

    # Convert text columns into numbers
    for column in data.select_dtypes(include=["object"]).columns:
        encoder = LabelEncoder()
        data[column] = encoder.fit_transform(data[column].astype(str))

    X = data.drop(columns=[target_column])
    y = data[target_column]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    print(f"Model Accuracy: {accuracy:.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, predictions))

    return model


if __name__ == "__main__":
    print("Cyber Threat Detection - Model Training")
