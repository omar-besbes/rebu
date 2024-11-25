const express = require('express');
const { calculateCost } = require('../controllers/tripController');

const router = express.Router();

router.post('/calculate_cost', calculateCost);

module.exports = router;