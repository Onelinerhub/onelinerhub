# How do I install and configure a PHP Redis DLL on a Windows machine?
// plain

1. Download the latest version of the PHP Redis DLL from [PECL](https://pecl.php.net/package/redis).
2. Extract the `php_redis.dll` from the downloaded archive and place it in the `ext` folder of the PHP installation directory.
3. Add the following line to the `php.ini` file: `extension=php_redis.dll`.
4. Restart the web server.
5. Test if the extension is loaded correctly by executing the following code:
```php
<?php
$redis = new Redis();
if ($redis) {
    echo "Redis is working";
}
```
## Output example
 `Redis is working`
6. Configure the Redis server connection by using the `connect` method:
```php
<?php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
```
7. Verify the connection by using the `ping` method:
```php
<?php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
echo $redis->ping();
```
## Output example
 `+PONG`

onelinerhub: [How do I install and configure a PHP Redis DLL on a Windows machine?](https://onelinerhub.com/predis/how-do-i-install-and-configure-a-php-redis-dll-on-a-windows-machine)