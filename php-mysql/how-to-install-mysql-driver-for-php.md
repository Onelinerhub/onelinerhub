# How to install MySQL driver for PHP?
// plain

1. Download the MySQL driver for PHP from the [MySQL website](https://dev.mysql.com/downloads/connector/php/).
2. Extract the downloaded file and copy the `php_mysql.dll` file to the `ext` folder of your PHP installation.
3. Add the following line to your `php.ini` file: `extension=php_mysql.dll`.
4. Restart your web server.
5. Verify the installation by running the following code:
```php
<?php
if (function_exists('mysql_connect')) {
    echo 'MySQL driver is installed!';
}
```
```
MySQL driver is installed!
```

onelinerhub: [How to install MySQL driver for PHP?](https://onelinerhub.com/php-mysql/how-to-install-mysql-driver-for-php)