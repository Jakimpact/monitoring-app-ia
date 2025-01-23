from pydantic import BaseModel


class FeaturesInput(BaseModel):
    MedInc : float
    HouseAge : float 
    AveRooms : float    
    AveBedrms : float  
    Population : float 
    AveOccup : float 
    Latitude : float   
    Longitude : float   


class PredictionOutput(BaseModel):
    prediction: float