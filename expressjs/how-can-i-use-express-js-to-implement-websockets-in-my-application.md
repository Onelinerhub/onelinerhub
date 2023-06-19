# How can I use Express.js to implement websockets in my application?
// plain

Express.js is a web application framework for Node.js that can be used to implement websockets in your application. Websockets are a protocol for bi-directional communication between a server and a client.

To use Express.js to implement websockets, you will need to install the `ws` package.

```
npm install ws
```

Once the `ws` package is installed, you can create a websocket server using the `WebSocket.Server` class. This class takes an `http.Server` instance as an argument.

```
const http = require('http');
const express = require('express');
const WebSocket = require('ws');

const app = express();
const server = http.createServer(app);

const wss = new WebSocket.Server({ server });
```

The `wss` object will be an instance of `WebSocket.Server` that you can use to listen for events and send messages.

To listen for events, you can use the `on` method. This method takes two arguments: the name of the event and a callback function.

```
wss.on('connection', (ws) => {
  ws.on('message', (message) => {
    console.log(`Received message => ${message}`);
  });
});
```

To send a message, you can use the `send` method. This method takes a string as an argument.

```
wss.on('connection', (ws) => {
  ws.send('Hello World!');
});
```

Once you've set up the websocket server, you can start the server using the `listen` method.

```
server.listen(8080, () => {
  console.log('Listening on http://localhost:8080');
});
```

## Output example

```
Listening on http://localhost:8080
```

## Helpful links
- [Express.js](https://expressjs.com/)
- [ws package](https://www.npmjs.com/package/ws)
- [WebSocket.Server class](https://github.com/websockets/ws/blob/master/doc/ws.md#class-websocketserver)

onelinerhub: [How can I use Express.js to implement websockets in my application?](https://onelinerhub.com/expressjs/how-can-i-use-express-js-to-implement-websockets-in-my-application)