# HTTP server example

```php
$http = new Swoole\HTTP\Server('127.0.0.1', 81);
$http->on('Request', function($req, $res) { $res->end('<b>Hey</b> you!'); });
$http->start();
```

- Swoole\HTTP\Server - class that implements HTTP server capabilities
- 127.0.0.1 - listen on localhost interface
- 81 - listen on 81 port
- on('Request' - define callback for HTTP requests made to our server
- $res->end - send response to HTTP client with specified HTML
- ->start() - Launch HTTP server


## Example
```php
curl 127.0.0.1:81
```
```
<b>Hey</b> you!
```