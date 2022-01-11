# Save nested JSON to Redis key

```php
$json = ['name' => 'Donald', 'top' => [1, 2, 3]];
$redis->set('js', json_encode($json));

```

- `$json` - sample nested JSON to store to Redis
- `$redis` - Redis object after [connection](/php-redis/how-to-connect-to-redis)
- `set` - save string value to the specified Redis key
- `json_encode` - converts associative array to JSON string
- `'js'` - name of the Redis key to store JSON string to

group: json

## Example: 
```php
<?php

$r = new Redis(); 
$r->connect('127.0.0.1', 6379);

$r->set('js', json_encode(['name' => 'Donald', 'top' => [1, 2, 3]]));

print_r(json_decode($r->get('js'), 1));
```
```
Array
(
    [name] => Donald
    [top] => Array
        (
            [0] => 1
            [1] => 2
            [2] => 3
        )

)

```

