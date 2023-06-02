# How do I use Redis Get and Set commands with PHP?
// plain

The `GET` and `SET` commands are the two primary commands used to interact with Redis from PHP.

Using `GET` to retrieve data from Redis in PHP is as simple as:

```php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
$value = $redis->get('key');
echo $value;
```

The above code will print the value of the key `key` stored in Redis.

Using `SET` to store data in Redis in PHP is as simple as:

```php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
$redis->set('key', 'value');
```

The above code will store the value `value` in the key `key` in Redis.

For more information on using Redis with PHP, see the [Redis PHP documentation](https://redis.io/clients/php).

onelinerhub: [How do I use Redis Get and Set commands with PHP?](https://onelinerhub.com/predis/how-do-i-use-redis-get-and-set-commands-with-php)