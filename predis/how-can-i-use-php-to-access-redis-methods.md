# How can I use PHP to access Redis methods?
// plain

PHP can be used to access Redis methods by using the [PHP Redis extension](https://github.com/phpredis/phpredis). This extension provides an API for communicating with Redis and supports most of the Redis commands.

For example, to set a key-value pair in Redis, the `set()` method can be used:

```
<?php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
$redis->set('key', 'value');
echo $redis->get('key');

// Output: value
?>
```

The code above:

1. Creates a new Redis instance with `$redis = new Redis()`
2. Connects to the Redis server with `$redis->connect('127.0.0.1', 6379)`
3. Sets a key-value pair with `$redis->set('key', 'value')`
4. Gets the value of the key with `$redis->get('key')`

For more information and examples, please see the [PHP Redis extension documentation](https://github.com/phpredis/phpredis#usage).

onelinerhub: [How can I use PHP to access Redis methods?](https://onelinerhub.com/predis/how-can-i-use-php-to-access-redis-methods)