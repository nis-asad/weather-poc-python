from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# MongoDB connection
MONGO_URI = os.getenv(
    "MONGO_URI",
    "mongodb+srv://kasad_db_user:tD5GqXzUqX697Z2C@basic.su6r0wq.mongodb.net/weather_poc?retryWrites=true&w=majority&ssl=true"
)
DB_NAME = os.getenv("DB_NAME", "weather_poc")

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client[DB_NAME]

# Collection for weather records
weather_collection = db["weather_records"]
