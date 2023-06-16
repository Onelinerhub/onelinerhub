# How do I use JWT authentication with Laravel in PHP?
// plain

JWT (JSON Web Token) authentication is a popular way for stateless authentication which is using by many modern applications. JWT authentication can be easily implemented with Laravel using the tymondesigns/jwt-auth package.

Below is an example code block for how to use JWT authentication with Laravel:

```php
// Include the package in your composer.json file
composer require tymon/jwt-auth

// Add the service provider to your config/app.php
Tymon\JWTAuth\Providers\JWTAuthServiceProvider::class

// Publish the config file
php artisan vendor:publish --provider="Tymon\JWTAuth\Providers\JWTAuthServiceProvider"

// Generate a secret key
php artisan jwt:secret
```

The example code above will include the package in your composer.json file, add the service provider to your config/app.php, publish the config file, and generate a secret key.

Once the setup is done, you can start using JWT authentication in your routes. For example, you can use the `jwt.auth` middleware in your routes to authenticate users with a valid JWT token.

```php
Route::group(['middleware' => ['jwt.auth']], function () {
    Route::get('/users', function() {
        // All users route logic
    });
});
```

## Helpful links

- [JWT Authentication for Laravel & Lumen](https://jwt-auth.readthedocs.io/en/develop/)
- [Laravel Documentation - Authentication](https://laravel.com/docs/7.x/authentication)

onelinerhub: [How do I use JWT authentication with Laravel in PHP?](https://onelinerhub.com/php-laravel/how-do-i-use-jwt-authentication-with-laravel-in-php)