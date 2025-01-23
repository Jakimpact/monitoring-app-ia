from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from prometheus_fastapi_instrumentator import Instrumentator

from models import FeaturesInput, PredictionOutput
from model_utils import load_model, prediction

app = FastAPI()

model = load_model()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Instrumentator().instrument(app).expose(app)


@app.get("/")
async def home():
    return {"hello": "HELLO THERE"}


@app.post("/predict")
async def predict(feature_input: FeaturesInput):
    """
    Realise une prédiction avec le modèle
    """

    feature_input_dict = {
        "MedInc": feature_input.MedInc,
        "HouseAge": feature_input.HouseAge,
        "AveRooms": feature_input.AveRooms,
        "AveBedrms": feature_input.AveBedrms,
        "Population": feature_input.Population,
        "AveOccup": feature_input.AveOccup,
        "Latitude": feature_input.Latitude,
        "Longitude": feature_input.Longitude,
    } 
    feature_input_df = pd.DataFrame([feature_input_dict])
    feature_input_df = feature_input_df.astype({
        "MedInc": float,
        "HouseAge": float,
        "AveRooms": float,
        "AveBedrms": float,
        "Population": float,
        "AveOccup": float,
        "Latitude": float,
        "Longitude": float,
    })

    pred = prediction(model, feature_input_df)
    return PredictionOutput(prediction=pred)
