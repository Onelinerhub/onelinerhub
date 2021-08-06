# CLI server example

```php
use Swoole\Http\Server;
use Swoole\Http\Request;
use Swoole\Http\Response;

$srv = new Swoole\HTTP\Server('127.0.0.1', 81);

$srv->on("Start", function($srv) { echo "Started"; });
$srv->on("Request", function($req, $res) { $res->end('Hi'); });

$srv->start();
```

- $srv - variable will contain server object
