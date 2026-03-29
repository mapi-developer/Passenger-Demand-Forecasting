from fastapi import FastAPI, HTTPException
import joblib
import pandas as pd
import os
from .schemas import PassengerForecastRequest, PassengerForecastResponse

app = FastAPI(
    title='Passenger  Demand API'
    ,description='Machine Learning API for forecasting airline passenger traffic'
    ,version='1.0.0'
)

MODEL_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'models', 'xgboost_model.joblib')

try:
    model = joblib.load(MODEL_PATH)
    print(f'Model loaded successfully from {MODEL_PATH}')
except Exception as e:
    print(F'Error loading model: {e}')
    model = None

@app.get('/')
def read_root():
    return {'status': 'healthy', 'message': 'Airline Demand Forecasting API is running'}

@app.post('/predict', response_model=PassengerForecastResponse)
def predict_demand(request: PassengerForecastRequest):
    if model is None:
        raise HTTPException(status_code=500, detail='Model not loaded on server.')
    
    try:
        input_data = pd.DataFrame([request.model_dump()])
        prediction = model.predict(input_data)[0]

        return PassengerForecastResponse(predicted_passengers=int(prediction))
    except Exception as e:
        raise HTTPException(status_code=400, detail=f'Prediction error: {str(e)}')
