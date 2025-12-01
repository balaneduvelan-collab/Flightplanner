from fastapi import APIRouter
from app.services.route_service import compute_route
from app.models.schemas import RouteRequest 

router = APIRouter(prefix="/route", tags=["Route"]) 

@router.post("/compute")
async def compute(data: RouteRequest):
    return compute_route(data)
