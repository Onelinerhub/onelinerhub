# Get keys by pattern

```php
$redis->keys('pattern');
```

- `$redis` - Redis object after [connection](/php-redis/how-to-connect-to-redis)
- `keys` - returns keys that match selected pattern
- `'pattern'` - [pattern to match](https://redis.io/commands/KEYS) keys

group: keys

## Example: 
```php
<?php

$r = new Redis(); 
$r->connect('127.0.0.1', 6379);

print_r($r->keys('tes*'));
```
```
Array
(
    [0] => test
    [1] => test2
)

```

