# How can I use the Redis setnx command in PHP?
// plain

The `setnx` command in Redis is used to set a key only if it does not already exist. This can be used to ensure that a key is only ever set once.

In PHP, the `setnx` command can be used with the `Redis` class. The following example code will set the key `mykey` to the value `myvalue` only if the key does not already exist:

```php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
$set = $redis->setnx('mykey', 'myvalue');
echo $set;
```

The output of the example code will be `1` if the key is successfully set, or `0` if the key already exists.

The parts of the example code are:

1. `$redis = new Redis();` - creates a new instance of the `Redis` class.
2. `$redis->connect('127.0.0.1', 6379);` - connects to the Redis server.
3. `$set = $redis->setnx('mykey', 'myvalue');` - sets the key `mykey` to the value `myvalue` only if it does not already exist.
4. `echo $set;` - prints the result of the `setnx` command.

For more information, see the [PHP Redis documentation](https://www.php.net/manual/en/book.redis.php).

onelinerhub: [How can I use the Redis setnx command in PHP?](https://onelinerhub.com/predis/how-can-i-use-the-redis-setnx-command-in-php)