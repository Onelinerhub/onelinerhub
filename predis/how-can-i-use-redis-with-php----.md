# How can I use Redis with PHP 7.4?
// plain

Using Redis with PHP 7.4 is very easy. You can use the Redis PHP extension to connect to and use Redis from your PHP code.

To install the Redis PHP extension, you can use the following command:
```
$ pecl install redis
```

Once the Redis extension is installed, you can use the following code to connect to a Redis server:
```
<?php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
?>
```

Once connected, you can use the various methods provided by the Redis extension to interact with the Redis server. For example, you can use the `set()` method to set a key-value pair in Redis:
```
<?php
$redis->set('key', 'value');
?>
```

You can also use the `get()` method to get the value of a key from Redis:
```
<?php
$value = $redis->get('key');
echo $value; // Outputs 'value'
?>
```

For more information about using Redis with PHP 7.4, see the [Redis PHP extension documentation](https://redis.io/clients/php).

onelinerhub: [How can I use Redis with PHP 7.4?](https://onelinerhub.com/predis/how-can-i-use-redis-with-php----)