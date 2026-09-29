# 🏗️ System Architecture

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
                    │ Feature Engineering  │
                    │ Encoding & Selection  │
                    └───────────┬───────────┘
                                │
                                ▼
                    ┌───────────────────────┐
                    │   Random Forest ML   │
                    │    Threat Classifier  │
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
