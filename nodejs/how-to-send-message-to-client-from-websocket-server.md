# How to send message to client from websocket server

```js
const WebSocketServer = require('ws');
const wss = new WebSocketServer.Server({ port: 8111 })

wss.on("connection", (ws,r) => {
  ws.send('This is a message to client');
});
```

- `require('ws')` - import [lib:ws](https://www.npmjs.com/package/ws) lib to create websocket server
- `new WebSocketServer.Server` - create and launch websocket server with params
- `port:` - port to listen on (in our case all network interfaces are going to be listened)
- `wss.on("connection"` - what to do when someone connects to our server
- `ws.send(` - send a message to client
- `This is a message to client` - this message will be sent to websocket client

group: websocket


