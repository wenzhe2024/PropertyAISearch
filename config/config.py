import os

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "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")
    DATABASE_URL = os.getenv("DATABASE_URL", "data/real_estate.db")
    #GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY", "your_google_maps_api_key")
    #LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
