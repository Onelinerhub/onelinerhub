# How can I reconnect to Redis using PHP?
// plain

To reconnect to Redis using PHP, you can use the [`Redis`](https://github.com/phpredis/phpredis) extension. The following code snippet demonstrates how to connect to a Redis server located on `127.0.0.1` port `6379`:

```php
<?php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
echo "Connection to server sucessfully";
// Check whether server is running or not
echo "Server is running: " . $redis->ping();
?>
```

## Output example

```
Connection to server sucessfully
Server is running: +PONG
```

The code snippet consists of the following parts:
1. `$redis = new Redis();` - create a new instance of the `Redis` class.
2. `$redis->connect('127.0.0.1', 6379);` - connect to the Redis server located on `127.0.0.1` port `6379`.
3. `echo "Connection to server sucessfully";` - print a message indicating that the connection was successful.
4. `echo "Server is running: " . $redis->ping();` - check whether the server is running or not by sending a `PING` command and printing the result.

For more information, please refer to the [PHP Redis extension documentation](https://github.com/phpredis/phpredis).

onelinerhub: [How can I reconnect to Redis using PHP?](https://onelinerhub.com/predis/how-can-i-reconnect-to-redis-using-php)