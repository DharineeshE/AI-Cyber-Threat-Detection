# 🛡️ AI Cyber Threat Detection System

[![Python Project Check](https://github.com/DharineeshE/AI-Cyber-Threat-Detection/actions/workflows/python-check.yml/badge.svg)](https://github.com/DharineeshE/AI-Cyber-Threat-Detection/actions/workflows/python-check.yml)

An AI-powered cybersecurity project that uses machine learning to analyze network traffic and classify predefined cyber-threat categories.

## 🚀 Overview

The **AI Cyber Threat Detection System** demonstrates an end-to-end machine learning workflow for cybersecurity analysis.

The project includes data preprocessing, feature engineering, machine learning classification, threat analysis, severity mapping, security alerts, automated tests, GitHub Actions, and an interactive Streamlit dashboard.

## ✨ Key Features

* 🤖 Machine Learning Threat Classification
* 🔍 Network Traffic Analysis
* 🚨 Automated Security Alerts
* ⚠️ Threat Severity Detection
* 📊 Interactive Threat Visualization
* 📁 CSV Network Traffic Upload
* 🧪 Automated Model Testing
* 🔄 GitHub Actions CI Pipeline
* 🖥️ Streamlit Cybersecurity Dashboard
* 🧠 Model Documentation with Model Card

## 🎯 Objectives

* Analyze network traffic data using machine learning
* Classify predefined network activity categories
* Demonstrate a practical AI and cybersecurity workflow
* Provide an interactive interface for testing network traffic
* Practice building a structured and maintainable machine learning project

## 🧠 Technologies Used

| Technology       | Purpose                |
| ---------------- | ---------------------- |
| Python           | Core development       |
| Pandas           | Data processing        |
| NumPy            | Numerical operations   |
| Scikit-learn     | Machine learning       |
| Matplotlib       | Visualization          |
| Seaborn          | Exploratory analysis   |
| Streamlit        | Interactive dashboard  |
| Joblib           | Model serialization    |
| GitHub Actions   | Continuous integration |
| Jupyter Notebook | Model development      |

## 🔄 Project Workflow

```text
Network Traffic Dataset
        ↓
Data Preprocessing
        ↓
Feature Engineering
        ↓
Train/Test Split
        ↓
Random Forest Classifier
        ↓
Threat Prediction
        ↓
Threat Analyzer
        ↓
Severity Classification
        ↓
Security Alerts
        ↓
Streamlit Dashboard
```

## 📌 Project Status

| Component                 | Status     |
| ------------------------- | ---------- |
| Data Processing           | ✅ Complete |
| Feature Engineering       | ✅ Complete |
| ML Model                  | ✅ Complete |
| Threat Classification     | ✅ Complete |
| Severity Analysis         | ✅ Complete |
| Security Alerts           | ✅ Complete |
| Streamlit Dashboard       | ✅ Complete |
| Automated Tests           | ✅ Complete |
| GitHub Actions CI         | ✅ Complete |
| Model Documentation       | ✅ Complete |
| Larger Real-World Dataset | 🔄 Planned |
| Real-Time Monitoring      | 🔄 Planned |

## 🖥️ Application Preview

The Streamlit dashboard provides an interactive interface for uploading network traffic data and viewing threat predictions, severity levels, alerts, and detection summaries.

![AI Cyber Threat Detection Dashboard](https://via.placeholder.com/1200x650?text=AI+Cyber+Threat+Detection+Dashboard)

> A real application screenshot can be added here after deploying or running the dashboard.

## 📊 Threat Categories

The current educational dataset contains the following categories:

* `normal`
* `dos`
* `probe`
* `r2l`

The project also maps predictions to basic severity levels for dashboard presentation.

## ⚠️ Severity Levels

| Threat Category | Severity |
| --------------- | -------- |
| `normal`        | LOW      |
| `probe`         | MEDIUM   |
| `r2l`           | HIGH     |
| `dos`           | CRITICAL |

## 📁 Project Structure

```text
AI-Cyber-Threat-Detection/
│
├── .github/
│   └── workflows/
│       └── python-check.yml
│
├── .streamlit/
│   └── config.toml
│
├── app/
│   └── app.py
│
├── data/
│   ├── README.md
│   ├── sample_network_traffic.csv
│   └── test_network_traffic.csv
│
├── docs/
│   └── architecture.md
│
├── models/
│   └── .gitkeep
│
├── notebooks/
│   └── cyber_threat_detection.ipynb
│
├── src/
│   ├── __init__.py
│   ├── alerts.py
│   ├── evaluate_model.py
│   ├── feature_engineering.py
│   ├── model_utils.py
│   ├── predict.py
│   ├── preprocessing.py
│   ├── save_model.py
│   ├── threat_analyzer.py
│   └── train_model.py
│
├── tests/
│   ├── .gitkeep
│   └── test_model.py
│
├── .gitignore
├── LICENSE
├── MODEL_CARD.md
├── README.md
├── SECURITY.md
└── requirements.txt
```

## ▶️ How to Use

### 1. Clone the Repository

```bash
git clone https://github.com/DharineeshE/AI-Cyber-Threat-Detection.git
cd AI-Cyber-Threat-Detection
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Dashboard

```bash
streamlit run app/app.py
```

### 4. Test the System

Open the Streamlit dashboard and upload:

```text
data/test_network_traffic.csv
```

The system will display:

* Predicted threat type
* Threat severity
* Security alert
* Recommended action
* Detection summary

## 🧪 Automated Testing

The project includes automated tests covering:

* Dataset loading
* Required dataset columns
* Model training
* Prediction output

Run the tests with:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

## 🤖 Continuous Integration

GitHub Actions automatically performs basic project checks whenever changes are pushed.

The workflow:

```text
Push / Pull Request
        ↓
Install Dependencies
        ↓
Check Python Files
        ↓
Run Automated Tests
        ↓
Verify Project Files
        ↓
Build Status
```

## 🏗️ System Architecture

```text
                    ┌───────────────────────┐
                    │   Network Traffic     │
                    │        CSV Data       │
                    └───────────┬───────────┘
                                │
                                ▼
                    ┌───────────────────────┐
                    │   Data Preprocessing  │
                    │  Cleaning & Validation│
                    └───────────┬───────────┘
                                │
                                ▼
                    ┌───────────────────────┐
                    │ Feature Engineering   │
                    │ Encoding & Selection  │
                    └───────────┬───────────┘
                                │
                                ▼
                    ┌───────────────────────┐
                    │   Random Forest ML    │
                    │   Threat Classifier   │
                    └───────────┬───────────┘
                                │
                                ▼
                    ┌───────────────────────┐
                    │   Threat Analyzer     │
                    │ Type + Severity       │
                    └───────────┬───────────┘
                                │
                    ┌───────────┴───────────┐
                    ▼                       ▼
          ┌─────────────────┐     ┌──────────────────┐
          │ Security Alerts │     │ Streamlit        │
          │ & Recommendations│    │ Dashboard        │
          └─────────────────┘     └──────────────────┘
```

## 📚 Dataset

The repository currently contains a small educational dataset created to demonstrate the machine learning workflow.

It includes features such as:

* Connection duration
* Network protocol
* Service type
* Source bytes
* Destination bytes
* Failed login attempts
* Connection count
* Threat label

A larger recognized cybersecurity dataset can be integrated in future versions.

## 🧠 Machine Learning Model

The current implementation uses a **Random Forest Classifier** through a Scikit-learn pipeline.

The pipeline performs:

```text
Input Data
    ↓
Categorical Encoding
    ↓
Numerical Feature Processing
    ↓
Random Forest Classifier
    ↓
Threat Prediction
```

Model evaluation includes:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

## 🚨 Security Alerts

The project generates human-readable alerts based on the predicted severity.

Examples include:

```text
LOW      → Continue monitoring network activity.
MEDIUM   → Review the source and connection pattern.
HIGH     → Investigate the connection and review authentication activity.
CRITICAL → Investigate immediately and follow your authorized incident-response process.
```

## ⚙️ Model Saving

The project includes a module for saving the trained model using Joblib:

```bash
python src/save_model.py
```

The serialized model is stored under:

```text
models/threat_detection_model.pkl
```

## 📈 Future Improvements

* Integration with a large real-world cybersecurity dataset
* Advanced anomaly detection
* Hyperparameter optimization
* Deep learning-based threat detection
* Explainable AI
* Real-time network monitoring
* Automated alert notifications
* Cloud deployment
* Model drift monitoring

## ⚠️ Disclaimer

This project is intended for **educational, research, and authorized testing purposes**.

The included dataset is a small demonstration dataset and does not represent the complexity of real-world network traffic.

The system should not be treated as a production-grade intrusion detection or security monitoring platform.

## 🔐 Responsible Use

Use this project only on systems and network data that you are authorized to analyze.

Do not use the software to monitor, scan, access, or interfere with systems without appropriate permission.

## 👨‍💻 Author

**Dharineesh E**

AI & Data Science Student

---

⭐ Star the repository if you find the project interesting!
