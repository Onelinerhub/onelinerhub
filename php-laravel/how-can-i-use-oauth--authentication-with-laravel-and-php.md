# How can I use OAuth2 authentication with Laravel and PHP?
// plain

OAuth2 authentication is a secure and easy way to authenticate users in a web application. It allows users to authenticate with an external service such as Google, Facebook, Twitter, etc. and then access protected resources in the application.

To use OAuth2 authentication with Laravel and PHP, you can use the [Laravel Passport package](https://laravel.com/docs/5.8/passport). This package provides an easy way to create and manage OAuth2 clients and tokens.

To install the package, run the following command:

```
composer require laravel/passport
```

Once the package is installed, you can register the service provider in your `config/app.php` file:

```php
'providers' => [
    // Other service providers...

    Laravel\Passport\PassportServiceProvider::class,
],
```

To create the tables needed for authentication, run the following command:

```
php artisan migrate
```

To create the encryption keys needed for authentication, run the following command:

```
php artisan passport:install
```

Once the package is installed and configured, you can use the Passport facade to create and manage clients and tokens:

```php
use Laravel\Passport\Passport;

// Create a client
$client = Passport::client()->create([
    'name' => 'My App',
    'redirect' => 'http://example.com/callback',
    'personal_access_client' => true,
    'password_client' => true
]);

// Create a token
$token = Passport::token()->create([
    'client_id' => $client->id,
    'user_id' => auth()->user()->id
]);
```

For more information, see the [Laravel Passport documentation](https://laravel.com/docs/5.8/passport).

onelinerhub: [How can I use OAuth2 authentication with Laravel and PHP?](https://onelinerhub.com/php-laravel/how-can-i-use-oauth--authentication-with-laravel-and-php)