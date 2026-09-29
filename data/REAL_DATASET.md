# Real-World Dataset

## UNSW-NB15

The project will be extended using the **UNSW-NB15 Network Intrusion Dataset**, developed by UNSW Canberra.

The dataset contains network traffic representing normal activities and multiple modern attack behaviors.

## Dataset Information

* **Records:** 2,540,044
* **Features:** 49
* **Attack Categories:** 9
* **Dataset Type:** Network intrusion detection
* **Source:** UNSW Canberra

## Attack Categories

The dataset includes:

* Fuzzers
* Analysis
* Backdoors
* DoS
* Exploits
* Generic
* Reconnaissance
* Shellcode
* Worms

## Training and Testing Data

The official dataset also provides separate training and testing files for machine-learning experiments.

The project can use these files to develop and evaluate the threat-detection model.

## Planned Integration

The current repository uses a small educational dataset so the project can be demonstrated easily.

The next development phase will:

```text
UNSW-NB15
      ↓
Data Cleaning
      ↓
Feature Selection
      ↓
Encoding
      ↓
Model Training
      ↓
Model Evaluation
      ↓
Threat Prediction
      ↓
Streamlit Dashboard
```

## Dataset Source

Official source:

**UNSW Research — The UNSW-NB15 Dataset**

The dataset should be downloaded from its official source and used according to its stated research-use conditions.

## Important Note

The current `sample_network_traffic.csv` remains in the repository for demonstration and testing.

Large external datasets should not be unnecessarily committed to the Git repository. Instead, dataset-download instructions or a preprocessing workflow can be provided.
