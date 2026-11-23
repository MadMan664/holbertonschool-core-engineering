const socket = new WebSocket('ws://localhost:8000/ws');
const messages = document.getElementById('messages');
const input = document.getElementById('input');

const show = (text) => {
  const item = document.createElement('li');
  item.textContent = text;
  messages.appendChild(item);
};

socket.onmessage = (event) => {
  show(event.data);
};

document.getElementById('form').addEventListener('submit', (event) => {
  event.preventDefault();
  socket.send(input.value);
  input.value = '';
});
