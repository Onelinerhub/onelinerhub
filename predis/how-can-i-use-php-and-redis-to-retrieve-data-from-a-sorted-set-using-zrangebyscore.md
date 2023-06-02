# How can I use PHP and Redis to retrieve data from a sorted set using ZRANGEBYSCORE?
// plain

Using PHP and Redis, you can retrieve data from a sorted set using ZRANGEBYSCORE by calling the `zrangebyscore` command. This command takes three arguments: the key of the sorted set, the starting score, and the ending score.

For example, the following code block will retrieve all values with scores between 1 and 4 from the sorted set with key `myzset`:

```
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
$values = $redis->zrangebyscore('myzset', 1, 4);
```

This code will return an array of values with scores between 1 and 4 from the sorted set with key `myzset`.

The parts of the code are as follows:

1. `$redis = new Redis();`: This creates a new Redis instance.
2. `$redis->connect('127.0.0.1', 6379);`: This connects to the Redis server.
3. `$values = $redis->zrangebyscore('myzset', 1, 4);`: This calls the `zrangebyscore` command to retrieve values with scores between 1 and 4 from the sorted set with key `myzset`.

## Helpful links

- [PHP Redis Documentation](https://redis.io/clients/php)
- [ZRANGEBYSCORE Command](https://redis.io/commands/zrangebyscore)

onelinerhub: [How can I use PHP and Redis to retrieve data from a sorted set using ZRANGEBYSCORE?](https://onelinerhub.com/predis/how-can-i-use-php-and-redis-to-retrieve-data-from-a-sorted-set-using-zrangebyscore)