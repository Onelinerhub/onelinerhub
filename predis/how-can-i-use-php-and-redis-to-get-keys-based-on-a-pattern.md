# How can I use PHP and Redis to get keys based on a pattern?
// plain

Using PHP and Redis together to get keys based on a pattern is possible by using the Redis `KEYS` command. The `KEYS` command takes a pattern as an argument and returns all the keys that match the pattern.

For example, the following code will return all keys that start with "user:".

```
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
$keys = $redis->keys('user:*');
```

## Output example

```
Array
(
    [0] => user:1
    [1] => user:2
    [2] => user:3
)
```

The code consists of the following parts:

1. Creating a Redis instance: `$redis = new Redis();`
2. Connecting to the Redis server: `$redis->connect('127.0.0.1', 6379);`
3. Using the `KEYS` command to get all the keys that match the pattern: `$keys = $redis->keys('user:*');`

For more information, please refer to the [Redis KEYS command documentation](https://redis.io/commands/keys).

onelinerhub: [How can I use PHP and Redis to get keys based on a pattern?](https://onelinerhub.com/predis/how-can-i-use-php-and-redis-to-get-keys-based-on-a-pattern)