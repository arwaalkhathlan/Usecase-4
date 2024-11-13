from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import logging

# Initialize FastAPI app
app = FastAPI()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    # Load pre-trained machine learning model and scaler
    model = joblib.load('ML/Sl/Classification/knn_model.joblib')
    scaler = joblib.load('ML/Sl/Classification/scaler.joblib')
except Exception as e:
    logger.error(f"Error loading model or scaler: {e}")
    raise HTTPException(status_code=500, detail="Internal Server Error: Model or Scaler Loading Failed")

class InputFeatures(BaseModel):
    Year: int
    Engine_Size: float
    Mileage: float
    Type: str
    Make: str
    Options: str

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
# Convert dictionary values to a list in the correct order
    features_list = [dict_f[key] for key in sorted(dict_f)]
# Scale the input features
    scaled_features = scaler.transform([list(dict_f.values
    ())])
    return scaled_features

@app.post("/predict")
async def predict(input_features: InputFeatures):
    data = preprocessing(input_features)
    y_pred = model.predict(data)
    return {"pred": y_pred.tolist()[0]}
