# How do I remove a key from Redis using PHP?
// plain

Using PHP, you can remove a key from Redis with the following code:

```php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
$redis->del('key');
```

This code will delete the key `key` from the Redis server.

## Code explanation


1. `$redis = new Redis();`: creates a new Redis instance.
2. `$redis->connect('127.0.0.1', 6379);`: connects to the Redis server.
3. `$redis->del('key');`: deletes the key `key` from the Redis server.

## Helpful links

- [Redis PHP documentation](https://redis.io/clients/php)
- [Redis DEL command](https://redis.io/commands/del)

onelinerhub: [How do I remove a key from Redis using PHP?](https://onelinerhub.com/predis/how-do-i-remove-a-key-from-redis-using-php)