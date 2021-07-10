const express = require('express');
const bodyParser = require('body-parser');
const dotenv = require('dotenv');

const app = express()

app.use(bodyParser.json());

dotenv.config();

const { SignUpController } = require("./controllers/signup");
const { AuthController } =require("./controllers/auth");

app.post('/auth', AuthController.auth);
app.post('/signup', SignUpController.create);
app.get('/validate', AuthController.validate)

app.get('/ping', (req, res) => {
    res.send("pong");
});


app.listen(7000)