from fastapi import FastAPI
from pydantic import BaseModel
import os
import requests
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Weather Agent")

API_KEY = os.getenv("OPENWEATHER_API_KEY")


# Request schema
class WeatherRequest(BaseModel):
    city: str


# Core logic (same as before)
def get_weather(city: str):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        res = requests.get(url)
        data = res.json()

        if res.status_code != 200 or "main" not in data:
            return {"error": "Weather fetch failed"}

        return {
            "city": city,
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"]
        }

    except Exception as e:
        return {"error": str(e)}


# ✅ API endpoint
@app.post("/weather")
def weather_endpoint(request: WeatherRequest):
    return get_weather(request.city)


# ✅ Health check
@app.get("/")
def home():
    return {"message": "Weather Agent running 🌦️"}