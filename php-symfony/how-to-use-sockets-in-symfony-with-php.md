# How to use sockets in Symfony with PHP?
// plain

Sockets are a powerful tool for communication between two or more computers. In Symfony with PHP, sockets can be used to create a connection between a client and a server.

## Example code

```
// Create a socket
$socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);

// Bind the socket to an address/port
socket_bind($socket, '127.0.0.1', 8080);

// Start listening for connections
socket_listen($socket);

// Accept incoming connections
$client = socket_accept($socket);

// Send data to the client
socket_write($client, 'Hello World!');

// Close the client connection
socket_close($client);

// Close the socket
socket_close($socket);
```

## Output example

```
Hello World!
```

## Code explanation

- `socket_create()`: creates a socket and returns a socket resource.
- `socket_bind()`: binds the socket to an address/port.
- `socket_listen()`: starts listening for connections.
- `socket_accept()`: accepts incoming connections.
- `socket_write()`: sends data to the client.
- `socket_close()`: closes the socket.

## Helpful links
- [PHP Sockets](https://www.php.net/manual/en/sockets.examples.php)
- [Symfony Documentation](https://symfony.com/doc/current/components/http_foundation/introduction.html)

onelinerhub: [How to use sockets in Symfony with PHP?](https://onelinerhub.com/php-symfony/how-to-use-sockets-in-symfony-with-php)