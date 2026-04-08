# 🌍 AI Travel Planner (Multi-Agent A2A System)

An AI-powered travel planning system that generates personalized, day-wise itineraries using Gemini LLM and a distributed multi-agent architecture with agent-to-agent (A2A) communication.

---

## 🚀 Features

- 🧠 AI-generated itineraries from natural language queries  
- 🌦️ Real-time weather data using OpenWeather API  
- 🔗 Agent-to-Agent (A2A) communication via HTTP microservices  
- ⚡ Asynchronous execution using AsyncIO for faster responses  
- 🌐 Interactive frontend built with Streamlit  
- 🧩 Modular multi-agent system (weather, flights, hotels, attractions)  

---

## 🏗️ Architecture


User (Streamlit UI)
↓
FastAPI Backend (Orchestrator)
↓
Weather Agent (Microservice - HTTP API)
↓
Gemini API (LLM)
↓
Response → UI


---

## 🛠️ Tech Stack

- **Backend:** FastAPI, Python  
- **Frontend:** Streamlit  
- **AI:** Gemini API (LLM)  
- **Concurrency:** AsyncIO  
- **APIs:** OpenWeather API  
- **Architecture:** Microservices, A2A (Agent-to-Agent)  

---

## ▶️ How to Run Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/NISHANT-SHARMA32/A2A-Travel-Planner.git
cd A2A-Travel-Planner
