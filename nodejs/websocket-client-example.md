# Websocket client example

```js
let ws = require('websocket');
let wsc = new ws.client;

wsc.on('connect', function(connection) {
  connection.sendUTF('Hello');

  connection.on('message', function(message) {
    console.log("Received: " + message.utf8Data);
    connection.close();
  });
});

wsc.connect('ws://echoof.me:8111/');
```

- `require('websocket')` - import [lib:websocket](https://www.npmjs.com/package/websocket) lib to create websocket client

group: websocket

## Example: 
```js
let ws = require('websocket');
let wsc = new ws.client;

wsc.on('connect', function(connection) {
  connection.sendUTF('Hello');

  connection.on('message', function(message) {
    console.log("Received: " + message.utf8Data);
    connection.close();
  });
});

wsc.connect('ws://echoof.me:8111/');
```
```
Received: I got "Hello" from you (1.2.3.4)
```

