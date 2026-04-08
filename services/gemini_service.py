import os
import json
import re
from dotenv import load_dotenv
import google.generativeai as genai

# Load env
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use stable model
model = genai.GenerativeModel("models/gemini-flash-latest")


# ✅ Extract structured trip details
def extract_trip_details(query):
    try:
        prompt = f"""
Extract structured travel details from the query.

Return ONLY valid JSON.
Do NOT include markdown or ```.

Format:
{{
  "source": "city or null",
  "destination": "city",
  "days": number
}}

Query: {query}
"""

        response = model.generate_content(prompt)

        text = response.text.strip()

        # Clean markdown if present
        clean_text = re.sub(r"```json|```", "", text).strip()

        try:
            return json.loads(clean_text)
        except:
            return {
                "source": None,
                "destination": "Delhi",
                "days": 3
            }

    except Exception:
        return {
            "source": None,
            "destination": "Delhi",
            "days": 3
        }


# ✅ Generate structured itinerary
def generate_itinerary(user_query, weather, flights, hotels, attractions):
    try:
        prompt = f"""
You are a smart travel planner AI.

Return ONLY valid JSON.
Do NOT include markdown or ```.

Format:
{{
  "day1": ["activity1", "activity2"],
  "day2": ["activity1"],
  "day3": ["activity1"]
}}

User request:
{user_query}

Weather: {weather}
Flights: {flights}
Hotels: {hotels}
Attractions: {attractions}
"""

        response = model.generate_content(prompt)

        text = response.text.strip()

        # Remove markdown if exists
        clean_text = re.sub(r"```json|```", "", text).strip()

        try:
            return json.loads(clean_text)
        except:
            return {"raw": clean_text}

    except Exception as e:
        return {"error": str(e)}