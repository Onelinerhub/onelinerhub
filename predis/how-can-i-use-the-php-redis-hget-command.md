# How can I use the PHP Redis HGET command?
// plain

The `HGET` command in PHP Redis is used to retrieve the value of a field in a hash stored at a given key.

```
<?php

$redis = new Redis();
$redis->connect('127.0.0.1', 6379);

$user = $redis->hGet('user', 'name');

echo $user;

// Output: John
?>
```

In the example above, we connect to a Redis server on `127.0.0.1` port `6379`, and then use the `hGet` command to retrieve the value of the `name` field in the `user` hash. The output of the code above is `John`.

The following parts are used in the example code:

* `Redis` - The Redis class in the PHP Redis extension.
* `connect` - A method that connects to a Redis server.
* `hGet` - The hGet command, which retrieves the value of a field in a hash stored at a given key.

For more information, see the [PHP Redis documentation](https://redis.io/clients/php).

onelinerhub: [How can I use the PHP Redis HGET command?](https://onelinerhub.com/predis/how-can-i-use-the-php-redis-hget-command)