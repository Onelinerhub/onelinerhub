# How can I use PHP and Redis together to unlink data?
// plain

PHP and Redis can be used together to unlink data by creating a Redis client and connecting to the server. The following example code creates a Redis client and sets a key-value pair to the server.

```
<?php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
$redis->set('key', 'value');
?>
```

## Code explanation


1. `$redis = new Redis();` - creates a new Redis client instance.
2. `$redis->connect('127.0.0.1', 6379);` - connects to the Redis server.
3. `$redis->set('key', 'value');` - sets a key-value pair to the server.

The output of the code is `TRUE`, indicating the key-value pair was successfully set to the server.

To unlink data, the `$redis->del('key');` command can be used to delete the key-value pair from the server.

## Helpful links

- [Redis PHP tutorial](https://redislabs.com/blog/redis-php-tutorial-getting-started/)
- [Redis commands](https://redis.io/commands)

onelinerhub: [How can I use PHP and Redis together to unlink data?](https://onelinerhub.com/predis/how-can-i-use-php-and-redis-together-to-unlink-data)