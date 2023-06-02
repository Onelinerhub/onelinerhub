# How do I use PHP and Redis together to scan data?
// plain

PHP and Redis can be used together to scan data by using the Redis SCAN command. This command will iterate over the keys in a Redis database. An example of how to use the SCAN command in PHP is shown below:

```
$cursor = 0;
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
do {
    list($cursor, $keys) = $redis->scan($cursor);
    foreach($keys as $key) {
        // Process each key
    }
} while ($cursor != 0);
```

The code above will loop through all the keys in the Redis database. The `$keys` variable will contain an array of all the keys. Each of these keys can then be processed in the `foreach` loop.

The following is a list of the parts of the code and what they do:

- `$cursor = 0`: This sets the initial cursor position to `0`.
- `$redis = new Redis()`: This creates a new Redis object.
- `$redis->connect('127.0.0.1', 6379)`: This connects to the Redis server.
- `list($cursor, $keys) = $redis->scan($cursor)`: This is the SCAN command. It will return an array of keys and the new cursor position.
- `foreach($keys as $key)`: This will loop through each key in the array.
- `// Process each key`: This is where you can process each key.
- `while ($cursor != 0)`: This will keep looping until the cursor position is `0`.

For more information about using PHP and Redis together, please see the following links:

- [Redis Quick Start](https://redis.io/topics/quickstart)
- [Redis SCAN Command](https://redis.io/commands/scan)
- [PHP Redis Documentation](https://github.com/phpredis/phpredis#scan)

onelinerhub: [How do I use PHP and Redis together to scan data?](https://onelinerhub.com/predis/how-do-i-use-php-and-redis-together-to-scan-data)