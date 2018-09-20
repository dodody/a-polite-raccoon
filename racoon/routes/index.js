var express = require('express');
var router = express.Router();

router.use('/', require('./turn/turn.js'));


module.exports = router;
