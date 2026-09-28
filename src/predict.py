import pandas as pd


def predict_threat(model, input_data):
    """Predict the threat category for new network data."""

    if not isinstance(input_data, pd.DataFrame):
        input_data = pd.DataFrame(input_data)

    prediction = model.predict(input_data)

    return prediction


if __name__ == "__main__":
    print("Cyber Threat Detection - Prediction Module")
