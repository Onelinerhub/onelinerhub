# Connecting to Redis using unix socket

```php
$r = new Redis();
$r->connect("/var/run/redis/redis-server.sock");
```

- `new Redis()` - create Redis object
- `connect(` - connect to specified unix socket
- `/var/run/redis/redis-server.sock` - path to unix socket file from [Redis configuration](/redis/configure-redis-to-use-unix-socket)

## Example: 
```php
<?php

$r = new Redis();
$r->connect("/var/run/redis/redis-server.sock");

echo $r->ping();
```
```
1
```

