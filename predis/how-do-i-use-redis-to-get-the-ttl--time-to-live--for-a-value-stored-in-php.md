# How do I use Redis to get the TTL (time to live) for a value stored in PHP?
// plain

To get the TTL (time to live) for a value stored in PHP using Redis, you can use the `ttl()` function. This function returns the remaining time in seconds before the key will expire.

## Example code

```
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
$ttl = $redis->ttl('key');
echo $ttl;
```

## Output example

```
120
```

Explanation:
1. `$redis = new Redis();`: Create a new Redis instance.
2. `$redis->connect('127.0.0.1', 6379);`: Connect to the Redis server.
3. `$ttl = $redis->ttl('key');`: Get the TTL (time to live) for the key.
4. `echo $ttl;`: Print the TTL value in seconds.

## Helpful links

- [Redis ttl() function](https://redis.io/commands/ttl)
- [PHP Redis documentation](https://redis.io/clients/php)

onelinerhub: [How do I use Redis to get the TTL (time to live) for a value stored in PHP?](https://onelinerhub.com/predis/how-do-i-use-redis-to-get-the-ttl--time-to-live--for-a-value-stored-in-php)