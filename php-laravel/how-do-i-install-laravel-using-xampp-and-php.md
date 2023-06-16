# How do I install Laravel using XAMPP and PHP?
// plain

1. Make sure you have XAMPP and PHP installed on your local machine.
2. Download the latest version of Laravel from the [Laravel website](https://laravel.com/).
3. Unzip the downloaded file and move the extracted folder to the `htdocs` directory of your XAMPP installation.
4. Open the `php.ini` file located in the `xampp/php` directory and enable the following extensions:
    - `extension=php_openssl.dll`
    - `extension=php_mbstring.dll`
    - `extension=php_fileinfo.dll`
5. Open the command prompt and navigate to the laravel project directory.
6. Run the following command to install the Laravel dependencies:
```
composer install
```
7. Once the dependencies are installed, you can start the Laravel server by running the following command:
```
php artisan serve
```

## Output example

```
Laravel development server started: <http://127.0.0.1:8000>
```

onelinerhub: [How do I install Laravel using XAMPP and PHP?](https://onelinerhub.com/php-laravel/how-do-i-install-laravel-using-xampp-and-php)