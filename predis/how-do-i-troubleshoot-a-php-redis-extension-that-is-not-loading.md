# How do I troubleshoot a PHP Redis extension that is not loading?
// plain

1. Check the PHP version. The Redis extension is only compatible with PHP 5.2 or later.
2. Check if the extension is installed. Execute the following command in the terminal to check if the Redis extension is installed: ```php -m | grep redis```
3. Check if the extension is enabled. Execute the following command in the terminal to check if the Redis extension is enabled: ```php -i | grep redis```
4. Check if the extension is correctly configured. If the extension is enabled, check if the configuration is correct. The configuration can be found in the php.ini file.
5. Check the log files. If the extension is enabled and configured correctly, check the log files to see if there are any errors.
6. Check the system requirements. The Redis extension requires a few system libraries to be installed. Check if all the libraries are installed.
7. Check the documentation. Check the official documentation for any other requirements that might be necessary to install the extension.

## Helpful links
* [Redis for PHP](https://redis.io/clients/php)
* [PHP Manual: Redis](https://www.php.net/manual/en/book.redis.php)

onelinerhub: [How do I troubleshoot a PHP Redis extension that is not loading?](https://onelinerhub.com/predis/how-do-i-troubleshoot-a-php-redis-extension-that-is-not-loading)