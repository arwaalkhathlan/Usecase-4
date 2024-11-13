from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib

# Initialize FastAPI app
app = FastAPI()

# Load pre-trained machine learning model and scaler
model = joblib.load('ML/UL/knn_model.joblib')
scaler = joblib.load('ML/UL/scaler.joblib')

# Define Pydantic model for input data validation
class InputFeatures(BaseModel):
    Year: int
    Engine_Size: float
    Mileage: float
    Type: str
    Make: str
    Options: str

# Function for preprocessing input features
def preprocessing(input_features: InputFeatures):
    dict_f = {
        'Year': input_features.Year,
        'Engine_Size': input_features.Engine_Size,
        'Mileage': input_features.Mileage,
        'Type_Accent': input_features.Type == 'Accent',
        'Type_Land Cruiser': input_features.Type == 'LandCruiser',
        'Make_Hyundai': input_features.Make == 'Hyundai',
        'Make_Mercedes': input_features.Make == 'Mercedes',
        'Options_Full': input_features.Options == 'Full',
        'Options_Standard': input_features.Options == 'Standard'
    }

    # Convert dict to a sorted list
    features_list = [dict_f[key] for key in sorted(dict_f)]

    # Scale features using the scaler
    scaled_features = scaler.transform([features_list])

    return scaled_features

@app.get("/")
def read_root():
    return {"message": "Welcome to Tuwaiq Academy"}

@app.get("/items/")
def create_item(item: dict):
    return {"item": item}


@app.post("/predict")
async def predict(input_features: InputFeatures):

    data = preprocessing(input_features)


    y_pred = model.predict(data)

    return {"pred": y_pred.tolist()[0]}
