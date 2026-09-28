import pandas as pd
from sklearn.preprocessing import LabelEncoder


def encode_categorical_features(data):
    """Convert categorical columns into numerical values."""
    data = data.copy()

    categorical_columns = data.select_dtypes(include=["object"]).columns

    for column in categorical_columns:
        encoder = LabelEncoder()
        data[column] = encoder.fit_transform(data[column].astype(str))

    return data


def separate_features_target(data, target_column):
    """Separate input features and target variable."""
    X = data.drop(columns=[target_column])
    y = data[target_column]

    return X, y


if __name__ == "__main__":
    print("Cyber Threat Detection - Feature Engineering")
