# Websocket client example

```php
include 'client.php';
$w = new WebSocketClient('127.0.0.1', 9504);
$w->connect();
$w->send('test');
echo $w->recv();

```

- client.php - include example [websocket implementation](https://github.com/nonunicorn/php-swoole-websocket-client/blob/main/client.php) based on Swoole
- WebSocketClient - websocket wrapper class
- '127.0.0.1', 9504 - [websocket server](/php-swoole/websocket_server) to connect to
- connect() - connect to server
- send('test') - send some message to server
- echo $w->recv() - get response from server and print it

## Example
```php
// ...
$w->send('test');
echo $w->recv();
```
```bash
Hello, test
```

group: websocket
