import requests
from config.config import Config

class APIClient:
    def __init__(self):
        self.api_key = Config.GOOGLE_MAPS_API_KEY

    def call(self, api_query):
        # 示例调用Google Maps API
        response = requests.get("https://maps.googleapis.com/maps/api/your_endpoint", params={
            "query": api_query,
            "key": self.api_key
        })
        return response.json()
