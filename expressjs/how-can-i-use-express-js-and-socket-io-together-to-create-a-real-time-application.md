# How can I use Express.js and Socket.io together to create a real-time application?
// plain

Express.js and Socket.io can be used together to create a real-time application. The following example demonstrates how to create a basic chat application using Express.js and Socket.io.

```
// server.js

const express = require('express');
const app = express();
const server = require('http').createServer(app);
const io = require('socket.io')(server);

io.on('connection', (socket) => {
  socket.on('send message', (data) => {
    io.emit('receive message', data);
  });
});

server.listen(3000);
```

This code creates an Express.js server that listens on port 3000. It also creates a Socket.io server that listens for incoming connections. When a connection is established, the server waits for a `send message` event. When this event is received, it emits a `receive message` event containing the data that was sent.

The following code demonstrates how to create a client that connects to the server and sends a message.

```
// client.js

const io = require('socket.io-client');
const socket = io.connect('http://localhost:3000');

socket.emit('send message', { message: 'Hello World!' });
```

This code creates a Socket.io client that connects to the server on port 3000. It then emits a `send message` event containing a message.

The server and client code can be combined to create a real-time application. When the client sends a message, the server will emit a `receive message` event that can be used to update the UI in real-time.

## Code explanation
**

- `server.js`: Creates an Express.js server and a Socket.io server.
- `io.on('connection', (socket) => {...})`: Listens for incoming connections and waits for a `send message` event.
- `io.emit('receive message', data)`: Emits a `receive message` event containing the data that was sent.
- `client.js`: Creates a Socket.io client and connects to the server.
- `socket.emit('send message', { message: 'Hello World!' })`: Emits a `send message` event containing a message.

**## Helpful links**

- [Socket.io](https://socket.io/)
- [Express.js](https://expressjs.com/)

onelinerhub: [How can I use Express.js and Socket.io together to create a real-time application?](https://onelinerhub.com/expressjs/how-can-i-use-express-js-and-socket-io-together-to-create-a-real-time-application)