# Save JSON to Redis hash

### We assume our array is not [nested](/php-redis/save-nested-json-to-redis-key) so let's use Redis hashes:

```php
$json = ['a' => 1, 'b' => 2];
array_walk($json, function($v, $k) use ($redis) {
  $redis->hset('json', $k, $v);
});
```

- `$json` - sample JSON to store to Redis
- `array_walk` - iterate through our JSON
- `$redis` - Redis object after [connection](/php-redis/how-to-connect-to-redis)
- `hset` - sets hash key and value
- `json` - name of the hash to save our JSON to

group: json

## Example: 
```php
<?php

$r = new Redis(); 
$r->connect('127.0.0.1', 6379);

$json = ['a' => 1, 'b' => 2];
array_walk($json, function($v, $k) use ($r) {
  $r->hset('json', $k, $v);
});

print_r($r->hgetall('json'));
```
```
Array
(
    [a] => 1
    [b] => 2
)

```

