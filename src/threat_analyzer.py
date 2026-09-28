import pandas as pd


THREAT_SEVERITY = {
    "normal": "LOW",
    "probe": "MEDIUM",
    "r2l": "HIGH",
    "dos": "CRITICAL"
}


def analyze_threat(model, network_data):
    """
    Predict the threat type and assign a severity level.
    """

    if not isinstance(network_data, pd.DataFrame):
        network_data = pd.DataFrame(network_data)

    predictions = model.predict(network_data)

    results = network_data.copy()

    results["predicted_threat"] = predictions

    results["severity"] = [
        THREAT_SEVERITY.get(
            threat,
            "UNKNOWN"
        )
        for threat in predictions
    ]

    return results


def get_threat_summary(results):
    """
    Return a summary of detected threats.
    """

    return results["predicted_threat"].value_counts()


if __name__ == "__main__":
    print("🛡️ Threat Analyzer")
    print("Threat analysis module ready.")
