# PHP redis time series example

```php
$redis->rawCommand('TS.RANGE', 'ts_2', 1644415000020, 1644417094099);
```

- `$redis` - Redis object after [connection](/php-redis/how-to-connect-to-redis)
- `rawCommand` - Execute raw Redis command
- `TS.RANGE` - [lib:RedisTimeSeries](https://onelinerhub.com/redis-timeseries/how-to-install-redis-time-series) command to get time series range
- `ts_2` - name of the time series object
- `1644415000020` - start timestamp (in microseconds)
- `1644417094099` - end timestamp (in microseconds)

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

