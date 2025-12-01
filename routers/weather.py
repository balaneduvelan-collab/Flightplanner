
from fastapi import APIRouter
from app.services.weather_service import get_weather 

router = APIRouter(prefix="/weather", tags=["Weather"]) 

@router.get("/{icao}")
async def weather(icao: str):
    return await get_weather(icao)
