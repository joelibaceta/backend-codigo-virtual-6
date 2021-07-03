const express = require('express')
const path = require('path')
const socketio = require('socket.io')
const http = require('http')

const app = express()

app.use(express.static(path.join(__dirname, 'public')))
const server = app.listen(3333, ()=> console.log("Server running..."))

const io = socketio(server)

io.on('connection', socket => {

    console.log("new Connection");

    socket.on('joinRoom', (username) => {
        console.log("joinRoom required");
        let welcome_message = username + " se ha unido a la sala"
        console.log(welcome_message);
        socket.broadcast.emit('message', welcome_message)
        socket.emit('message', "bienvenido");
    })

    socket.on('onTyping', (username) => {
        socket.broadcast.emit('typing', username)
    })

    socket.on('chatMessage', (data) => {
        let prepare_message = data.user + ": " + data.msg;
        socket.broadcast.emit('message', prepare_message)
        socket.emit('message', prepare_message)
    })
})