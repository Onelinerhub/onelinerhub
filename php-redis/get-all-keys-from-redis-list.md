# Get all keys from Redis list

```php
$redis->lrange('list1', 0, -1);
```

- `$redis` - Redis object after [connection](/php-redis/how-to-connect-to-redis)
- `lrange` - returns specified elements from the list
- `list1` - name of the list to get elements of
- `0, -1` - offset and limit to use for the elements (`0, -1` - get all elements from start)

## Example: 
```php
<?php

$r = new Redis(); 
$r->connect('127.0.0.1', 6379);

$r->lpush('list1', 1);
$r->lpush('list1', 2);
$r->lpush('list1', 3);

print_r($r->lrange('list1', 0, -1));
```
```
Array
(
    [0] => 3
    [1] => 2
    [2] => 1
)

```

