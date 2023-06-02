# How do I use PHP to flush Redis data?
// plain

To flush all data from Redis, you can use the `FLUSHALL` command. To execute this command using PHP, you can use the `Redis::flushAll()` method:

```php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
$redis->flushAll();
```

This will delete all keys from the currently selected database.

The code above consists of the following parts:

1. `$redis = new Redis();`: This creates a new Redis instance.
2. `$redis->connect('127.0.0.1', 6379);`: This connects to a Redis server running on the local machine.
3. `$redis->flushAll();`: This executes the `FLUSHALL` command, which deletes all keys from the currently selected database.

For more information, please see the [PHP Redis documentation](https://redis.io/clients/php).

onelinerhub: [How do I use PHP to flush Redis data?](https://onelinerhub.com/predis/how-do-i-use-php-to-flush-redis-data)