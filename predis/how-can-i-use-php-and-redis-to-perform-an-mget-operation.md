# How can I use PHP and Redis to perform an MGET operation?
// plain

PHP and Redis can be used together to perform an MGET operation. To do this, you need to install the Redis PHP extension and use the `MGET` command. Here is an example of how to use the `MGET` command in PHP:

```
<?php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
$values = $redis->mget(['key1', 'key2', 'key3']);
print_r($values);
?>
```

This example will output the values stored in the keys `key1`, `key2`, and `key3`:

```
Array
(
    [0] => value1
    [1] => value2
    [2] => value3
)
```

## Code explanation


1. `$redis = new Redis();` - This creates a new Redis object.
2. `$redis->connect('127.0.0.1', 6379);` - This connects to the Redis server on localhost.
3. `$values = $redis->mget(['key1', 'key2', 'key3']);` - This uses the `MGET` command to get the values stored in the keys `key1`, `key2`, and `key3`.
4. `print_r($values);` - This prints out the values stored in the keys.

## Helpful links

- [Redis PHP Extension](https://redis.io/clients/php)
- [Redis MGET Command](https://redis.io/commands/mget)

onelinerhub: [How can I use PHP and Redis to perform an MGET operation?](https://onelinerhub.com/predis/how-can-i-use-php-and-redis-to-perform-an-mget-operation)