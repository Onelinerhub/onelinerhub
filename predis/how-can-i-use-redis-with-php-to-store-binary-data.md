# How can I use Redis with PHP to store binary data?
// plain

You can use Redis with PHP to store binary data by using the Redis PHP extension. This extension provides a client library that allows you to communicate with a Redis server from your PHP code.

To store binary data, you can use the `set()` method of the Redis client. This method takes two arguments, the first being the key and the second being the data.

For example:
```
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
$redis->set('my_binary_data', $binary_data);
```

The `get()` method can then be used to retrieve the data:
```
$binary_data = $redis->get('my_binary_data');
```

The following parts are involved:
- `$redis`: An instance of the Redis client
- `connect()`: Connects to the Redis server
- `set()`: Stores data in Redis
- `get()`: Retrieves data from Redis

## Helpful links
- [Redis PHP extension](https://github.com/phpredis/phpredis)
- [Redis set command](https://redis.io/commands/set)
- [Redis get command](https://redis.io/commands/get)

onelinerhub: [How can I use Redis with PHP to store binary data?](https://onelinerhub.com/predis/how-can-i-use-redis-with-php-to-store-binary-data)