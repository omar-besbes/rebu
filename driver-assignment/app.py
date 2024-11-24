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
  rider_request = {
    "type": "find_closest_available_rider",
    "available_riders": [
      {
        "name": "Rider1", 
        "location": "Loc1"
      }, 
      {
        "name": "Rider2",
        "location": "Loc2"
      }
    ],
    "customer_location": "LocCustomer",
    "customer_destination": "LocDestination"
  }
  rider_response = requests.post(f"{ROUTE_OPTIMIZATION_URL}", json=rider_request).json()
  route_request = rider_response.copy()
  route_request["type"] = "calculate_best_route"

  best_route_response = requests.post(f"{ROUTE_OPTIMIZATION_URL}", json=route_request).json()

  return {
    "type": "available_ride",
    "duration": "10 mins",
    "route": best_route_response["route"]
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

  trip_response = requests.post(f"{TRIP_MANAGEMENT_URL}", json=trip_data)

  return customer_response