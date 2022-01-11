# How to get all keys from Redis

```php
$redis->keys('*');
```

- `$redis` - Redis object after [connection](/php-redis/how-to-connect-to-redis)
- `keys` - returns keys that match selected pattern
- `'*'` - will match all keys

group: keys

## Example: 
```php
<?php

$r = new Redis(); 
$r->connect('127.0.0.1', 6379);

print_r($r->keys('*'));
```
```
Array
(
    [0] => test
    [1] => d1
    [2] => list1
    # ...
)

```

