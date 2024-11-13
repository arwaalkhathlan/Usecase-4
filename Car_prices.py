import streamlit as st
import requests
import pandas as pd


df = pd.read_csv('data/data_saudi_used_cars.csv')


st.title("Car Price Prediction")

# Input fields for user to enter data
year = st.number_input("Year", min_value=2000, max_value=2025, value=2020)
engine_size = st.number_input("Engine Size", min_value=0.5, max_value=10.0, value=2.5)
mileage = st.number_input("Mileage", min_value=0, max_value=200000, value=15000)
type_options = ["Accent", "LandCruiser"]
type_ = st.selectbox("Car Type", type_options)
make_options = ["Hyundai", "Mercedes",""]
make = st.selectbox("Car Make", make_options)
options_options = ["Full", "Standard"]
options = st.selectbox("Car Options", options_options)

# Button to submit the input data
if st.button("Predict Cluster"):
    # Prepare the data to send to the FastAPI endpoint
    input_data = {
        "Year": year,
        "Engine_Size": engine_size,
        "Mileage": mileage,
        "Type": type_,
        "Make": make,
        "Options": options
    }

    # Send POST request to the deployed FastAPI server
    try:
        response = requests.post("https://usecase-4-api.onrender.com/predict", json=input_data)

        # Get the prediction result from the response
        if response.status_code == 200:
            prediction = response.json().get("pred")
            st.success(f"Predicted Cluster: {prediction}")
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to the API: {e}")