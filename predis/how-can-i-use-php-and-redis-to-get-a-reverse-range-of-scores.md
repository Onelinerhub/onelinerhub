# How can I use PHP and Redis to get a reverse range of scores?
// plain

Using PHP and Redis, you can get a reverse range of scores by using the `ZREVRANGE` command. This command takes a start and end score as arguments and returns the elements in the sorted set stored at the key with a score between the start and end.

For example, if you have a Redis sorted set stored at the key `scores` that contains the following elements:

```
scores
1) "bob"
2) "alice"
3) "jane"
```

You can use the following code to get a reverse range of scores between 0 and 10:

```php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);

$result = $redis->zRevRange('scores', 0, 10);

var_dump($result);
```

The output of the above code would be:

```
array(3) {
  [0]=>
  string(4) "jane"
  [1]=>
  string(5) "alice"
  [2]=>
  string(3) "bob"
}
```

The code consists of the following parts:

1. Connecting to the Redis server: `$redis = new Redis(); $redis->connect('127.0.0.1', 6379);`
2. Executing the `ZREVRANGE` command: `$result = $redis->zRevRange('scores', 0, 10);`
3. Printing the result: `var_dump($result);`

## Helpful links

- [Redis Docs - ZREVRANGE](https://redis.io/commands/zrevrange)
- [PHP Redis Docs - ZREVRANGE](https://www.php.net/manual/en/redis.zrevrange.php)

onelinerhub: [How can I use PHP and Redis to get a reverse range of scores?](https://onelinerhub.com/predis/how-can-i-use-php-and-redis-to-get-a-reverse-range-of-scores)