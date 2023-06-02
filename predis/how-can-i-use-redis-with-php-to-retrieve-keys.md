# How can I use Redis with PHP to retrieve keys?
// plain

Using Redis with PHP is fairly straightforward. Below is an example of how to retrieve keys using PHP and Redis.

```
<?php

// Connect to Redis
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);

// Retrieve the keys
$keys = $redis->keys('*');

// Output the keys
foreach($keys as $key) {
    echo $key . "\n";
}

?>
```

The above code will output a list of all the keys stored in Redis.

The code consists of the following parts:

1. Connect to Redis: `$redis = new Redis();` and `$redis->connect('127.0.0.1', 6379);` - This connects to Redis using the `Redis` class and the `connect()` method.

2. Retrieve the keys: `$keys = $redis->keys('*');` - This uses the `keys()` method to retrieve all the keys stored in Redis.

3. Output the keys: `foreach($keys as $key) {` and `echo $key . "\n";` - This uses a `foreach` loop to iterate through the keys and `echo` each one.

For more information, see the [PHP Redis documentation](https://redis.io/clients/php).

onelinerhub: [How can I use Redis with PHP to retrieve keys?](https://onelinerhub.com/predis/how-can-i-use-redis-with-php-to-retrieve-keys)