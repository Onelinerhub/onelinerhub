# How do I use Laravel Horizon with PHP?
// plain

Laravel Horizon is a queue manager for Laravel applications. It is used to monitor and manage queues in a Laravel application.

Using Laravel Horizon with PHP is a simple process. First, you need to install the Horizon package via Composer:

```
composer require laravel/horizon
```

Once the package is installed, you need to add the Horizon service provider to your `config/app.php` file:

```php
'providers' => [
    // Other Service Providers

    Laravel\Horizon\HorizonServiceProvider::class,
],
```

After that, you need to publish the Horizon configuration and migrations:

```
php artisan horizon:install
```

Then, you need to run the migrations to create the Horizon database tables:

```
php artisan migrate
```

Finally, you can start Horizon with the following command:

```
php artisan horizon
```

For more information on using Laravel Horizon with PHP, please refer to the [Laravel Horizon documentation](https://laravel.com/docs/master/horizon).

onelinerhub: [How do I use Laravel Horizon with PHP?](https://onelinerhub.com/php-laravel/how-do-i-use-laravel-horizon-with-php)