
from fastapi import APIRouter
from app.services.regulatory_service import check_regulations
from app.models.schemas import RegulatoryRequest 

router = APIRouter(prefix="/regulatory", tags=["Regulatory"]) 

@router.post("/check")
def regulatory(data: RegulatoryRequest):
    return check_regulations(data)