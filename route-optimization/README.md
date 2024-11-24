# REBU Ride Route Optimization App

This is a backend app. It should be written in Golang (you may use any framework you like).

This app is used to calculate the best routes from any starting point to any end point.

Everything in the app is static / hard-coded (all data), **except for the communications URLs**. All URLs should be in a `.env` file.

May be done by **at most 1 person**.

## Description of communications

These are the following endpoints that this app should expose:

- `/route/best`: should return

```json
{
  "type": "best_route",
  "rider": {
    "name": "",
    "location": ""
  },
  "customer_location": "",
  "customer_destination": "",
  "route": ["", "", "", ""]
}
```

- `/route/closest`: should return

```json
{
  "type": "closest_available_rider",
  "rider": {
    "name": "",
    "location": ""
  },
  "customer_location": "",
  "customer_destination": ""
}
```
