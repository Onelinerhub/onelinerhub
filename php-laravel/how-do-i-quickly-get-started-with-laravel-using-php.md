# How do I quickly get started with Laravel using PHP?
// plain

1. Install the latest version of PHP and a web server such as Apache or Nginx.
2. Install [Composer](https://getcomposer.org/download/), the dependency manager for PHP.
3. Install Laravel using the Composer command `composer create-project laravel/laravel myprojectname --prefer-dist`
4. Configure the database connection in the `.env` file.
5. Generate a key for the application using `php artisan key:generate`
6. Start the development server using `php artisan serve`
7. Create a route in `routes/web.php` and a view in `resources/views` to test your setup.

## Example code

```php
Route::get('/', function () {
    return view('welcome');
});
```

## Output example

```
Laravel development server started: <http://127.0.0.1:8000>
```

onelinerhub: [How do I quickly get started with Laravel using PHP?](https://onelinerhub.com/php-laravel/how-do-i-quickly-get-started-with-laravel-using-php)