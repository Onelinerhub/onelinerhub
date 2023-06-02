# How can I use PHP and Redis to get multiple keys?
// plain

You can use PHP and Redis to get multiple keys by using the `Redis::mget` command. This command takes an array of keys and returns an array of values for the requested keys. For example:

```php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);

$keys = array('key1', 'key2', 'key3');
$values = $redis->mget($keys);

print_r($values);
// Output: Array ( [0] => value1 [1] => value2 [2] => value3 )
```

The `Redis::mget` command works as follows:

1. The `$keys` array is passed to the `Redis::mget` command.
2. The `Redis::mget` command looks up the values for each key in the `$keys` array.
3. The values are returned as an array.

For more information, see the [Redis documentation](https://redis.io/commands/mget).

onelinerhub: [How can I use PHP and Redis to get multiple keys?](https://onelinerhub.com/predis/how-can-i-use-php-and-redis-to-get-multiple-keys)