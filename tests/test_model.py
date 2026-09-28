import unittest
import pandas as pd

from src.model_utils import build_threat_model


class TestThreatDetectionModel(unittest.TestCase):

    def setUp(self):
        self.data = pd.read_csv(
            "data/sample_network_traffic.csv"
        )

    def test_dataset_loaded(self):
        self.assertGreater(len(self.data), 0)

    def test_required_columns_exist(self):
        required_columns = {
            "duration",
            "protocol",
            "service",
            "src_bytes",
            "dst_bytes",
            "failed_logins",
            "connection_count",
            "label"
        }

        self.assertTrue(
            required_columns.issubset(
                set(self.data.columns)
            )
        )

    def test_model_can_train(self):
        X = self.data.drop(columns=["label"])
        y = self.data["label"]

        model = build_threat_model()
        model.fit(X, y)

        predictions = model.predict(X)

        self.assertEqual(
            len(predictions),
            len(self.data)
        )


if __name__ == "__main__":
    unittest.main()
