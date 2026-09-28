# 🧠 Model Card — AI Cyber Threat Detection System

## Model Overview

The AI Cyber Threat Detection System uses a **Random Forest Classifier** to classify network traffic into predefined threat categories.

The model is implemented using a Scikit-learn pipeline that combines:

- Categorical feature encoding
- Numerical feature processing
- Random Forest classification

## Intended Use

The model is intended for:

- Educational projects
- Machine learning demonstrations
- Cybersecurity research prototypes
- Network traffic classification experiments

## Input Features

The current model uses:

| Feature | Description |
|---|---|
| duration | Connection duration |
| protocol | Network protocol |
| service | Network service |
| src_bytes | Source bytes |
| dst_bytes | Destination bytes |
| failed_logins | Failed login attempts |
| connection_count | Number of connections |

## Output

The model predicts a threat category such as:

- `normal`
- `dos`
- `probe`
- `r2l`

The dashboard additionally maps these predictions to severity levels.

## Model Architecture

```text
Network Traffic
       ↓
Feature Separation
       ↓
Categorical Encoding
       ↓
Random Forest Classifier
       ↓
Threat Prediction
       ↓
Severity Classification
