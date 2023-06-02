# How can I resolve the "PHP Class Not Found" error when using Redis?
// plain

The "PHP Class Not Found" error is a common issue that occurs when using Redis. To resolve this error, you must first ensure that the correct version of the Redis PHP extension is installed. This can be done by running the following command in the terminal:

```
php -m | grep redis
```

If the output of this command does not contain the correct version of the Redis extension, you will need to install it. For example, if you are using PHP 7.3, you can install the Redis extension with the command:

```
sudo pecl install redis
```

Once the extension is installed, you will need to enable it in the `php.ini` file. To do this, you will need to add the following line to the `php.ini` file:

```
extension=redis.so
```

Finally, you will need to restart your web server for the changes to take effect. After restarting the web server, you should be able to use the Redis extension without any errors.

## Code explanation
**
- `php -m | grep redis`: This command is used to check if the correct version of the Redis PHP extension is installed.
- `sudo pecl install redis`: This command is used to install the Redis extension for the correct version of PHP.
- `extension=redis.so`: This line is added to the `php.ini` file to enable the Redis extension.

**## Helpful links**
- [How to Install the Redis PHP Extension](https://www.digitalocean.com/community/tutorials/how-to-install-the-redis-php-extension-on-ubuntu-18-04)
- [PHP: redis - Manual](https://www.php.net/manual/en/book.redis.php)

onelinerhub: [How can I resolve the "PHP Class Not Found" error when using Redis?](https://onelinerhub.com/predis/how-can-i-resolve-the--php-class-not-found--error-when-using-redis)