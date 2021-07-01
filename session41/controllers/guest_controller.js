
const { Guest, Booking } = require('../models');
const { Op } = require("sequelize");

class GuestController {

    static findAll(req, res) {
        console.log(req.user);
        Guest.findAll({
            include: {model: Booking, as: 'booking'},
        })
        .then(data => { res.send(data) })
        .catch(err => {
            res.status(404).send({
                message: err.message
            })
        });
    }

    static create(req, res) {
        let json_data = req.body
        json_data.createdAt = new Date()
        json_data.updatedAt = new Date()

        Guest.create(json_data)
            .then(data => { res.send(data) })
            .catch(err => {
                res.status(500).send({
                    message: err.message
                })
            });
    }
};

module.exports = { GuestController }