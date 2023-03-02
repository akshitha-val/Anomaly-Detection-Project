# Login Behavior Anomaly Detection System

An intelligent machine learning-based anomaly detection system designed to identify suspicious user login activities and potential security threats using behavioral analytics and XGBoost.

---

## Overview

This project focuses on detecting anomalous login behavior by analyzing user activity patterns such as login frequency, IP behavior, device usage, failed attempts, session timing, and geographical inconsistencies.

The system assigns an **anomaly score between 1–10** to each login event.

- **Score < 3** → Normal Activity  
- **Score ≥ 3** → Anomalous Activity 

The project can help organizations proactively identify:

- Unauthorized access attempts
- Credential stuffing attacks
- Compromised user accounts
- Insider threats
- Suspicious login patterns

---

# Features

- Machine Learning-based anomaly detection
- XGBoost classification model
- FastAPI integration for prediction APIs
- Exploratory Data Analysis (EDA)
- Outlier detection techniques
- Supervised & unsupervised anomaly detection
- Model serialization using Pickle
- Jupyter Notebook experimentation
- Scalable architecture for future deployment

---

# Tech Stack

## Languages & Libraries
- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Matplotlib
- Seaborn

## Frameworks & Tools
- FastAPI
- Jupyter Notebook
- Git & GitHub

---

# 📂 Project Structure

```bash
anomaly-detection/
│
├── notebooks/
│   ├── anomaly_detection.ipynb
│   ├── outlier_user.ipynb
│   └── unsupervised.ipynb
│
├── app/
│   └── fast_api.py
│
├── models/
│   └── regressor_model.pkl
│
├── requirements.txt
├── README.md
└── .gitignore