# Get multiple keys from Redis

```php
$redis->mget(['a', 'b']);
```

- `$redis` - Redis object after [connection](/php-redis/how-to-connect-to-redis)
- `mget` - gets values of specified keys
- `['a', 'b']` - list of keys to get values of

## Example: 
```php
<?php

$r = new Redis(); 
$r->connect('127.0.0.1', 6379);

$r->set('a', 1);
$r->set('b', 2);

print_r($r->mget(['a', 'b']));
```
```
Array
(
    [0] => 1
    [1] => 2
)

```

