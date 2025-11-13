from datetime import datetime
import random
import time
from api.db import weather_collection

def generate_dummy(city="London"):
    now = datetime.utcnow()
    temp = round(random.uniform(5, 30), 1)
    humidity = round(random.uniform(30, 90), 1)
    pressure = round(random.uniform(990, 1035), 1)
    desc = random.choice(["clear sky", "cloudy", "light rain", "sunny"])
    return {
        "city": city,
        "timestamp": now,
        "temp_c": temp,
        "humidity": humidity,
        "pressure": pressure,
        "description": desc
    }

def insert_record(record):
    weather_collection.insert_one(record)

if __name__ == "__main__":
    cities = ["London", "Paris", "New York", "Tokyo"]
    for city in cities:
        for _ in range(24):
            rec = generate_dummy(city)
            insert_record(rec)
            time.sleep(0.01)
    print("Inserted dummy records into MongoDB!")
