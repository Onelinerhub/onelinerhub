# How to check Redis version

```php
$redis->info()['redis_version'];
```

- `$redis` - Redis object after [connection](/php-redis/how-to-connect-to-redis)
- `info` - returns system Redis information
- `redis_version` - contains Redis server version

## Example: 
```php
<?php

$r = new Redis();
$r->connect('127.0.0.1', 6379);

echo $r->info()['redis_version'];
```
```
5.0.7
```

