# How do I install and use the PHP Redis module?
// plain

1. Install the [PHP Redis module](https://github.com/phpredis/phpredis) using [Composer](https://getcomposer.org/):
```
composer require predis/predis
```

2. Enable the module in your `php.ini` file:
```
extension=redis.so
```

3. Create a Redis connection object:
```php
$redis = new Redis();
```

4. Connect to the Redis server:
```php
$redis->connect('127.0.0.1', 6379);
```

5. Set a key-value pair:
```php
$redis->set('key', 'value');
```

6. Get the value of the key:
```php
$value = $redis->get('key');
// Output: "value"
```

7. Close the connection:
```php
$redis->close();
```

onelinerhub: [How do I install and use the PHP Redis module?](https://onelinerhub.com/predis/how-do-i-install-and-use-the-php-redis-module)