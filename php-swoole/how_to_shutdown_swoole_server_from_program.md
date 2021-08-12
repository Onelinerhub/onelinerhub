# How to shutdown Swoole server from program

```php
$srv = new Swoole\Server('127.0.0.1', 81);

$srv->on('receive', function ($srv, $fd, $from_id, $data)
{
    if ( trim($data) == 'off' ) {
        $srv->shutdown();
    }
});

$srv->start();
```

- new Swoole\Server - init Swoole server object, listening on `localhost:81`
- on('receive' - handle event when client send us request
- 'off' - let's shut down the server if we receive `off` from client
