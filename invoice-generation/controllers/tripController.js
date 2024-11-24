exports.calculateCost = (req, res) => {
    const soapResponse = `
    <Envelope xmlns="http://schemas.xmlsoap.org/soap/envelope/">
      <Body>
        <TripCalculateCost>
          <Rider>
            <Name>John Doe</Name>
            <Location>Central Park</Location>
          </Rider>
          <CustomerLocation>Empire State Building</CustomerLocation>
          <CustomerDestination>Statue of Liberty</CustomerDestination>
          <Route>
            <Point>Central Park</Point>
            <Point>Times Square</Point>
            <Point>Wall Street</Point>
            <Point>Statue of Liberty</Point>
          </Route>
          <Cost>50.00</Cost>
        </TripCalculateCost>
      </Body>
    </Envelope>`;

    res.type('text/xml').send(soapResponse);
};