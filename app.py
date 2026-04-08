import streamlit as st
import requests

st.set_page_config(page_title="AI Travel Planner", layout="centered")

st.title("🌍 AI Travel Planner ✈️")

query = st.text_input("Enter your trip plan:")

if st.button("Plan Trip"):
    res = requests.post(
        "http://127.0.0.1:8000/plan",
        json={"query": query}
    )

    data = res.json()

    # 📌 Parsed Details
    st.subheader("📌 Trip Details")
    details = data["parsed_details"]
    st.write(f"**Destination:** {details.get('destination')}")
    st.write(f"**Days:** {details.get('days')}")

    # 🌦️ Weather
    st.subheader("🌦️ Weather")
    weather = data["weather"]
    st.write(f"🌡️ Temperature: {weather['temperature']}°C")
    st.write(f"🤗 Feels Like: {weather['feels_like']}°C")
    st.write(f"💧 Humidity: {weather['humidity']}%")
    st.write(f"🌤️ Condition: {weather['description']}")

    # ✈️ Flights
    st.subheader("✈️ Flights")
    for flight in data["flights"]:
        st.write(f"• {flight['airline']} — ₹{flight['price']}")

    # 🏨 Hotels
    st.subheader("🏨 Hotels")
    for hotel in data["hotels"]:
        st.write(f"• {hotel['name']} — ₹{hotel['price']}/night")

    # 📍 Attractions
    st.subheader("📍 Attractions")
    for place in data["attractions"]:
        st.write(f"• {place}")

    # 🧠 Itinerary (🔥 CLEAN FORMAT)
    st.subheader("🧠 Itinerary")

    itinerary = data["itinerary"]

    if isinstance(itinerary, dict):
        for day, activities in itinerary.items():
            st.markdown(f"### 📅 {day.capitalize()}")
            for act in activities:
                st.write(f"• {act}")
    else:
        st.write(itinerary)