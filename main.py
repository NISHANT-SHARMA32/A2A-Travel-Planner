from fastapi import FastAPI
from pydantic import BaseModel
import asyncio
import httpx

from agents.flight_agent import get_flights
from agents.hotel_agent import get_hotels
from agents.attraction_agent import get_attractions
from services.gemini_service import generate_itinerary, extract_trip_details

app = FastAPI()


class TravelRequest(BaseModel):
    query: str


@app.get("/")
def home():
    return {"message": "AI Travel Planner running 🚀"}


# ✅ A2A call to Weather Agent
async def fetch_weather(city):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://127.0.0.1:8001/weather",
            json={"city": city}
        )
        return response.json()


@app.post("/plan")
async def plan_trip(request: TravelRequest):
    user_query = request.query

    # ✅ Smart parsing (Gemini)
    details = extract_trip_details(user_query)
    city = details.get("destination", "Delhi")
    source = details.get("source") or "Delhi"

    # ✅ Async execution
    weather_task = fetch_weather(city)
    flights_task = asyncio.to_thread(get_flights, source, city)
    hotels_task = asyncio.to_thread(get_hotels, city)
    attractions_task = asyncio.to_thread(get_attractions, city)

    weather, flights, hotels, attractions = await asyncio.gather(
        weather_task,
        flights_task,
        hotels_task,
        attractions_task
    )

    # ✅ Generate itinerary
    itinerary = generate_itinerary(
        user_query,
        weather,
        flights,
        hotels,
        attractions
    )

    return {
        "parsed_details": details,
        "weather": weather,
        "flights": flights,
        "hotels": hotels,
        "attractions": attractions,
        "itinerary": itinerary
    }