# How do I use the PHP Redis zrevrange command?
// plain

The PHP Redis zrevrange command is used to get the elements of a sorted set with a score in a given range, sorted in descending order.

## Example code

```
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
$redis->zadd('myzset', 1, 'one');
$redis->zadd('myzset', 2, 'two');
$redis->zadd('myzset', 3, 'three');
$values = $redis->zrevrange('myzset', 0, 1);
```

## Output example

```
Array
(
    [0] => three
    [1] => two
)
```

## Code explanation

1. `$redis = new Redis();` - Create a new Redis instance.
2. `$redis->connect('127.0.0.1', 6379);` - Connect to Redis server.
3. `$redis->zadd('myzset', 1, 'one');` - Add an element to a sorted set, with a score of 1.
4. `$redis->zadd('myzset', 2, 'two');` - Add another element to the same sorted set, with a score of 2.
5. `$redis->zadd('myzset', 3, 'three');` - Add a third element to the same sorted set, with a score of 3.
6. `$values = $redis->zrevrange('myzset', 0, 1);` - Get the elements of the sorted set with a score between 0 and 1, sorted in descending order.

## Helpful links
- [PHP Redis Documentation](https://redis.io/clients/php)
- [zrevrange Command](https://redis.io/commands/zrevrange)

onelinerhub: [How do I use the PHP Redis zrevrange command?](https://onelinerhub.com/predis/how-do-i-use-the-php-redis-zrevrange-command)