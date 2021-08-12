# Redis connection and get/set example

Make sure to have [Redis extension installed](https://onelinerhub.com/php-redis/install)

```php
Co\run(function()
{
  go(function() {
    $rd = new Redis();
    $rd->connect('127.0.0.1', 6379);
    $rd->set('some', 'val');
    print_r($rd->get('name'));
  });
});
```

- new Redis() - create Redis object
- $rd->connect - connect to Redis server
- $rd->set - save `val` value to `some` key
- $rd->get - get value of `name` key
