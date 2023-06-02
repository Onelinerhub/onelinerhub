# How can I use PHP and Redis together with Brew?
// plain

PHP and Redis can be used together with Brew by using Brew to install the Redis PHP extension. This extension provides an API for communicating with Redis servers from within PHP code.

For example, to connect to a Redis server and set a key-value pair, the following code can be used:

```
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
$redis->set('key', 'value');
```

The above code will set the key-value pair `key` -> `value` in the Redis server.

In order to use the Redis PHP extension, the following steps should be taken:

1. Install the Redis PHP extension using Brew: `brew install php-redis`
2. Enable the extension in the `php.ini` file: `extension=redis.so`
3. Restart the web server

For more information on using Redis with PHP, please refer to the [documentation](https://redis.io/clients/php).

onelinerhub: [How can I use PHP and Redis together with Brew?](https://onelinerhub.com/predis/how-can-i-use-php-and-redis-together-with-brew)