# Set key expiration in Redis

```php
$redis->setex('key', 30, 'test');
```

- `$redis` - Redis object after [connection](/php-redis/how-to-connect-to-redis)
- `setex` - set key value along with expiration in seconds
- `key` - name of the key
- `30` - seconds after which key will expire
- `test` - value of the key

group: expire

## Example: 
```php
<?php

$r = new Redis(); 
$r->connect('127.0.0.1', 6379);

$r->setex('key', 30, 'test');
sleep(1);

echo $r->ttl('key');
```
```
29
```

