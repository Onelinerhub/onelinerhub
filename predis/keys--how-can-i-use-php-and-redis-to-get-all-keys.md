# keys

How can I use PHP and Redis to get all keys?
// plain

You can use the `Redis::keys()` method in PHP to get all the keys present in the Redis database. This method takes a pattern as its argument and returns an array of keys that match the pattern. For example, the following code will return all the keys that start with 'user:':

```php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
$keys = $redis->keys('user:*');
```

The output of the above code will be an array of keys that start with `user:`, for example:

```
Array
(
    [0] => user:1
    [1] => user:2
    [2] => user:3
    [3] => user:4
)
```

## Code explanation


1. `$redis = new Redis();` - creates a new instance of the Redis class.
2. `$redis->connect('127.0.0.1', 6379);` - connects to the Redis server on the specified host and port.
3. `$keys = $redis->keys('user:*');` - gets all the keys that start with 'user:' from the Redis database.

## Helpful links

- [Redis documentation](https://redis.io/commands/keys)
- [PHP Redis documentation](https://www.php.net/manual/en/book.redis.php)

onelinerhub: [keys

How can I use PHP and Redis to get all keys?](https://onelinerhub.com/predis/keys--how-can-i-use-php-and-redis-to-get-all-keys)