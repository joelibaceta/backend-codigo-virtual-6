const jwt = require('jsonwebtoken')

const TOKEN_SECRET = require('crypto').randomBytes(64).toString('hex');

class AuthController {

    static auth(req, res) {
        let username = req.body.username
        let password = req.body.password

        if (password =="root") {
            let payload = {username: username}
            const token = jwt.sign(payload, TOKEN_SECRET, {expiresIn: '1800s'})
            res.json(token)
        }
    }

}

module.exports = { AuthController }