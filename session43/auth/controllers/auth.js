const jwt = require('jsonwebtoken');
const bcrypt = require('bcrypt');
const { User } = require('../models');

class AuthController  {
    static auth(req, res) {
        let dataUser = req.body
        User.findOne({where: {"uid": dataUser.uid}})
            .then((user) => {
                bcrypt.compare(dataUser.password, user.password)
                    .then((status) => {
                        let payload = {uid: user.uid}
                        let token =jwt.sign(payload, process.env.TOKEN_SECRET, {expiresIn: '1800s'})
                        res.json(token)
                    })
                    .catch(err => {
                        res.sendStatus(403);
                    })
            })
            .catch(err => {
                console.log(err);
                res.sendStatus(401);
            })
    }

    static async validate(req, res) {
        const pretoken = req.headers['authorization']
        const token = pretoken.split(' ')[1]

        await jwt.verify(token, process.env.TOKEN_SECRET, (err, payload)=>{
            if (err) {
                res.sendStatus(401);
            } else {
                res.status(200).send(payload);
            }
        });
          
    }
}

module.exports= { AuthController }