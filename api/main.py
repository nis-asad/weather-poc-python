from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from api.db import weather_collection
import random

app = FastAPI(title="Weather POC API")

@app.get("/")
def root():
    return {"message": "Welcome to Weather POC API!", "info": "Visit /docs to explore endpoints."}

class WeatherIn(BaseModel):
    city: str
    temp_c: float
    humidity: float
    pressure: float
    description: Optional[str] = None

@app.post("/ingest", status_code=201)
def ingest_weather(data: WeatherIn):
    record = data.dict()
    record["timestamp"] = datetime.utcnow()
    result = weather_collection.insert_one(record)
    return {"status": "success", "id": str(result.inserted_id)}

@app.get("/latest/{city}")
def get_latest_weather(city: str):
    record = weather_collection.find_one(
        {"city": city},
        sort=[("timestamp", -1)],
        projection={"_id": 0}
    )
    if not record:
        raise HTTPException(status_code=404, detail=f"No weather data found for city: {city}")
    return record

@app.get("/history/{city}")
def get_weather_history(city: str, limit: int = 50):
    records = list(
        weather_collection.find(
            {"city": city},
            {"_id": 0}
        ).sort("timestamp", -1).limit(limit)
    )
    if not records:
        raise HTTPException(status_code=404, detail=f"No history found for city: {city}")
    return {"city": city, "records": records}  # ✅ returns dict (what Streamlit expects)

