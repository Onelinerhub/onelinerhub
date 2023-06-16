# How do I create a "Hello World" application using PHP and Laravel?
// plain

Creating a "Hello World" application using PHP and Laravel is a quick and easy process.

1. Start by creating a new Laravel project:
```
composer create-project --prefer-dist laravel/laravel hello-world
```

2. Create a route in the routes/web.php file:
```
Route::get('/', function () {
    return 'Hello World';
});
```

3. Start the Laravel development server:
```
php artisan serve
```

4. Visit http://127.0.0.1:8000 in your browser and you should see "Hello World" displayed.

## Code explanation

- composer create-project --prefer-dist laravel/laravel hello-world, to create a new Laravel project
- Route::get('/', function () { return 'Hello World'; });, to create a route in the routes/web.php file
- php artisan serve, to start the Laravel development server

## Helpful links
- [Laravel Documentation](https://laravel.com/docs/7.x)
- [PHP Documentation](https://www.php.net/docs.php)

onelinerhub: [How do I create a "Hello World" application using PHP and Laravel?](https://onelinerhub.com/php-laravel/how-do-i-create-a--hello-world--application-using-php-and-laravel)