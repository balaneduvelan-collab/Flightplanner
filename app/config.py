from pydantic import BaseSettings 

class Settings(BaseSettings):
    AVWX_API_KEY: str = ""
    CHECKWX_API_KEY: str = ""
    OPENMETEO_ENABLED: bool = True 

settings = Settings()

