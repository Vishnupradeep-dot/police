import streamlit as st
import pandas as pd

st.subheader("🚨 Add New Police Log & Predict Outcome and Violation")

# Form inputs
with st.form("new_log_form"):
    stop_date = st.date_input("Stop Date")
    stop_time = st.time_input("Stop Time")
    country = st.text_input("Country Name")

    driver_gender = st.selectbox("Driver Gender", ["male", "female", "other"])
    driver_age = st.number_input("Driver Age", min_value=16, max_value=100)
    driver_race = st.text_input("Driver Race")

    is_search = st.selectbox("Was a Search Conducted?", [0, 1])
    search_type = st.text_input("Search Type")

    is_drug_related = st.selectbox("Was it Drug Related?", [0, 1])

    stop_duration = st.selectbox("Stop Duration", ["0-15 Min", "16-30 Min", "30+ Min"])
    vehicle_number = st.text_input("Vehicle Number")

    submitted = st.form_submit_button("Predict Stop Outcome & Violation")

# Dummy logic to display a prediction (replace this with ML logic or SQL-based rules)
if submitted:
    st.success("✅ Log received and processed!")

    # Example response output
    predicted_outcome = "Citation"
    predicted_violation = "Speeding"

    st.markdown(f"""
        ### 🔍 Prediction Result:
        - **Outcome**: `{predicted_outcome}`
        - **Likely Violation**: `{predicted_violation}`
    """)
