# How to get client IP in websocket server

```js
const WebSocketServer = require('ws');
const wss = new WebSocketServer.Server({ port: 8111 })

wss.on("connection", (ws,r) => {
  ws.on("message", data => {
    let client_ip = r.socket.remoteAddress;
  });
});
```

- `require('ws')` - import [lib:websocket](https://www.npmjs.com/package/ws) lib to create websocket server
- `new WebSocketServer.Server` - create and launch websocket server with params
- `port:` - port to listen on (in our case all network interfaces are going to be listened)
- `wss.on("connection"` - what to do when someone connects to our server
- `ws.on("message"` - what to do when we've received a message from client
- `r.socket.remoteAddress` - returns websocket client IP

group: websocket


