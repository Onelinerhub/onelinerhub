# Using Lua scripts in Redis

### Let's execute LUA script that sets and then gets value from Redis:

```php
$redis->eval("redis.call('set', 'l1', 'hi'); return redis.call('get', 'l1');");
```

- `$redis` - Redis object after [connection](/php-redis/how-to-connect-to-redis)
- `eval` - evaluates specified LUA code
- `redis.call` - LUA interface to call Redis methods

group: lua

## Example: 
```php
<?php

$r = new Redis(); 
$r->connect('127.0.0.1', 6379); 

echo $r->eval("redis.call('set', 'l1', 'hi'); return redis.call('get', 'l1');");
```
```
hi
```

