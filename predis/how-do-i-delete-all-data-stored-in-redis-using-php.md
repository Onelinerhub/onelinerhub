# How do I delete all data stored in Redis using PHP?
// plain

To delete all data stored in Redis using PHP, you can use the Redis `flushall()` command. This command will delete all keys in all existing databases in Redis.

## Example code

```
<?php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
$redis->flushall();
?>
```

No output is produced with this command.

The code above consists of the following parts:
1. `$redis = new Redis();`: This creates a new Redis instance.
2. `$redis->connect('127.0.0.1', 6379);`: This connects to the Redis server at the given host and port.
3. `$redis->flushall();`: This command deletes all keys in all existing databases in Redis.

## Helpful links
- [Redis Documentation for flushall()](https://redis.io/commands/flushall)
- [PHP Redis Documentation](https://github.com/phpredis/phpredis)

onelinerhub: [How do I delete all data stored in Redis using PHP?](https://onelinerhub.com/predis/how-do-i-delete-all-data-stored-in-redis-using-php)