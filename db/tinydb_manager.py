
from tinydb import TinyDB 

DB_PATH = "app/db/local_cache.json" 

def get_cache_db():
    return TinyDB(DB_PATH)
