# Car Price Classification System

A machine learning system that classifies car prices into categories based on various features using multiple models, with a deployed KNN model accessible via FastAPI and a Streamlit interface.

## Project Overview

This project implements several machine learning models to classify car prices in Saudi Arabia based on features like:
- Year
- Engine Size
- Mileage
- Type
- Make
- Options

The following models were implemented and compared:
- K-Nearest Neighbors (KNN) - *Deployed*
- Decision Trees
- Logistic Regression
- Support Vector Machine (SVM)

## Project Structure


usecase-4/
├── API.py                     # FastAPI implementation
├── ML/
│   └── SL/
│       └── Classification/
│           ├── KNN.ipynb
│           ├── Decision_Trees.ipynb
│           ├── Logistic_regression.ipynb
│           ├── SVM.ipynb
│           ├── knn_model.joblib
│           └── scaler.joblib


## Live Deployments

- API Endpoint: [https://usecase-4-api.onrender.com]
- Streamlit Interface: [https://arwaalkhathlan-usecase-4-car-prices-hle8gb.streamlit.app/]

## How to Use

### API Endpoints

1. Root endpoint:
```http
GET /
```
Returns a welcome message

2. Prediction endpoint:
```http
POST /predict
```
Accepts JSON payload with the following structure:
```json
{
    "Year": int,
    "Engine_Size": float,
    "Mileage": float,
    "Type": string,
    "Make": string,
    "Options": string
}
```

### Streamlit Interface

Visit the Streamlit app to interact with the model through a user-friendly interface. Enter the car details and get instant price classification predictions.

## Local Development

1. Install dependencies:
```bash
pip install fastapi uvicorn scikit-learn pandas numpy streamlit
```

2. Run the FastAPI server:
```bash
uvicorn API:app --reload
```

3. Run the Streamlit app:
```bash
streamlit run main.py
```

## Machine Learning Models

The project includes multiple classification models:

- **KNN Model (Deployed)**: Implemented with scikit-learn's KNeighborsClassifier
- **Decision Trees**: Using scikit-learn's DecisionTreeClassifier
- **Logistic Regression**: Binary and multiclass classification
- **SVM**: Support Vector Machine implementation

## Team Members for the EDA section

- [arwa alkhathlan](https://github.com/arwaalkhathlan)
- [MAMDOUH ALSHARARI](https://github.com/MAMDOUH-ALSHARARI)
- [sarah](https://github.com/sara1h0t)
- [Mohammed Abdullah](https://github.com/Mohammed-Abdullah2)
- [Abdulrahman](https://github.com/Abdulrahman-w)
