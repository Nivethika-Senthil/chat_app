const chatSocket = new WebSocket(
    'ws://' + window.location.host + '/ws/chat/'
);

chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    const messageElement = document.createElement('p');
    messageElement.textContent = `${data.user}: ${data.message}`;
    document.getElementById('messages').appendChild(messageElement);
};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

document.getElementById('message-form').onsubmit = function(e) {
    e.preventDefault();
    const messageInput = document.getElementById('message-input');
    const message = messageInput.value;
    chatSocket.send(JSON.stringify({'message': message}));
    messageInput.value = '';
};
