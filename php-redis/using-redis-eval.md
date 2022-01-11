# Using Redis eval

```php
$redis->eval("return redis.call('get', 'test');");
```

- `$redis` - Redis object after [connection](/php-redis/how-to-connect-to-redis)
- `eval` - evaluates specified LUA code
- `redis.call('get', 'test')` - LUA code to get key value from Redis

group: lua

## Example: 
```php
<?php

$r = new Redis(); 
$r->connect('127.0.0.1', 6379); 

echo $r->eval("return redis.call('get', 'test');");
```
```
1
```

