# How do I use Redis with Laravel in PHP?
// plain

Using Redis with Laravel in PHP is quite simple.

1. First, you need to install the predis/predis package via Composer:
```
composer require predis/predis
```

2. Then, you need to configure the Redis connection in your `config/database.php` file:
```
'redis' => [
    'client' => 'predis',
    'default' => [
        'host' => env('REDIS_HOST', '127.0.0.1'),
        'password' => env('REDIS_PASSWORD', null),
        'port' => env('REDIS_PORT', 6379),
        'database' => 0,
    ],
],
```

3. Finally, you can use Redis in your code like this:
```
$redis = Redis::connection();
$redis->set('key', 'value');
echo $redis->get('key');
```

## Output example

```
value
```

You can find more information about using Redis with Laravel in the [official documentation](https://laravel.com/docs/5.8/redis).

## Code explanation
**

1. `composer require predis/predis` - Installs the predis/predis package via Composer.
2. `'redis' => [ ... ]` - Configures the Redis connection in the `config/database.php` file.
3. `$redis = Redis::connection();` - Creates a Redis connection.
4. `$redis->set('key', 'value');` - Sets a key-value pair in Redis.
5. `echo $redis->get('key');` - Gets the value of a key from Redis.

**## Helpful links**

1. [Official Laravel Documentation - Redis](https://laravel.com/docs/5.8/redis)

onelinerhub: [How do I use Redis with Laravel in PHP?](https://onelinerhub.com/php-laravel/how-do-i-use-redis-with-laravel-in-php)