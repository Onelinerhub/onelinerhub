# Set existing key expiration in Redis

```php
$redis->expire('key', 10);
```

- `$redis` - Redis object after [connection](/php-redis/how-to-connect-to-redis)
- `expire` - set existing key expiration in seconds
- `key` - name of the key
- `10` - seconds after which key will expire

group: expire

## Example: 
```php
<?php

$r = new Redis(); 
$r->connect('127.0.0.1', 6379);

$r->set('key', 'test');
$r->expire('key', 10);
sleep(1);

echo $r->ttl('key');
```
```
9
```

