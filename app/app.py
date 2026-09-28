import streamlit as st
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


st.set_page_config(
    page_title="AI Cyber Threat Detection",
    page_icon="🛡️",
    layout="wide"
)


# --------------------------------------------------
# PAGE HEADER
# --------------------------------------------------

st.title("🛡️ AI Cyber Threat Detection System")

st.write(
    "AI-powered network traffic analysis and cyber threat classification."
)

st.divider()


# --------------------------------------------------
# LOAD TRAINING DATA
# --------------------------------------------------

@st.cache_resource
def train_model():

    data = pd.read_csv(
        "data/sample_network_traffic.csv"
    )

    X = data.drop(columns=["label"])
    y = data["label"]

    categorical_features = [
        "protocol",
        "service"
    ]

    numeric_features = [
        "duration",
        "src_bytes",
        "dst_bytes",
        "failed_logins",
        "connection_count"
    ]

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "categorical",
                OneHotEncoder(handle_unknown="ignore"),
                categorical_features
            ),
            (
                "numeric",
                "passthrough",
                numeric_features
            )
        ]
    )

    model = Pipeline(
        steps=[
            (
                "preprocessor",
                preprocessor
            ),
            (
                "classifier",
                RandomForestClassifier(
                    n_estimators=200,
                    random_state=42
                )
            )
        ]
    )

    model.fit(X, y)

    return model, data


model, training_data = train_model()


# --------------------------------------------------
# DASHBOARD METRICS
# --------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "System Status",
        "ONLINE"
    )

with col2:
    st.metric(
        "Training Records",
        len(training_data)
    )

with col3:
    st.metric(
        "Threat Classes",
        training_data["label"].nunique()
    )


st.divider()


# --------------------------------------------------
# THREAT DISTRIBUTION
# --------------------------------------------------

st.subheader("📊 Threat Distribution")

threat_counts = training_data["label"].value_counts()

st.bar_chart(threat_counts)


# --------------------------------------------------
# FILE UPLOAD
# --------------------------------------------------

st.subheader("🔍 Analyze Network Traffic")

uploaded_file = st.file_uploader(
    "Upload a CSV network traffic file",
    type=["csv"]
)


if uploaded_file is not None:

    try:

        data = pd.read_csv(uploaded_file)

        required_columns = [
            "duration",
            "protocol",
            "service",
            "src_bytes",
            "dst_bytes",
            "failed_logins",
            "connection_count"
        ]

        missing_columns = [
            column
            for column in required_columns
            if column not in data.columns
        ]

        if missing_columns:

            st.error(
                "Missing columns: "
                + ", ".join(missing_columns)
            )

        else:

            st.success(
                "Network traffic file loaded successfully."
            )

            st.subheader("📋 Uploaded Data")

            st.dataframe(
                data,
                use_container_width=True
            )

            predictions = model.predict(data)

            data["predicted_threat"] = predictions

            st.subheader("🚨 Threat Analysis")

            st.dataframe(
                data,
                use_container_width=True
            )

            st.subheader("📈 Detection Summary")

            prediction_counts = (
                pd.Series(predictions)
                .value_counts()
            )

            st.bar_chart(
                prediction_counts
            )

            st.success(
                f"Analyzed {len(data)} network connections."
            )

    except Exception as error:

        st.error(
            f"Unable to analyze the file: {error}"
        )


else:

    st.info(
        "Upload a CSV file to begin AI-based threat detection."
    )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "AI Cyber Threat Detection System • Educational Project"
)
