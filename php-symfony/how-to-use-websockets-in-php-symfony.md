# How to use websockets in PHP Symfony?
// plain

Websockets can be used in PHP Symfony to create real-time applications. To use websockets, the Ratchet library can be used.

## Example code

```
<?php

use Ratchet\Server\IoServer;
use Ratchet\Http\HttpServer;
use Ratchet\WebSocket\WsServer;
use MyApp\Chat;

$server = IoServer::factory(
    new HttpServer(
        new WsServer(
            new Chat()
        )
    ),
    8080
);

$server->run();
```

The code above creates a websocket server on port 8080.

## Code explanation

- `use Ratchet\Server\IoServer;` - imports the IoServer class from the Ratchet library
- `IoServer::factory()` - creates a websocket server
- `new HttpServer()` - creates an HTTP server
- `new WsServer()` - creates a websocket server
- `new Chat()` - creates a chat class
- `$server->run()` - runs the websocket server

## Helpful links
- https://socketo.me/
- https://github.com/ratchetphp/Ratchet

onelinerhub: [How to use websockets in PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-use-websockets-in-php-symfony)