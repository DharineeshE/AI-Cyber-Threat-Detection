import pandas as pd


def load_data(file_path):
    """Load the cybersecurity dataset."""
    try:
        data = pd.read_csv(file_path)
        print("Dataset loaded successfully.")
        print(f"Rows: {data.shape[0]}")
        print(f"Columns: {data.shape[1]}")
        return data
    except FileNotFoundError:
        print("Dataset file not found.")
        return None


def clean_data(data):
    """Basic dataset cleaning."""
    if data is None:
        return None

    data = data.drop_duplicates()
    data = data.dropna()

    return data


if __name__ == "__main__":
    print("Cyber Threat Detection - Data Preprocessing")
