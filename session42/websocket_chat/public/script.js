var socket = io();

var username = "";

function joinRoom(){
    console.log("emit joinRoom event")
    let inputname = document.getElementById("inputName").value;
    socket.emit('joinRoom', inputname);
    let messageArea = document.getElementById("messageArea");
    messageArea.style.display="block";
    let inputName = document.getElementById("inputName");
    inputName.style.display="none";
    username = inputname;
}

function sendMessage(){
    let chatinput = document.getElementById("inputchat");

    socket.emit('chatMessage', {
        user: username,
        msg: chatinput.value
    });
}

socket.on('message', (msg)=>{
    let spanmessage = document.createElement("span");
    spanmessage.textContent = msg;
    let divmessage = document.getElementById("messages")
    divmessage.appendChild(spanmessage);
})

socket.on('typing', (username)=>{
    console.log(username + " esta escribiendo ...")
})

let chatinput = document.getElementById("inputchat");
chatinput.addEventListener("keydown", (e) => {
    socket.emit('onTyping', username);
})