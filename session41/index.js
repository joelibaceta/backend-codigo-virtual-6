const express = require('express')
const bodyParser = require('body-parser')
const dotenv = require('dotenv');
const cors = require('cors');

const { greetingController } = require('./controllers/greeting_controller');
const { BookingController } = require('./controllers/booking_controller');
const { GuestController } = require('./controllers/guest_controller');
const { AuthController } = require('./controllers/auth_controller');

const authmiddelware = require('./middlewares/jwt_authentication')

dotenv.config();

console.log(process.env.TOKEN_SECRET)

const app = express()
app.use(bodyParser.json());
app.use(cors());

const corsOptions = {
    origin: 'https://midominio.com'
}
//app.use(authmiddelware)

app.get('/', greetingController.get);
app.post('/greeting', greetingController.post);
app.get('/hello/:name', greetingController.get);

app.get('/bookings', BookingController.findAll);
app.post('/bookings', authmiddelware, BookingController.create);
app.get('/booking/:id', BookingController.findOne);
app.put('/booking/:id', authmiddelware, BookingController.update);
app.delete('/booking/:id', authmiddelware, BookingController.safeDelete);
app.delete('/bookings', authmiddelware, BookingController.delete);

app.get('/guests', GuestController.findAll);
app.post('/guests', authmiddelware, GuestController.create);

app.post('/auth', AuthController.auth);
app.post('/signup', AuthController.signup);

app.listen(3000, () => {
    console.log('Server running ...');
})
