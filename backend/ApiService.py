import httpx
import asyncio
import os
from dotenv import load_dotenv

class ApiService:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("OPENWEATHER_API_KEY")
        self.api_endpoint = "https://api.openweathermap.org/data/2.5/weather"
        if not self.api_key:
            raise ValueError("API key not found")

    async def get_data(self, city_name: str) -> dict:
        params = {"q": city_name, "appid": self.api_key}
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(self.api_endpoint, params=params)
            data = response.json()

        if response.status_code != 200:
            return {"status": "error", "message": data.get("message", "Unknown error")}

        return {
            "status": "success",
            "city": data["name"],
            "country": data["sys"]["country"],
            "temp": round(data["main"]["temp"] - 273.15, 1),
            "weather": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind": data["wind"]["speed"],
            "icon": data["weather"][0]["icon"]
        }

    def fetch(self, city_name: str) -> dict:
        return asyncio.run(self.get_data(city_name))