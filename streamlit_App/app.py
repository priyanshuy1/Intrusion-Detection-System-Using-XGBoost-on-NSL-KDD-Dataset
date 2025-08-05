# app.py

import streamlit as st
import pandas as pd
import joblib

# Load model and scaler
model = joblib.load("../models/rf_model.joblib")      # Or xgb_model.joblib if you're using XGBoost
scaler = joblib.load("../models/scaler.joblib")

st.set_page_config(page_title="Intrusion Detection System", layout="centered")
st.title("Intrusion Detection System (IDS) using Machine Learning")

st.markdown("Upload a CSV file (without header) containing network traffic data to detect **Normal** or **Attack**.")

uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file is not None:
    try:
        # Read uploaded CSV (no headers)
        df = pd.read_csv(uploaded_file, header=None)

        # Drop label and difficulty_level if present (columns 41 & 42)
        df = df.drop(columns=[41, 42], errors='ignore')

        # Encode categorical columns by index: protocol_type (1), service (2), flag (3)
        df[1] = pd.factorize(df[1])[0]
        df[2] = pd.factorize(df[2])[0]
        df[3] = pd.factorize(df[3])[0]

        # Scale the features
        df_scaled = scaler.transform(df)

        # Make predictions
        predictions = model.predict(df_scaled)

        # Append predictions to DataFrame
        df['Prediction'] = predictions
        df['Prediction'] = df['Prediction'].map({0: "Normal", 1: "Attack"})

        st.subheader("Prediction Results")
        st.write(df[['Prediction']])

        st.success(f"Normal: {(df['Prediction'] == 'Normal').sum()} Attack: {(df['Prediction'] == 'Attack').sum()}")

        # Download predictions
        result_csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Results as CSV",
            data=result_csv,
            file_name='ids_predictions.csv',
            mime='text/csv'
        )

    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.info("Please upload a CSV file to get started.")
