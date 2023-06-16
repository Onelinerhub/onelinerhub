# How do I install Laravel using PHP?
// plain

1. To install Laravel using PHP, first make sure you have the latest version of PHP installed. You can check your version of PHP with the following command in your terminal:
```
php -v
```

2. If you need to update your version of PHP, you can do so by following the instructions for your specific operating system.

3. Once you have the latest version of PHP installed, you can install Laravel using Composer. Composer is a dependency manager for PHP that allows you to easily install packages from the command line.

4. To install Laravel using Composer, use the following command in your terminal:
```
composer create-project --prefer-dist laravel/laravel project-name
```

5. This will create a new directory in your current working directory with the name of the project you specified and install all of the necessary Laravel dependencies.

6. Once the installation is complete, you can start the development server with the following command:
```
php artisan serve
```

7. This will start a local development server on http://localhost:8000. You can now access the Laravel application in your browser.

## Helpful links

- [Installing PHP](https://www.php.net/manual/en/install.php)
- [Composer](https://getcomposer.org/)
- [Laravel Installation](https://laravel.com/docs/6.x/installation)

onelinerhub: [How do I install Laravel using PHP?](https://onelinerhub.com/php-laravel/how-do-i-install-laravel-using-php-1686942004)