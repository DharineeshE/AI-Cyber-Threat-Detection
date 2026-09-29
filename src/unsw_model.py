import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier


CATEGORICAL_FEATURES = [
    "proto",
    "service",
    "state"
]


def load_unsw_dataset(file_path):
    """Load the UNSW-NB15 training dataset."""

    data = pd.read_csv(file_path)

    return data


def prepare_unsw_dataset(data):
    """
    Prepare UNSW-NB15 data for multiclass
    attack-category classification.
    """

    data = data.copy()

    # Remove unnecessary identifier
    if "id" in data.columns:
        data = data.drop(columns=["id"])

    # Remove rows without a target category
    data = data.dropna(subset=["attack_cat"])

    # Clean attack category text
    data["attack_cat"] = (
        data["attack_cat"]
        .astype(str)
        .str.strip()
    )

    # Separate target
    X = data.drop(
        columns=["attack_cat", "label"],
        errors="ignore"
    )

    y = data["attack_cat"]

    categorical_features = [
        column
        for column in CATEGORICAL_FEATURES
        if column in X.columns
    ]

    numeric_features = [
        column
        for column in X.columns
        if column not in categorical_features
    ]

    numeric_pipeline = Pipeline(
        steps=[
            (
                "imputer",
                SimpleImputer(strategy="median")
            )
        ]
    )

    categorical_pipeline = Pipeline(
        steps=[
            (
                "imputer",
                SimpleImputer(
                    strategy="most_frequent"
                )
            ),
            (
                "encoder",
                OneHotEncoder(
                    handle_unknown="ignore"
                )
            )
        ]
    )

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "numeric",
                numeric_pipeline,
                numeric_features
            ),
            (
                "categorical",
                categorical_pipeline,
                categorical_features
            )
        ]
    )

    return X, y, preprocessor


def build_unsw_model(preprocessor):
    """Create the UNSW-NB15 Random Forest model."""

    model = Pipeline(
        steps=[
            (
                "preprocessor",
                preprocessor
            ),
            (
                "classifier",
                RandomForestClassifier(
                    n_estimators=100,
                    random_state=42,
                    class_weight="balanced",
                    n_jobs=-1
                )
            )
        ]
    )

    return model


if __name__ == "__main__":
    print("🛡️ UNSW-NB15 model module ready.")
