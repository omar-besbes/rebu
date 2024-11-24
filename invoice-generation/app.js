require('dotenv').config();
const express = require('express');
const bodyParser = require('body-parser');
const tripRoutes = require('./routes/trip');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(bodyParser.text({ type: 'text/xml' })); // To handle SOAP requests
app.use('/trip', tripRoutes);

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});