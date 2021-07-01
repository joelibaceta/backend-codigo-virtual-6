const express = require('express')
const bodyParser = require('body-parser')


const { greetingController } = require('./controllers/greeting_controller');
const { BookingController } = require('./controllers/booking_controller');
const { GuestController } = require('./controllers/guest_controller');
const { AuthController } = require('./controllers/auth_controller');

const app = express()
app.use(bodyParser.json())

app.get('/', greetingController.get);
app.post('/greeting', greetingController.post);
app.get('/hello/:name', greetingController.get);

app.get('/bookings', BookingController.findAll);
app.post('/bookings', BookingController.create);
app.get('/booking/:id', BookingController.findOne);
app.put('/booking/:id', BookingController.update);
app.delete('/booking/:id', BookingController.safeDelete);
app.delete('/bookings', BookingController.delete);

app.get('/guests', GuestController.findAll);
app.post('/guests', GuestController.create);

app.post('/auth', AuthController.auth);

app.listen(3000, () => {
    console.log('Server running ...');
})
