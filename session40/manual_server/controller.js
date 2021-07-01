class PingController {
    static get(request, response) {
        response.writeHead(200, {"Content-Type": "text/html"})
        response.write("pong");
        response.end();
    }
}

class HelloController {
    static get(request, response) {
        response.writeHead(200, {"Content-Type": "text/html"})
        response.write("hello world");
        response.end();
    }
}

module.exports = { PingController, HelloController };