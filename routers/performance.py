from fastapi import APIRouter
from app.services.performance_service import compute_performance
from app.models.schemas import PerformanceRequest 

router = APIRouter(prefix="/performance", tags=["Performance"]) 

@router.post("/compute")
async def compute(data: PerformanceRequest):
    return compute_performance(data)
