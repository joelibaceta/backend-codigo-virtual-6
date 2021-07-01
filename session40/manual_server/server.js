var http = require('http');
var url = require("url");

const { Router } = require("./router");
const { PingController, HelloController } = require("./controller");

function iniciar(){

    var router = new Router();

    router.register("/ping", PingController.get );
    router.register("/hello", HelloController.get );

    var onRequest = (request, response) => {
        var path = url.parse(request.url).pathname
        router.route(path, request, response)
    };
    http.createServer(onRequest).listen(8888);
    console.log("Servidor Iniciado");
}

exports.iniciar = iniciar;

