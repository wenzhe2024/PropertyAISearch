import os

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your_openai_api_key")
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///your_database.db")
    GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY", "your_google_maps_api_key")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
