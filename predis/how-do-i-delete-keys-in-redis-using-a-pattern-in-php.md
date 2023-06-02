# How do I delete keys in Redis using a pattern in PHP?
// plain

You can use the `Redis::preg_delete()` method to delete keys in Redis using a pattern in PHP. This method takes two arguments: the pattern and the optional `count` argument. The `count` argument is used to limit the number of keys deleted.

## Example code

```
<?php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
$numDeleted = $redis->preg_delete('user:*');
echo "Number of keys deleted: " . $numDeleted;
```
## Output example

```
Number of keys deleted: 3
```

## Code explanation

- `$redis = new Redis();` - Create a new Redis instance.
- `$redis->connect('127.0.0.1', 6379);` - Connect to the Redis server on localhost.
- `$numDeleted = $redis->preg_delete('user:*');` - Delete all keys that match the pattern `user:*`.
- `echo "Number of keys deleted: " . $numDeleted;` - Print out the number of keys deleted.

## Helpful links
- [Redis::preg_delete()](https://redis.io/commands/preg_delete)
- [PHP Redis documentation](https://redis.io/clients/php)

onelinerhub: [How do I delete keys in Redis using a pattern in PHP?](https://onelinerhub.com/predis/how-do-i-delete-keys-in-redis-using-a-pattern-in-php)