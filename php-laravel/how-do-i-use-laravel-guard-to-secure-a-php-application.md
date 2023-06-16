# How do I use Laravel Guard to secure a PHP application?
// plain

Laravel Guard is a powerful authentication system used to secure a PHP application. It allows developers to quickly configure authentication for their application.

To use Laravel Guard, first create a file called `auth.php` in the `config` directory. This file will contain the configuration for authentication.

Next, create a User model and a migration for the User model. This will allow Laravel to store and retrieve user data from the database.

Then, in the auth.php file, configure the authentication guard. In the example below, we are setting the default guard to use the 'web' guard.

```php
'guards' => [
    'web' => [
        'driver' => 'session',
        'provider' => 'users',
    ],
],
```

Finally, add the authentication middleware to the routes that need to be protected. This will ensure that only authenticated users can access those routes.

```php
Route::middleware('auth')->group(function () {
    // Protected routes
});
```

By following these steps, you can use Laravel Guard to secure a PHP application.

## Helpful links

- [Laravel Authentication Documentation](https://laravel.com/docs/7.x/authentication)
- [Laravel Authentication Guard](https://laravel.com/docs/7.x/authentication#guard-configuration)
- [Laravel Middleware](https://laravel.com/docs/7.x/middleware)

onelinerhub: [How do I use Laravel Guard to secure a PHP application?](https://onelinerhub.com/php-laravel/how-do-i-use-laravel-guard-to-secure-a-php-application)