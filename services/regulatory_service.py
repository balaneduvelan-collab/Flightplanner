def check_regulations(data):
    # simple rule: no flight below FL110 in controlled airspace
    violation = data.altitude < 11000
    return {
        "altitude": data.altitude,
        "violation": violation,
        "message": "Below minimum altitude!" if violation else "OK"
    }
