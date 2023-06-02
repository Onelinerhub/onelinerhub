# How do I install PHP Redis on Windows?
// plain

1. Download and install Redis on Windows by following the instructions from the [Redis Windows download page](https://github.com/microsoftarchive/redis/releases).
2. Download and install the [PHP Redis extension](https://pecl.php.net/package/redis) for your version of PHP.
3. Install the extension by running the following command in the command prompt:
```
php -r "copy('https://pecl.php.net/get/redis', 'redis.zip');"
```
4. Unzip the file and then run:
```
php -r "chdir('redis'); phpize && ./configure && make && make install"
```
5. Add the following line to your `php.ini` file:
```
extension=redis.so
```
6. Restart your web server.
7. Test the installation by running the following code in the command prompt:
```
php -r "if (new Redis() == true){ echo \"\r\nOK\r\n\"; }"
```
## Output example
 `OK`

onelinerhub: [How do I install PHP Redis on Windows?](https://onelinerhub.com/predis/how-do-i-install-php-redis-on-windows)