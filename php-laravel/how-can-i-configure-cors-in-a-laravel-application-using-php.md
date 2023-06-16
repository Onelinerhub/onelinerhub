# How can I configure CORS in a Laravel application using PHP?
// plain

Configuring CORS in a Laravel application using PHP can be done in the following steps:

1. In the `app/Http/Kernel.php` file, add the following line in the `$middleware` array:

```
\Fruitcake\Cors\HandleCors::class,
```

2. Create a file named `cors.php` in the `config` directory and add the following code:

```
<?php

return [
    /*
     * You can enable CORS for 1 or multiple paths.
     * Example: ['api/*']
     */
    'paths' => ['api/*'],

    /*
    * Matches the request method. `[*]` allows all methods.
    */
    'allowed_methods' => ['*'],

    /*
     * Matches the request origin. `[*]` allows all origins.
     */
    'allowed_origins' => ['*'],

    /*
     * Matches the request origin with, similar to `Request::is()`
     */
    'allowed_origins_patterns' => [],

    /*
     * Sets the Access-Control-Allow-Headers response header. `[*]` allows all headers.
     */
    'allowed_headers' => ['*'],

    /*
     * Sets the Access-Control-Expose-Headers response header.
     */
    'exposed_headers' => false,

    /*
     * Sets the Access-Control-Max-Age response header.
     */
    'max_age' => false,

    /*
     * Sets the Access-Control-Allow-Credentials header.
     */
    'supports_credentials' => false,
];
```

3. In the `.env` file, set the `CORS_ENABLED` value to `true`:

```
CORS_ENABLED=true
```

4. Finally, run the following command to allow CORS requests:

```
php artisan config:cache
```

This will enable CORS for your Laravel application.

## Code explanation
**

* `app/Http/Kernel.php` - This is the main configuration file for the Laravel application.
* `config/cors.php` - This is the file where the CORS configuration is stored.
* `.env` - This is the environment configuration file for the Laravel application.
* `php artisan config:cache` - This command is used to enable CORS requests.

**## Helpful links**

* [Laravel Docs - Configuring CORS](https://laravel.com/docs/7.x/routing#cors)
* [Fruitcake/laravel-cors Github](https://github.com/fruitcake/laravel-cors)

onelinerhub: [How can I configure CORS in a Laravel application using PHP?](https://onelinerhub.com/php-laravel/how-can-i-configure-cors-in-a-laravel-application-using-php)