# How can I delete keys in Redis that match a specific pattern using PHP?
// plain

Using the `scan` and `del` commands, you can delete keys in Redis that match a specific pattern using PHP.

```
<?php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);

// Get keys matching pattern
$iterator = NULL;
$keys = $redis->scan($iterator, 'my-key-*');

// Delete keys
foreach ($keys as $key) {
    $redis->del($key);
}
```

This code will search for all keys that begin with `my-key-` and delete them.

## Code explanation


1. `$redis = new Redis();` - Instantiate a new Redis client
2. `$redis->connect('127.0.0.1', 6379);` - Connect to the Redis server
3. `$iterator = NULL;` - Set the iterator to NULL
4. `$keys = $redis->scan($iterator, 'my-key-*');` - Use the `scan` command to get all keys that match the pattern `my-key-*`
5. `foreach ($keys as $key) {` - Loop through all of the keys
6. `$redis->del($key);` - Use the `del` command to delete each key
7. `}` - End the loop

## Helpful links

- [PHP Redis Documentation](https://github.com/phpredis/phpredis#scan)
- [Redis Documentation](https://redis.io/commands/scan)

onelinerhub: [How can I delete keys in Redis that match a specific pattern using PHP?](https://onelinerhub.com/predis/how-can-i-delete-keys-in-redis-that-match-a-specific-pattern-using-php)