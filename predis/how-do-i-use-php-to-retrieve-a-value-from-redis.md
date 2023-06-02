# How do I use PHP to retrieve a value from Redis?
// plain

Using PHP to retrieve a value from Redis is quite simple. First, you will need to install the [PHP Redis extension](https://github.com/phpredis/phpredis). Once installed, you can connect to a Redis server and retrieve a value.

## Example code

```
<?php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
$value = $redis->get('my_key');
echo $value;
?>
```

The code above will connect to a Redis server on `127.0.0.1` port `6379` and retrieve the value of the key `my_key`. The output of the code would be the value of `my_key`.

The code consists of the following parts:

1. `$redis = new Redis();` - This line creates a new Redis instance.
2. `$redis->connect('127.0.0.1', 6379);` - This line connects to a Redis server on `127.0.0.1` port `6379`.
3. `$value = $redis->get('my_key');` - This line retrieves the value of the key `my_key`.
4. `echo $value;` - This line prints out the value of `my_key`.

onelinerhub: [How do I use PHP to retrieve a value from Redis?](https://onelinerhub.com/predis/how-do-i-use-php-to-retrieve-a-value-from-redis)