# How do I install the PHP Redis module?
// plain

The PHP Redis module provides an API for communicating with the Redis key-value store. To install the module, you need to have [Redis](https://redis.io/) installed and configured first.

Once Redis is installed, you can install the PHP Redis module with [PECL](https://pecl.php.net/). To install with PECL, run the following command in your terminal:

```
pecl install redis
```

The command will install the Redis module and add it to your `php.ini` file. You can then restart your web server to enable the module.

Once the module is enabled, you can use it in your PHP code. For example, to connect to Redis and set a key-value pair, you can use the following code:

```php
<?php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
$redis->set('key', 'value');
```

The code will connect to Redis and set the key `key` with the value `value`.

For more information, you can refer to the [PHP Redis documentation](https://redis.io/clients/php).

onelinerhub: [How do I install the PHP Redis module?](https://onelinerhub.com/predis/how-do-i-install-the-php-redis-module)