from fastapi import FastAPI
import time
import threading
import requests
from pydantic import BaseModel
import os
from dotenv import load_dotenv

load_dotenv()

INVOICE_GENERATION_APP = os.getenv("INVOICE_GENERATION_APP", "http://localhost:9004")

app = FastAPI(
  title="Trip Management",
  description="Trip Management Service",
  version="0.1"
)

trip_finished = False
trip_cost = None

class TripBeginResponse(BaseModel):
    type: str
    rider: dict
    customer_location: str
    customer_destination: str
    route: list

class InvoiceRequest(BaseModel):
    type: str
    rider: dict
    customer_location: str
    customer_destination: str
    route: list

def simulate_trip_end():
    global trip_finished, trip_cost

    print("Trip started... Simulating trip duration (30 seconds)")
    time.sleep(30)  
    trip_finished = True  
    
    invoice_request = {
        "type": "trip_calculate_cost",
        "rider": {"name": "John Doe", "location": "Rider Location"},
        "customer_location": "Customer Location",
        "customer_destination": "Customer Destination",
        "route": ["Stop 1", "Stop 2", "Stop 3", "Final Stop"],
    }
    print(f"Sending invoice request to: {INVOICE_GENERATION_APP}")
    try:
        response = requests.post(f"{INVOICE_GENERATION_APP}/trip/calculate_cost", json=invoice_request)
        if response.status_code == 200:
            invoice_data = response.json()
            trip_cost = invoice_data.get("cost", "100.00")
            print("Invoice response received:", invoice_data)
        else:
            print("Failed to generate invoice. Status code:", response.status_code)
    except Exception as e:
        print("Error communicating with invoice generation app:", e)

@app.post("/trip/begin", response_model=TripBeginResponse)
async def trip_begin():
    global trip_finished
    trip_finished = False  

    response_data = {
        "type": "trip_begin_acknowledgment",
        "rider": {"name": "Ennoury Lemaalem", "location": "Cuba La Famille"},
        "customer_location": "CUBAAAA",
        "customer_destination": "ELBORJJ",
        "route": ["Stop 1", "Stop 2", "Stop 3", "Final Stop"],
    }

    thread = threading.Thread(target=simulate_trip_end)
    thread.start()

    print("Acknowledgment sent.")
    return response_data

@app.post("/trip/check_finish")
async def check_finish():
    if not trip_finished:
        print("Trip is still ongoing...")
        return {"type": "ride_not_yet_finished"}
    else:
        print("Trip has finished. Sending payment URL...")
        return {"type": "ride_finished", "cost": trip_cost}

@app.post("/trip/payment_done")
async def payment_done():
    print("Payment confirmed. Ride has ended.")
    return {"type": "ride_end"}
