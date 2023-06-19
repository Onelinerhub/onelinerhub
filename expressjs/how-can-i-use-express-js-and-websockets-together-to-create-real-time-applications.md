# How can I use Express.js and websockets together to create real-time applications?
// plain

Express.js and websockets can be used together to create real-time applications. Websockets enable bi-directional communication between the client and the server, allowing for real-time updates in the application. Here is an example of how to use Express.js and websockets together to create a real-time application:

```
// Create a websocket server
const WebSocket = require('ws');
const wss = new WebSocket.Server({ port: 8080 });

// Create Express server
const express = require('express');
const app = express();

// Create websocket handler
wss.on('connection', (ws) => {
    ws.on('message', (message) => {
        console.log(`Received message => ${message}`);
    });
    ws.send('Hello from the server!');
});

// Start Express server
app.listen(3000, () => {
    console.log('Express server listening on port 3000');
});
```

## Output example

```
Received message => Hello from the client!
Express server listening on port 3000
```

The code above creates a websocket server on port 8080 and an Express server on port 3000. It then creates a websocket handler which logs incoming messages from the client and sends a message to the client. Finally, it starts the Express server.

## Code explanation


1. `const WebSocket = require('ws');` - This line imports the `ws` module which allows us to create a websocket server.
2. `const wss = new WebSocket.Server({ port: 8080 });` - This line creates a websocket server on port 8080.
3. `const express = require('express');` - This line imports the `express` module which allows us to create an Express server.
4. `const app = express();` - This line creates an Express server.
5. `wss.on('connection', (ws) => {...});` - This line creates a websocket handler which handles incoming messages from the client and sends messages to the client.
6. `app.listen(3000, () => {...});` - This line starts the Express server on port 3000.

## Helpful links

- [Express.js](https://expressjs.com/)
- [Websockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API)

onelinerhub: [How can I use Express.js and websockets together to create real-time applications?](https://onelinerhub.com/expressjs/how-can-i-use-express-js-and-websockets-together-to-create-real-time-applications)