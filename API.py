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
    try:
        dict_f = {
            'Year': input_features.Year,
            'Engine_Size': input_features.Engine_Size,
            'Mileage': input_features.Mileage,
            'Type_Accent': 1 if input_features.Type == 'Accent' else 0,
            'Type_Land Cruiser': 1 if input_features.Type == 'Land Cruiser' else 0,
            'Make_Hyundai': 1 if input_features.Make == 'Hyundai' else 0,
            'Make_Mercedes': 1 if input_features.Make == 'Mercedes' else 0,
            'Options_Full': 1 if input_features.Options == 'Full' else 0,
            'Options_Standard': 1 if input_features.Options == 'Standard' else 0
        }

        # Convert dict to a sorted list
        features_list = [dict_f[key] for key in sorted(dict_f)]
        scaled_features = scaler.transform([features_list])

        return scaled_features
    except Exception as e:
        logger.error(f"Error in preprocessing: {e}")
        raise HTTPException(status_code=400, detail="Bad Request: Preprocessing Failed")

@app.post("/predict")
async def predict(input_features: InputFeatures):
    try:
        data = preprocessing(input_features)
        y_pred = model.predict(data)
        return {"pred": y_pred.tolist()[0]}
    except Exception as e:
        logger.error(f"Prediction error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error: Prediction Failed")
