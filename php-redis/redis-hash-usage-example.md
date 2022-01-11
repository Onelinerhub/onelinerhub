# Redis hash usage example

```php
$redis->hset('h1', 'name', 'Donald');
$redis->hset('h1', 'age', '120');

$redis->hgetall('h1');
```

- `$redis` - Redis object after [connection](/php-redis/how-to-connect-to-redis)
- `hset` - sets hash key and value
- `hgetall` - gets all key/values from hash
- `'h1'` - name of the hash to save/get

## Example: 
```php
<?php

$r = new Redis(); 
$r->connect('127.0.0.1', 6379);

$r->hset('h1', 'name', 'Donald');
$r->hset('h1', 'age', '120');

print_r($r->hgetall('h1'));
```
```
Array
(
    [name] => Donald
    [age] => 120
)

```

