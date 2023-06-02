# How can I use Redis to watch for changes in my PHP code?
// plain

Redis can be used to watch for changes in PHP code by using the [`watch`](https://redis.io/commands/watch) command. This command will monitor the given key and will execute an atomic transaction only if the key has not been modified since the last `WATCH` call.

For example, the following code will watch the `my_key` key and will set the `my_value` value if it is not modified.

```php
<?php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
$redis->watch('my_key');
$redis->multi();
$redis->set('my_key', 'my_value');
$redis->exec();
?>
```

This code will output `1` if the transaction is successful, otherwise `0` will be outputted.

## Code explanation


1. `$redis = new Redis();`: This line creates a new Redis instance.
2. `$redis->connect('127.0.0.1', 6379);`: This line connects to the Redis server on `127.0.0.1` port `6379`.
3. `$redis->watch('my_key');`: This line watches the `my_key` key for changes.
4. `$redis->multi();`: This line starts an atomic transaction.
5. `$redis->set('my_key', 'my_value');`: This line sets the `my_value` value for the `my_key` key.
6. `$redis->exec();`: This line executes the atomic transaction.

## Helpful links

- [Redis watch command](https://redis.io/commands/watch)
- [PHP Redis Documentation](https://redis.io/clients/php)

onelinerhub: [How can I use Redis to watch for changes in my PHP code?](https://onelinerhub.com/predis/how-can-i-use-redis-to-watch-for-changes-in-my-php-code)