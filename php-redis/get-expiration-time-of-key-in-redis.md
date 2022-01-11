# Get expiration time of key in Redis

```php
$redis->ttl('key');
```

- `$redis` - Redis object after [connection](/php-redis/how-to-connect-to-redis)
- `ttl` - returns seconds left for the key to live
- `key` - name of the key to get expiration for

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

## Additional keywords
- ttl

