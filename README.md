# Intrusion Detection System using XGBoost (NSL-KDD)

## Overview

This project implements a Machine Learning-based Intrusion Detection System (IDS) using the NSL-KDD dataset. The system classifies network traffic as normal or malicious using the XGBoost algorithm.

## Objective

To detect cyber attacks such as DoS, Probe, R2L, and U2R using supervised machine learning.

## Dataset

* NSL-KDD dataset (improved version of KDD Cup 99)
* Contains labeled network traffic data with attack categories

## Technologies Used

* Python
* XGBoost
* Pandas, NumPy
* Scikit-learn
* Streamlit (for UI)

## Project Structure

* `data/` → Dataset files
* `models/` → Trained ML model
* `notebooks/` → Jupyter notebooks for training
* `streamlit_App/` → Web interface for prediction

## Working

1. Data preprocessing and feature selection
2. Training XGBoost model on NSL-KDD dataset
3. Model predicts whether traffic is normal or attack
4. Streamlit app allows user to test inputs

## Attack Detection

The model detects:

* DoS (Denial of Service)
* Probe (Scanning attacks)
* R2L (Remote to Local)
* U2R (User to Root)

## Results

* High accuracy in classifying normal vs attack traffic
* Effective detection of multiple attack types

## Future Improvements

* Real-time traffic integration
* Deployment with live network monitoring
* Integration with SIEM tools like Wazuh

## Author

Priyanshu Yadav
