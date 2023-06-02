# How do I remove data from Redis using PHP?
// plain

Removing data from Redis using PHP is a simple process. The following example code shows how to delete a key from a Redis server using the [PHP Redis extension](https://github.com/phpredis/phpredis):

```php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
$redis->del('my_key');
```

The above code will delete the key `my_key` from the Redis server.

The code consists of the following parts:

1. `$redis = new Redis();` creates a new instance of the Redis class.
2. `$redis->connect('127.0.0.1', 6379);` connects to the Redis server on `127.0.0.1` with port `6379`.
3. `$redis->del('my_key');` deletes the key `my_key` from the Redis server.

No output is produced by the code.

onelinerhub: [How do I remove data from Redis using PHP?](https://onelinerhub.com/predis/how-do-i-remove-data-from-redis-using-php)