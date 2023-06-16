# How do I install Laravel using PHP?
// plain

Installing Laravel using PHP is a relatively easy process.

1. First, you need to make sure you have the necessary dependencies installed. This includes PHP 7.2 or higher, along with the OpenSSL, PDO, Mbstring, Tokenizer, XML, and Ctype PHP extensions.

2. Next, you need to download the Laravel installer using Composer. You can do this by running the following command in your terminal:

```
composer global require laravel/installer
```

3. After the Laravel installer is installed, you can create a new project using the `laravel new` command. For example, to create a project called "myproject", you would run the following command:

```
laravel new myproject
```

4. Once the project is created, you can move into the project directory and start the development server using the `php artisan serve` command. This will start a development server at http://localhost:8000:

```
cd myproject
php artisan serve
```

5. Finally, you can access your project in your web browser at http://localhost:8000.

## Helpful links

- [Laravel Installation Documentation](https://laravel.com/docs/7.x/installation)
- [Composer Installation Documentation](https://getcomposer.org/doc/00-intro.md)

onelinerhub: [How do I install Laravel using PHP?](https://onelinerhub.com/php-laravel/how-do-i-install-laravel-using-php)