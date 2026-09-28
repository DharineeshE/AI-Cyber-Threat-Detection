import streamlit as st

st.set_page_config(
    page_title="AI Cyber Threat Detection",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ AI Cyber Threat Detection System")

st.write(
    "Machine learning-based cybersecurity platform "
    "for detecting and classifying suspicious network activity."
)

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("System Status", "ONLINE")

with col2:
    st.metric("Threats Detected", "0")

with col3:
    st.metric("Model Status", "READY")

st.subheader("🔍 Threat Detection")

uploaded_file = st.file_uploader(
    "Upload network traffic CSV file",
    type=["csv"]
)

if uploaded_file is not None:
    st.success("File uploaded successfully!")

    import pandas as pd

    data = pd.read_csv(uploaded_file)

    st.subheader("📊 Dataset Preview")
    st.dataframe(data.head(10))

    st.subheader("📈 Dataset Information")

    col1, col2 = st.columns(2)

    with col1:
        st.write("Rows:", data.shape[0])

    with col2:
        st.write("Columns:", data.shape[1])
else:
    st.info("Upload a CSV dataset to begin threat analysis.")
