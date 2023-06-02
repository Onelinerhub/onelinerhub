# How do I use Redis Lock in a PHP application?
// plain

Using Redis Lock in a PHP application is a simple process. First, you need to install the Redis extension for PHP. Then, you can use the `setnx` command to create a lock. The following code shows an example of how to use Redis Lock in a PHP application:

```
<?php
// Connect to Redis
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);

// Create a lock
$lockKey = 'lock_key';
$lockValue = time();
$lockTTL = 10;
$lock = $redis->setnx($lockKey, $lockValue);

// Set a TTL on the lock
if ($lock) {
    $redis->expire($lockKey, $lockTTL);
}

echo $lock; // 1
?>
```

The output of this example code is `1`, indicating that the lock was successfully created.

## Code explanation


- `$redis = new Redis();`: Connects to the Redis server.
- `$redis->connect('127.0.0.1', 6379);`: Specifies the IP address and port of the Redis server.
- `$lockKey = 'lock_key';`: Specifies the key of the lock.
- `$lockValue = time();`: Specifies the value of the lock.
- `$lockTTL = 10;`: Specifies the time-to-live of the lock.
- `$lock = $redis->setnx($lockKey, $lockValue);`: Creates a lock with the given key and value.
- `$redis->expire($lockKey, $lockTTL);`: Sets a TTL on the lock.

For more information, please refer to the following links:

- [Redis Documentation - SETNX](https://redis.io/commands/setnx)
- [Redis Documentation - EXPIRE](https://redis.io/commands/expire)
- [PHP Manual - Redis](https://www.php.net/manual/en/book.redis.php)

onelinerhub: [How do I use Redis Lock in a PHP application?](https://onelinerhub.com/predis/how-do-i-use-redis-lock-in-a-php-application)