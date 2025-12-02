import json 

with open("data/airports.json") as f:
    AIRPORTS = json.load(f) 

def lookup_airport(icao):
    return AIRPORTS.get(icao.upper(), {"error": "Not found"})