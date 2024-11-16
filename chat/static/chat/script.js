const chatSocket = new WebSocket('ws://' + window.location.host + '/ws/chat/');

chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    const messageElement = document.createElement('p');
    messageElement.textContent = `${data.sender} to ${data.receiver}: ${data.message}`;
    document.getElementById('messages').appendChild(messageElement);
};

chatSocket.onclose = function() {
    console.error('Chat socket closed unexpectedly');
};

document.getElementById('send-button').onclick = function() {
    const sender = document.getElementById('sender').value;
    const receiver = document.getElementById('receiver').value;
    const message = document.getElementById('message-input').value;

    chatSocket.send(JSON.stringify({
        sender: sender,
        receiver: receiver,
        message: message
    }));
    document.getElementById('message-input').value = '';
};
