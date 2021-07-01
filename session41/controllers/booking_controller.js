
const { Booking, Guest } = require('../models');
const { Op } = require("sequelize");

class BookingController {

    static create(req, res) {
        let json_data = req.body
        json_data.createdAt = new Date()
        json_data.updatedAt = new Date()

        Booking.create(json_data)
            .then(data => { res.send(data) })
            .catch(err => {
                res.status(500).send({
                    message: err.message
                })
            });
    }

    static findAll(req, res) {
        Booking.findAll({
            include: {model: Guest, as: 'guests'},
            where: {
                deleted: {
                    [Op.eq]: null
                }
            }
        })
        .then(data => { res.send(data) })
        .catch(err => {
            res.status(404).send({
                message: err.message
            })
        });
    }

    static findOne(req, res) {
        let pk = req.params.id
        Booking.findByPk(pk)
            .then(data => { res.send(data) })
            .catch(err => {
                res.status(404).send({
                    message: err.message
                })
            });
    }

    static update(req, res) {
        let pk = req.params.id;
        let json_data = req.body;
        Booking.update(json_data, { where: {id: pk} })
            .then(data => { res.send(data) })
            .catch(err => {
                res.status(500).send({
                    message: err.message
                })
            });
    }

    static safeDelete(req, res) {
        let pk = req.params.id;
       
        let data ={
            deleted: 1,
            deletedAt: new Date()
        }
        
        console.log(data)
        
        Booking.update(data, { where: {id: pk} })
        .then(data => { res.send(data) })
        .catch(err => {
            res.status(500).send({
                message: err.message
            })
        });

    }

    static delete(req, res) {
        let pk = req.params.id;
        Booking.destroy({ where: {id: pk} })
            .then(data => { res.status(201).send(data) })
            .catch(err => {
                res.status(500).send({
                    message: err.message
                })
            });
    }

    static deleteAll(req, res) {
        Booking.destroy()
            .then(data => { res.status(201).send(data) })
            .catch(err => {
                res.status(500).send({
                    message: err.message
                })
            });
    }

}

module.exports = { BookingController }