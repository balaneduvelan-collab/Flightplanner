from fastapi import APIRouter
from app.services.notam_service import get_notams 

router = APIRouter(prefix="/notam", tags=["NOTAM"]) 

@router.get("/{icao}")
async def notams(icao: str):
    return await get_notams(icao)

