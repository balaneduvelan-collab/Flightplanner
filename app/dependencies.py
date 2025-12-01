from fastapi import Depends
from app.db.tinydb_manager import get_cache_db 

def get_db():
    return get_cache_db()

