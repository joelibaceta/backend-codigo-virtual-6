const jwt = require('jsonwebtoken');
const { User, Profile } = require('../lib/db');

class AuthController {

    static auth(req, res) {
        let username = req.body.username
        let password = req.body.password

        User.authenticate(username, password, (err, user) => {
            if (err) {
                err.status = 401
                res.sendStatus(401)
            } else {
                let payload = {username: username}
                const token = jwt.sign(payload, process.env.TOKEN_SECRET, {expiresIn: '1800s'})
                res.json(token)
            }
        })

    }

    static signup(req, res) {
        let userData = req.body;
        let profileData = req.body.profile

        let newProfile = new Profile(profileData);
        newProfile.save((err) => {

            if (err) {
                res.send(err.message);
            } else {
                userData.profile = newProfile._id;
                console.log(userData);
                let newUser = new User(userData);
                newUser.save((err) => {
                    if (err) {
                        res.send(err.message);
                    } else {
                        res.send('El usuario se ha registrado con exito.')
                    }
                })
            }
        })

        
    }

}

module.exports = { AuthController }