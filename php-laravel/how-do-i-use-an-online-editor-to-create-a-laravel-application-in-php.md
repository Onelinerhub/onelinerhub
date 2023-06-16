# How do I use an online editor to create a Laravel application in PHP?
// plain

1. To create a Laravel application in PHP using an online editor, first create a project directory on your local computer and open it in the editor.
2. Create a new file called `composer.json` and add the following code:
```json
{
    "require": {
        "laravel/framework": "4.2.*"
    }
}
```
3. Run the command `composer install` to install the Laravel framework.
4. Create a new file called `index.php` and add the following code:
```php
<?php
require 'vendor/autoload.php';
$app = new Laravel\Lumen\Application();
$app->run();
```
5. Run the command `php -S localhost:8000` to start the application.
6. Open a web browser and navigate to `localhost:8000` to view the application.
7. You can now use the online editor to create and modify the Laravel application.

## Helpful links

- [Laravel Documentation](https://laravel.com/docs/5.7)
- [Composer Documentation](https://getcomposer.org/doc/)

onelinerhub: [How do I use an online editor to create a Laravel application in PHP?](https://onelinerhub.com/php-laravel/how-do-i-use-an-online-editor-to-create-a-laravel-application-in-php)