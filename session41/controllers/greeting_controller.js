class greetingController {

    static get(req, res) {
        console.log(req.user);
        if (req.params.name === undefined) {
            res.send({
                "message": "hello world"
            });
        } else {
            res.send({
                "message": "hello " + req.params.name
            });
        }
    }

    static post(req, res) {
        console.log(req.body)
        res.send({
            "message": "Hello " + req.body.name
        });
    }
}

module.exports = { greetingController }