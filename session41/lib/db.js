const mongoose = require('mongoose');
const bcrypt = require('bcrypt');

mongoose.connect('mongodb://localhost:27017/booking', {useNewUrlParser: true});

const AuthLogger = mongoose.model('AuthLogger', {
    username: String, 
    date: Date
});

var UserSchema = mongoose.Schema({
    username: {
        type: String,
        required: true
    },
    password: {
        type: String,
        required: true
    }, 
    profile: {
        type: mongoose.Schema.Types.ObjectId,
        ref: 'profile'
    }
});

UserSchema.pre('save', function(next) {

    console.log(this)
    let user = this
    

    bcrypt.genSalt(15, (err, salt) => {
        bcrypt.hash(user.password, salt, (err, hash) => {
            if (err) {
                return next(err);
            } else {
                user.password = hash;
                next();
            }
        });
    })
});

UserSchema.statics.authenticate = function(username, password, callback) {
    User.findOne({username: username})
        .exec((err, user) => {
            if (err) {
                return callback(err);
            } else if (!user) {
                let err = new Error("User not found!");
                err.status = 401;
                return callback(err)
            } else {
                bcrypt.compare(password, user.password, (err, result) => {
                    if (result == true) {
                        return callback(null, user)
                    } else {
                        let err = new Error("Wrong password!");
                        err.status = 401;
                        return callback(err)
                    }
                })
            }
        })
}

const User = mongoose.model('user', UserSchema);

var ProfileSchema = mongoose.Schema({
    "fullname": {
        type: String,
        required: true
    },
    "email": {
        type: String,
        required: true
    },
    "user": {
        type: mongoose.Schema.Types.ObjectId, 
        ref: 'User'
    }
})

const Profile = mongoose.model('profile', ProfileSchema)

module.exports = { AuthLogger, User, Profile };