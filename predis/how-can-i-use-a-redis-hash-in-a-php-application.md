# How can I use a Redis hash in a PHP application?
// plain

Hash data type in Redis is used to store key-value pairs in a single data structure. It can be used in a PHP application to store data in an efficient way.

## Example code

```
<?php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);

$redis->hSet('user:1', 'name', 'John');
$redis->hSet('user:1', 'age', '25');

echo $redis->hGet('user:1', 'name'); // John
echo $redis->hGet('user:1', 'age');  // 25
```

Parts of the code:

1. `$redis = new Redis();` - Create a new Redis connection.
2. `$redis->connect('127.0.0.1', 6379);` - Connect to Redis server.
3. `$redis->hSet('user:1', 'name', 'John');` - Set a key-value pair in the hash.
4. `$redis->hSet('user:1', 'age', '25');` - Set a key-value pair in the hash.
5. `echo $redis->hGet('user:1', 'name');` - Get a value from the hash using the key.
6. `echo $redis->hGet('user:1', 'age');` - Get a value from the hash using the key.

## Helpful links

* [Redis Documentation](https://redis.io/documentation)
* [PHP Redis Documentation](https://github.com/phpredis/phpredis)
* [Redis Hashes](https://redis.io/topics/data-types#hashes)

onelinerhub: [How can I use a Redis hash in a PHP application?](https://onelinerhub.com/predis/how-can-i-use-a-redis-hash-in-a-php-application)