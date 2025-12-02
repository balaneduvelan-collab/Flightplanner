async def get_notams(icao):
    return {
        "icao": icao,
        "notams": ["Mock NOTAM - runway maintenance", "Mock NOTAM - bird activity"]
    }

