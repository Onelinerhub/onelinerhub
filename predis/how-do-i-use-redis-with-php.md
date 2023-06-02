# How do I use Redis with PHP?
// plain

Using Redis with PHP is easy and requires only a few steps. Here is an example of how to do it:

```php
<?php
// Connecting to Redis server on localhost
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);

// Setting a value
$redis->set("key", "value");

// Getting a value
echo $redis->get("key");
// Output: value
?>
```

1. First, create a new Redis instance using `$redis = new Redis();`.
2. Then, connect to the Redis server using `$redis->connect('127.0.0.1', 6379);`.
3. To set a value, use `$redis->set("key", "value");`.
4. To get a value, use `$redis->get("key");`.

For more information on using Redis with PHP, see the [PHP Redis documentation](https://redis.io/clients/php).

onelinerhub: [How do I use Redis with PHP?](https://onelinerhub.com/predis/how-do-i-use-redis-with-php)