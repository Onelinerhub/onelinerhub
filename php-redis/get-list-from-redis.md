# Get list from Redis

### This examples is based on [Redis Timeseries](https://onelinerhub.com/redis-timeseries) module:

```php
$redis->rawCommand('TS.RANGE', 'ts_2', 1644415000020, 1644417094099);
```

- `$redis` - Redis object after [connection](/php-redis/how-to-connect-to-redis)
- `rawCommand` - Execute raw Redis command
- `list1` - name of the list to get elements of
- `1,` - index of the first element (starts with `0`, so we're starting from second element)
- `4)` - index of the last element

group: list

## Example: 
```php
<?php

$r = new Redis(); 
$r->connect('127.0.0.1', 6379);

print_r($r->rawCommand('TS.RANGE', 'ts_2', 1644415000020, 1644417094099) );
```
```
Array
(
    [0] => Array
        (
            [0] => 1644416919386
            [1] => 1
        )

    [1] => Array
        (
            [0] => 1644416925338
            [1] => 1
        )

    [2] => Array
        (
            [0] => 1644417094095
            [1] => 1
        )

)

```

