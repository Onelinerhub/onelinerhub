# Get array from Redis

### The best way to store to and get arrays from Redis is to use Redis lists:

```php
$redis->lrange('list2', 0, -1)
```

- `lrange` - returns specified elements from the list
- `list2` - name of the key to get array from (should be a Redis list)
- `0, -1` - offset and limit to use for the elements (`0, -1` - get all elements from start)

group: array

## Example: 
```php
<?php

$r = new Redis(); 
$r->connect('127.0.0.1', 6379);

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

