import json
from pathlib import Path 

CACHE = Path("app/db/local_cache.json") 

def read_cache():
    if CACHE.exists():
        return json.loads(CACHE.read_text())
    return {} 

def write_cache(data):
    CACHE.write_text(json.dumps(data, indent=2))

