const jwt = require('jsonwebtoken')

class AuthController {

    static auth(req, res) {
        let username = req.body.username
        let password = req.body.password

        if (password =="root") {
            let payload = {username: username}
            const token = jwt.sign(payload, process.env.TOKEN_SECRET, {expiresIn: '1800s'})
            res.json(token)
        }
    }

}

module.exports = { AuthController }