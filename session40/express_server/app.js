const express = require('express');
const logger = require('morgan');

var miMiddleware = (req, res, next) => {
    console.log("has llamado al middleware");
    next();
}

const app = express()
app.use(logger('dev'))
app.use(miMiddleware);

app.get('/', (req, res) => {
    res.send("hello wolrd");
});

app.listen(3000);