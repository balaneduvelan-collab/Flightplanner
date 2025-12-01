from fastapi import FastAPI
from app.routers import (
    route, weather, notam, turbulence,
    performance, airports, regulatory
) 

app = FastAPI(
    title="Flight Planner Backend",
    version="1.0.0"
)
# Routers
app.include_router(route.router)
app.include_router(weather.router)
app.include_router(notam.router)
app.include_router(turbulence.router)
app.include_router(performance.router)
app.include_router(airports.router)
app.include_router(regulatory.router) 

@app.get("/")
def root():
    return {"status": "Flight Planner Backend Running"}
