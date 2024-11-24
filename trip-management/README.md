# REBU Ride Trip Management App

This is a backend app. It should be written in JS / Python (you may use any framework you like).

This app is used to manage a trip once it has been approved by the customer.

Everything in the app is static / hard-coded (all data), **except for the communications URLs**. All URLs should be in a `.env` file.

May be done by **at most 2 person**.

All communications are RESTful and use JSON.

There is 1 main app to communicate with: `invoice generation app`. So, your `.env` should contain something similar to this:

```.env
INVOICE_GENERATION_APP=http://localhost:9004
```

## Description of communications

### Endpoints

These are the following endpoints that this app should expose:

- `/trip/begin`: should return

```json
{
  "type": "trip_begin_acknowledgment",
  "rider": {
    "name": "",
    "location": ""
  },
  "customer_location": "",
  "customer_destination": "",
  "route": ["", "", "", ""]
}
```

- `/trip/check_finish`: should return

if trip did not finish yet:

```json
{
  "type": "ride_not_yet_finished"
}
```

if trip has finished:

```json
{
  "type": "ride_finished",
  "cost": "",
  "payment_url": ""
}
```

- `/trip/payment_done`: should return

```json
{
  "type": "ride_end"
}
```

### Flow

1. Upon recieving a `/trip/begin` request, you should reply with: 

```json
{
  "type": "trip_begin_acknowledgment",
  "rider": {
    "name": "",
    "location": ""
  },
  "customer_location": "",
  "customer_destination": "",
  "route": ["", "", "", ""]
}
```

Please put the `type` field as is. You are free to fill the rest with any static data you want.

and start a counter of 30 seconds. Once the counter reaches 0, this marks the end of the trip. You should have an attribute in memory set to false initally that represents the state of the trip. Once the counter reaches 0, change the attribute to true, and you should respond to any `/trip/check_finish` accordingly.

Furthermore, you should send a request to the `invoice generation app` once the trip ends (counter reaches 0) with the following content:

```json
{
  "type": "trip_calculate_cost",
  "rider": {
    "name": "",
    "location": ""
  },
  "customer_location": "",
  "customer_destination": "",
  "route": ["", "", "", ""]
}
```

Please put the `type` field as is. You are free to fill the rest with any static data you want.

The `invoice generation app` should respond with something like this:

```json
{
  "type": "trip_calculate_cost",
  "rider": {
    "name": "",
    "location": ""
  },
  "customer_location": "",
  "customer_destination": "",
  "route": ["", "", "", ""],
  "cost": "",
}
```

2. Upon recieving a `/trip/payment_done` request, you should reply with:

```json
{
  "type": "ride_end"
}
```