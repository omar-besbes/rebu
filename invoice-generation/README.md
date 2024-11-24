# REBU Ride Trip Management App

This is a backend app. It should be written in JS / Python (you may use any framework you like).

This app is used to manage a trip once it has been approved by the customer.

Everything in the app is static / hard-coded (all data), **except for the communications URLs**. All URLs should be in a `.env` file.

May be done by **at most 1 person**.

All communications are **SOAP**.

## Description of communications

These are the following endpoints that this app should expose:

- `/trip/calculate_cost`: should return

```xml
<Envelope xmlns="http://schemas.xmlsoap.org/soap/envelope/">
  <Body>
    <TripCalculateCost>
      <Rider>
        <Name></Name>
        <Location></Location>
      </Rider>
      <CustomerLocation></CustomerLocation>
      <CustomerDestination></CustomerDestination>
      <Route>
        <Point></Point>
        <Point></Point>
        <Point></Point>
        <Point></Point>
      </Route>
      <Cost></Cost>
    </TripCalculateCost>
  </Body>
</Envelope>
```
