# How can I create a persistent connection to Redis using PHP?
// plain

To create a persistent connection to Redis using PHP, you can use the [phpredis](https://github.com/phpredis/phpredis) library.

First, install the library via [Composer](https://getcomposer.org/):

```
composer require predis/predis
```

Then, create a connection to Redis using the `connect` method:

```php
$redis = new Predis\Client([
    'scheme' => 'tcp',
    'host'   => '127.0.0.1',
    'port'   => 6379,
]);
```

You can then use the `set` and `get` methods to store and retrieve data:

```php
$redis->set('hello', 'world');
echo $redis->get('hello'); // prints 'world'
```

Finally, you can use the `persist` method to make the connection persistent:

```php
$redis->persist('hello');
```

For more information, see the [phpredis](https://github.com/phpredis/phpredis) library documentation.

onelinerhub: [How can I create a persistent connection to Redis using PHP?](https://onelinerhub.com/predis/how-can-i-create-a-persistent-connection-to-redis-using-php)