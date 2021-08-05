# Websocket server example

```php
$ws = new Swoole\WebSocket\Server('0.0.0.0', 9504);
$ws->on(
  'message',
  function (Swoole\WebSocket\Server $ws, Swoole\WebSocket\Frame $frame) {
    $ws->push($frame->fd, "Hello, {$frame->data}");
  }
);
$ws->start();
```

- Swoole\WebSocket\Server - Swoole class to launch Websocket server
- '0.0.0.0' - listen on all interfaces
- 9504 - listen on this port
- $ws->on( - listen for specific event on server
- 'message' - do something when we receive message from client
- $ws->push( - send response to client
- "Hello, {$frame->data}" - response message we want to send (`$frame->data` will contain message received from client)

group: websocket
