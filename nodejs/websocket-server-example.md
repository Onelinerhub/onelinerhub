# Websocket server example

```js
const WebSocketServer = require('ws');
const wss = new WebSocketServer.Server({ port: 8111 })

wss.on("connection", (ws,r) => {
  ws.on("message", data => {
    ws.send('You sent me: ' + data);
  });
  
  ws.on("close", () => { });
  ws.onerror = function () { };
});
```

- `require('ws')` - import [lib:websocket](https://www.npmjs.com/package/ws) lib to create websocket server
- `new WebSocketServer.Server` - create and launch websocket server with params
- `port:` - port to listen on (in our case all network interfaces are going to be listened)
- `wss.on("connection"` - what to do when someone connects to our server
- `ws.on("message"` - what to do when we've received a message from client
- `ws.send(` - send a message to client
- `ws.on("close"` - what to do when client closes connection
- `ws.onerror` - set custom error handler

group: websocket


