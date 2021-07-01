class Router {

    constructor () {
        this.routes = {}
    }

    route(path, request, response) {
        let callback = this.routes[path]
        callback(request, response);
    }

    register(path, callback) {
        this.routes[path] = callback
    }
};

module.exports = { Router };