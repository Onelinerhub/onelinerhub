# How can I execute a Redis query using PHP?
// plain

To execute a Redis query using PHP, you can use the [PHP Redis library](https://github.com/phpredis/phpredis). The following example code connects to a Redis server, sets a key-value pair, and retrieves the value:

```php
<?php
// connect to Redis server
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);

// set a key-value pair
$redis->set('key', 'value');

// get the value
$value = $redis->get('key');
echo $value;
// Output: value
```

The code above consists of the following parts:

1. A new instance of the Redis class is created, which is used to connect to the Redis server.
2. The `connect` method is used to establish a connection to the Redis server, which is located at `127.0.0.1` and uses port `6379`.
3. The `set` method is used to set a key-value pair, where `key` is the key and `value` is the value.
4. The `get` method is used to retrieve the value associated with the key.

For more information on how to use the PHP Redis library, please refer to the [documentation](https://github.com/phpredis/phpredis#usage).

onelinerhub: [How can I execute a Redis query using PHP?](https://onelinerhub.com/predis/how-can-i-execute-a-redis-query-using-php)