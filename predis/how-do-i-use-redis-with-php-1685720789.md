# How do I use Redis with PHP?
// plain

Using Redis with PHP is relatively simple. To get started, you'll need to install the [phpredis](https://github.com/phpredis/phpredis) extension. Once installed, you can use the following example code to connect to Redis:

```php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
```

Once connected, you can use the various methods provided by the Redis class to interact with Redis. For example, to set a key-value pair:

```php
$redis->set('my_key', 'my_value');
```

You can also get values from Redis:

```php
$value = $redis->get('my_key'); // $value is now "my_value"
```

You can also use Redis to store and retrieve complex data structures such as hashes, lists, and sets. For example, to store a hash:

```php
$redis->hmset('my_hash', array('key1' => 'value1', 'key2' => 'value2'));
```

And to retrieve the hash:

```php
$hash = $redis->hgetall('my_hash'); // $hash is now array('key1' => 'value1', 'key2' => 'value2')
```

These are just a few examples of how to use Redis with PHP. For more information, see the [phpredis](https://github.com/phpredis/phpredis) documentation.

onelinerhub: [How do I use Redis with PHP?](https://onelinerhub.com/predis/how-do-i-use-redis-with-php-1685720789)