# Flightplanner
Build a Flight Planner Demo Project with: • Route planning &amp; navigation • Aircraft performance &amp; fuel estimation • Weather / turbulence overlays • NOTAM / hazard alerts • Simplified regulatory / ATC compliance • 3D visualization in Cesium
✈️ Flight Planner Backend (FastAPI) 

The backend service powering the Flight Planner Demo Application. 

This backend performs all heavy aviation logic including:
- Route planning
- Weather ingestion (METAR/TAF)
- NOTAM parsing
- Turbulence approximation
- Aircraft performance (OpenAP / JetFuelBurn)
- Regulatory & ATC mock checks
- Data preprocessing
- Caching & storage
- API for frontend (CesiumJS) 

--- 

## 🚀 Tech Stack 

### **Backend**
- Python 3.12
- FastAPI
- Uvicorn ASGI
- TinyDB (or SQLite fallback)
- Pydantic Models
- Async HTTPX Client 

### **Aviation Libraries**
- OpenAP (aircraft performance)
- JetFuelBurn
- AVWX Engine (METAR/TAF/NOTAM)
- OpenAir Parser (airspace boundaries) 

### **Data & Preprocessing**
- NCEI / Open-Meteo weather datasets
- Copernicus turbulence grids (preprocessed)
- OpenAIP navigation data
- Local caching layer (JSON)
