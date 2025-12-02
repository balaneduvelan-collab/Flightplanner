import httpx 

async def get_weather(icao):
    # Temporary mock until API keys added
    return {
        "icao": icao,
        "metar": "MOCK METAR DATA",
        "taf": "MOCK TAF DATA"
    }
