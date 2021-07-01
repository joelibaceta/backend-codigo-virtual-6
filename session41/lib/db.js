const mongoose = require('mongoose');


mongoose.connect('mongodb://localhost:27017/booking', {useNewUrlParser: true});

const AuthLogger = mongoose.model('AuthLogger', {
    username: String, 
    date: Date
});

module.exports = { AuthLogger }