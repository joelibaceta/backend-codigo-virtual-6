const { User } = require("../models");

class SignUpController {
     
    static create(req, res) {
        let userData = req.body;
        User.create(userData)
            .then((data) => {
                res.send(data)
            })
            .catch((err) => {
                res.sendStatus(500)
            });
    }

}

module.exports = { SignUpController }