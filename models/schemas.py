
from pydantic import BaseModel 

class RouteRequest(BaseModel):
    origin: str
    destination: str 

class PerformanceRequest(BaseModel):
    aircraft: str
    payload: float
    distance: float 

class RegulatoryRequest(BaseModel):
    altitude: float
    route: list[str] = []
