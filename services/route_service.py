from app.utils.geo import great_circle 

def compute_route(data):
    points = great_circle(data.origin, data.destination)
    return {
        "origin": data.origin,
        "destination": data.destination,
        "points": points
    }

