from fastapi import FastAPI
from app.routers import (
    route, weather, notam, turbulence,
    performance, airports, regulatory
) 

app = FastAPI(
    title="Flight Planner Backend",
    version="1.0.0"
)
