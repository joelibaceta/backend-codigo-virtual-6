const jwt = require('jsonwebtoken');
const { AuthLogger } = require('../lib/db')

function authenticateToken(req, res, next) {
    const headerAuth = req.headers['authorization']


    if (headerAuth == null) return res.sendStatus(401)

    const token = headerAuth.split(' ')[1]

    jwt.verify(token, process.env.TOKEN_SECRET, (err, user) => {
        console.log(err)

        if (err) return res.sendStatus(403)

        req.user = user

        const log_entry = new AuthLogger({
            username: user.username,
            date: new Date()
        })

        console.log(log_entry)

        log_entry.save().then(() => {
            console.log("registro creado");
        })

        next()
    })
}

module.exports = authenticateToken;