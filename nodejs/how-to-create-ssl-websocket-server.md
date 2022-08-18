# How to create SSL websocket server

```js
const WebSocket = require('ws').Server;
const { createServer } = require("https");
const fs = require("fs");

const server = createServer({
  cert: fs.readFileSync('/path/to/ssl_cert'),
  key: fs.readFileSync('/path/to/ssl_key'),
});

const socket = new WebSocket({ server, });

socket.on(() => {});
server.listen(8765);
```

- `require('ws')` - import [lib:ws](https://www.npmjs.com/package/ws) lib to create websocket server
- `require("https")` - standard lib to create `https` servers
- `require("fs")` - library to manage files
- `createServer(` - create `https` server based on given certificate and key
- `/path/to/ssl_cert` - path to `SSL` certificate file
- `/path/to/ssl_key` - path to `SSL` key file
- `new WebSocket({ server, })` - create websocket based on `https` server
- `socket.on(() => {})` - define [websocket server](https://onelinerhub.com/nodejs/websocket-server-example) handlers
- `server.listen(` - launch `https` server to listen on a given port

group: websocket


