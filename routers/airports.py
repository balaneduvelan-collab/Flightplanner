from fastapi import APIRouter
from app.services.airports_service import lookup_airport 

router = APIRouter(prefix="/airports", tags=["Airports"]) 

@router.get("/{icao}")
def lookup(icao: str):
    return lookup_airport(icao)

