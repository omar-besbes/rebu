# REBU Ride Driver Assignment App

This is a backend app. It should be written in Python (you may use any framework you like).

This app is used to assign a driver to a ride request.

Everything in the app is static / hard-coded (all data), **except for the communications URLs**. All URLs should be in a `.env` file.

May be done by **at most 1 person**.

All communications are RESTful and use JSON.

There are 2 main apps to communicate with: `route optimization app` and `trip management app`. So, your `.env` should contain something similar to this:

```.env
ROUTE_OPTIMIZATION_APP=http://localhost:9003
TRIP_MANAGEMENT_APP=http://localhost:9002
```

## Description of communications

### Endpoints

These are the following endpoints that this app should expose:

- `/ride/request`: should return

```json
{
  "type": "available_ride",
  "duration": ""
}
```

- `/ride/approve`: should return

```json
{
  "type": "ride_begin"
}
```

### Flow

1. Upon recieving a `/ride/request` request, you should send a request to the `route optimization app` with the following content:

```json
{
  "type": "find_closest_available_rider",
  "available_riders": [
    {
      "name": "",
      "location": ""
    },
    {
      "name": "",
      "location": ""
    },
    {
      "name": "",
      "location": ""
    }
  ],
  "customer_location": "",
  "customer_destination": "",
}
```

Please put the `type` field as is. You are free to fill the rest with any static data you want.

The `route optimization app` should respond with something like this:

```json
{
  "type": "closest_available_rider",
  "rider": {
    "name": "",
    "location": ""
  },
  "customer_location": "",
  "customer_destination": "",
}
```

2. Now that the rider has been identified, the best route should be calculated. Send a request to the `route optimization app` with the following content:

```json
{
  "type": "calculate_best_route",
  "rider": {
    "name": "",
    "location": ""
  },
  "customer_location": "",
  "customer_destination": "",
}
```

Please put the `type` field as is. You are free to fill the rest with any static data you want.

The `route optimization app` should respond with something like this:

```json
{
  "type": "best_route",
  "rider": {
    "name": "",
    "location": ""
  },
  "customer_location": "",
  "customer_destination": "",
  "route": ["", "", "", ""],
}
```

3. Now that the route and the rider have been identified, respond to the current request from the customer with:

```json
{
  "type": "available_ride",
  "duration": "",
  "route": ["", "", "", ""],
}
```

Please put the `type` field as is. You are free to fill the rest with any static data you want.

4. Upon recieving a `/ride/approve` request, reply to the customer with the following content:

```json
{
  "type": "ride_begin",
}
```

Please put the `type` field as is. You are free to fill the rest with any static data you want.

5. You should also send a request to the `trip management app` with the following content:

```json
{
  "type": "ride_begin",
  "rider": {
    "name": "",
    "location": ""
  },
  "customer_location": "",
  "customer_destination": "",
  "route": ["", "", "", ""],
}
```

Please put the `type` field as is. You are free to fill the rest with any static data you want.

The `trip management app` should respond with something like this:

```json
{
  "type": "trip_begin_acknowledgment",
  "rider": {
    "name": "",
    "location": ""
  },
  "customer_location": "",
  "customer_destination": "",
  "route": ["", "", "", ""],
}
```
