# How do I enable CORS in a Laravel PHP application?
// plain

To enable CORS in a Laravel PHP application, you must first modify the `config/cors.php` file. This file contains the configuration options for the Laravel CORS package.

You can then use the `\Barryvdh\Cors\HandleCors` middleware to add CORS headers to your routes. For example:

```php
Route::middleware('\Barryvdh\Cors\HandleCors')->get('/api', function () {
    return response('Hello World', 200)
        ->header('Content-Type', 'text/plain');
});
```

The `HandleCors` middleware will add the following CORS headers to the response:

```
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: *
Access-Control-Allow-Headers: *
```

You can also use the `\Barryvdh\Cors\CorsServiceProvider` service provider to configure the CORS package. This allows you to customize the CORS headers for each route, and also set the allowed origins, methods, and headers. For example:

```php
Cors::setHeader('Access-Control-Allow-Origin', 'http://example.com');
```

You can find more information about configuring CORS in the [Laravel CORS documentation](https://github.com/barryvdh/laravel-cors).

onelinerhub: [How do I enable CORS in a Laravel PHP application?](https://onelinerhub.com/php-laravel/how-do-i-enable-cors-in-a-laravel-php-application)