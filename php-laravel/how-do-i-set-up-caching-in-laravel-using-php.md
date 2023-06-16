# How do I set up caching in Laravel using PHP?
// plain

Setting up caching in Laravel using PHP is fairly straightforward. First, you need to configure the cache configuration in the `config/cache.php` file. Here, you can specify the default cache driver, as well as the connection details for specific drivers.

Once the configuration is set, you can start using the cache. For example, to store a value in the cache:

```php
Cache::put('key', 'value', $minutes);
```

To retrieve a value from the cache:

```php
$value = Cache::get('key');
// Outputs 'value'
echo $value;
```

## Code explanation


- `Cache::put('key', 'value', $minutes)` - Stores a value in the cache with a given key and for a given number of minutes.
- `Cache::get('key')` - Retrieves a value from the cache with a given key.

For more information, see the [Laravel Cache Documentation](https://laravel.com/docs/7.x/cache).

onelinerhub: [How do I set up caching in Laravel using PHP?](https://onelinerhub.com/php-laravel/how-do-i-set-up-caching-in-laravel-using-php)