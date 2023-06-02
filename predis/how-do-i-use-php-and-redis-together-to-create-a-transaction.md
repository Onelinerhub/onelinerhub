# How do I use PHP and Redis together to create a transaction?
// plain

PHP and Redis can be used together to create a transaction by using the following steps:

1. Establish a connection to the Redis server from PHP using a client library like [Predis](https://github.com/nrk/predis).

```php
$redis = new Predis\Client();
```

2. Use `WATCH` and `MULTI/EXEC` commands to create a transaction block.

```php
$redis->watch('key1');
$redis->multi();
$redis->set('key1', 'value1');
$redis->set('key2', 'value2');
$redis->exec();
```

3. Use `DISCARD` command to discard all the commands in the transaction block.

```php
$redis->discard();
```

4. Use `UNWATCH` command to unlock the keys that were being watched.

```php
$redis->unwatch();
```

5. Use `EXISTS` command to check if the keys have been set.

```php
$redis->exists('key1'); // returns 1 if key exists
```

By following these steps, a transaction can be created using PHP and Redis.

onelinerhub: [How do I use PHP and Redis together to create a transaction?](https://onelinerhub.com/predis/how-do-i-use-php-and-redis-together-to-create-a-transaction)