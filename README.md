# Weather POC - Complete Full-Stack Application

A comprehensive Proof of Concept (POC) demonstrating a complete full-stack weather data management system built with Python, showcasing integration of REST API, Database, Data Analysis, Visualization, and Web UI.

## 🚀 Features

### REST API Endpoints
- **GET /**: Welcome message and API documentation
- **POST /ingest**: Insert new weather data
- **GET /latest/{city}**: Get latest weather reading for a city
- **GET /history/{city}**: Get historical weather data with pagination

### Web Dashboard
- Interactive city selection
- Real-time data loading from API
- Temperature and humidity trend visualization
- Statistical aggregations (mean, max, min)
- Clean, responsive UI with Streamlit
```
```

## 🔧 Installation & Setup

### Prerequisites
- Python 3.8+
- MongoDB Atlas account (or local MongoDB instance)

### 1. Clone and Setup Environment
```bash
git clone <your-repo-url>
cd weather-poc

# Create virtual environment
python -m venv weather
source weather/bin/activate  # On Windows: weather\Scripts\activate

# Install dependencies
pip install fastapi uvicorn pymongo python-dotenv streamlit pandas matplotlib requests
```

## 🚀 Running the Application

### Start the API Server
```bash
# Terminal 1: Start FastAPI server
uvicorn api.main:app --reload --port 8000
```

### Start the Web Dashboard
```bash
# Terminal 2: Start Streamlit app
streamlit run streamlit_app.py
```

### Access the Applications
- **API Documentation**: http://localhost:8000/docs
- **Web Dashboard**: http://localhost:8501
- **API Base URL**: http://localhost:8000

## 📈 Usage Examples

### API Usage

### Dashboard Usage
1. Open http://localhost:8501
2. Enter a city name (e.g., "London", "Paris", "New York", "Tokyo")
3. Click "Load Data" to fetch and visualize weather data
4. View temperature/humidity trends and statistical summaries

## 🧪 Testing

### Test API Endpoints
```bash
# Test root endpoint
curl http://localhost:8000/

# Test with sample data
python -m api.ingest
curl http://localhost:8000/latest/London
```

### Test Dashboard
1. Ensure API server is running
2. Run Streamlit app
3. Test with different cities
4. Verify charts and data display correctly

## 📝 API Documentation

The FastAPI application automatically generates comprehensive API documentation:
- **Swagger UI**: Available at http://localhost:8000/docs
- **ReDoc**: Available at http://localhost:8000/redoc
- **OpenAPI Schema**: Available at http://localhost:8000/openapi.json
