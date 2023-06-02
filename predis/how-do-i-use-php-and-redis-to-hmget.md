# How do I use PHP and Redis to HMGET?
// plain

PHP and Redis can be used together to perform a HMGET command. The HMGET command allows you to retrieve multiple values from a hash stored in Redis.

To use the HMGET command in PHP, you must first connect to the Redis server using the `connect()` method of the `Redis` class. Then, you can use the `hMGet()` method of the `Redis` class to perform the HMGET command.

For example:
```
<?php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
$values = $redis->hMGet('myhash', array('field1', 'field2'));
print_r($values);
?>
```

This example code connects to a Redis server running on `127.0.0.1` port `6379`, and then retrieves the values stored in the `field1` and `field2` fields of the `myhash` hash. The output of this code is:
```
Array
(
    [field1] => value1
    [field2] => value2
)
```

The code consists of the following parts:
1. `$redis = new Redis();` - creates a new instance of the `Redis` class.
2. `$redis->connect('127.0.0.1', 6379);` - connects to the Redis server running on `127.0.0.1` port `6379`.
3. `$values = $redis->hMGet('myhash', array('field1', 'field2'));` - retrieves the values stored in the `field1` and `field2` fields of the `myhash` hash.
4. `print_r($values);` - prints the values retrieved from the `myhash` hash.

## Helpful links
- [Redis PHP Client](https://github.com/phpredis/phpredis)
- [HMGET Command](https://redis.io/commands/hmget)

onelinerhub: [How do I use PHP and Redis to HMGET?](https://onelinerhub.com/predis/how-do-i-use-php-and-redis-to-hmget)