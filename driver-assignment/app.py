from fastapi import FastAPI
import requests
import os
from dotenv import load_dotenv

load_dotenv()

ROUTE_OPTIMIZATION_URL = os.getenv("ROUTE_OPTIMIZATION_APP")
TRIP_MANAGEMENT_URL = os.getenv("TRIP_MANAGEMENT_APP")

app = FastAPI(
  title="Driver Assignment",
  description="Driver Assignment Service",
  version="0.1"
)
  
@app.post("/ride/request")
async def request_ride():
  print("Request for a ride ... Searching for available riders")

  return {
    "type": "available_rider",
    "time_until_arrival_to_location": "10 mins",
    "rider": {
      "name":     "John Doe",
			"location": "Point A",
    }
  }



@app.post("/ride/approve")
async def approve_ride():
  customer_response = {
    "type": "ride_begin"
  }

  trip_data = {
    "type": "ride_begin",
    "rider": {
      "name": "Rider A", 
      "location": "Loc1"
    },
    "customer_location": "LocCustomer",
    "customer_destination": "LocDestination",
    "route": ["Step1", "Step2"]
  }

  trip_response = requests.post(f"{TRIP_MANAGEMENT_URL}/trip/begin", json=trip_data)

  return customer_response