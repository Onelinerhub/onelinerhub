# HTTP request get query string

```php
$http = new Swoole\HTTP\Server('127.0.0.1', 81);
$http->on('Request', function($req, $res) { echo $req->get['id'] . "\n"; });
$http->start();
```

- $http - creates [HTTP server](/php-swoole/http_server_example)
- on('Request' - do something when we got request from client
- $req - Swoole [HTTP Request](https://www.swoole.co.uk/docs/modules/swoole-http-request) object to operate on request
- $req->get['id'] - output `id` param from query string of client request right into server output


## Example
```php
curl 127.0.0.1:81?id=20
```
```
20 // printed on server (not returned to client)
```