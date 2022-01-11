# Save array to Redis

### The best way to store to and get arrays from Redis is to use Redis lists:

```php
$arr = [1, 2, 3];
call_user_func_array([$redis, 'lpush'], array_merge(['list2'], $arr));
```

- `$arr` - sample array to store to Redis
- `call_user_func_array` - will call specified method with custom set of arguments
- `$redis` - Redis object after [connection](/php-redis/how-to-connect-to-redis)
- `lpush` - saves given values to a list
- `array_merge` - merges to arrays
- `list2` - name of the key to store array to in Redis

group: array

## Example: 
```php
<?php

$r = new Redis(); 
$r->connect('127.0.0.1', 6379);

$r->delete('list2');
call_user_func_array([$r, 'lpush'], array_merge(['list2'], [1, 2, 3]));

print_r($r->lrange('list2', 0, -1));
```
```
Array
(
    [0] => 3
    [1] => 2
    [2] => 1
)

```

