
from fastapi import APIRouter
from app.services.turbulence_service import get_turbulence 

router = APIRouter(prefix="/turbulence", tags=["Turbulence"]) 

@router.get("/")
async def turbulence(lat: float, lon: float):
    return get_turbulence(lat, lon)