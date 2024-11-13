import streamlit as st
import requests
import pandas as pd


df = pd.read_csv('data/data_saudi_used_cars.csv')


st.title("Car Price Prediction")

# take the user input and saves it
year = st.number_input("Year", min_value=1990, max_value=2025, value=2020)
engine_size = st.number_input("Engine Size", min_value=0.5, max_value=10.0, value=2.5)
mileage = st.number_input("Mileage", min_value=0, max_value=2000000, value=15000)
type = st.selectbox("Car Type", type_options)
make_ = st.selectbox("Car make", make_options)



# menu for car tpe


#car option
options_options = df['Options'].unique().tolist()
options = st.selectbox("Car Options", options_options)

# submit
if st.button("Predict Cluster"):
    # Prepare the data to send to the FastAPI endpoint
    input_data = {
        "Year": year,
        "Engine_Size": engine_size,
        "Mileage": mileage,
        "Type": type,
        "Make": make_,
        "Options": options
    }

    # Send POST
    try:
        response = requests.post("https://usecase-4-api.onrender.com/predict", json=input_data)

        # predict
        if response.status_code == 200:
            prediction = response.json().get("pred")
            st.success(f"Predicted Cluster: {prediction}")
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to the API: {e}")
