# How do I use PHP to set a value in Redis?
// plain

You can use the [PHP Redis extension](https://github.com/phpredis/phpredis) to set a value in Redis.

Here is an example code block to set a value in Redis:
```
<?php
    // Connect to Redis
    $redis = new Redis();
    $redis->connect('127.0.0.1', 6379);

    // Set a value
    $redis->set('key', 'value');
?>
```

The code above will set `value` to the `key` in Redis.

The code consists of several parts:

1. `$redis = new Redis();`: Creating a new Redis instance.
2. `$redis->connect('127.0.0.1', 6379);`: Connecting to the Redis server.
3. `$redis->set('key', 'value');`: Setting a value to the key.

You can find more information about how to use the PHP Redis extension in the [documentation](https://github.com/phpredis/phpredis#usage).

onelinerhub: [How do I use PHP to set a value in Redis?](https://onelinerhub.com/predis/how-do-i-use-php-to-set-a-value-in-redis)