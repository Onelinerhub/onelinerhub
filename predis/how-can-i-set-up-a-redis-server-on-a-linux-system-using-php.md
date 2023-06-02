# How can I set up a Redis server on a Linux system using PHP?
// plain

1. Install Redis on your Linux system by running `sudo apt-get install redis-server` in the terminal.
2. Start the Redis server by running `redis-server` in the terminal.
3. Install the [PHP Redis Extension](https://github.com/phpredis/phpredis) using `pecl install redis` in the terminal.
4. Add `extension=redis.so` to your `php.ini` file.
5. Restart your web server to enable the extension.
6. Test the connection to Redis by running the following code:
```php
<?php
$redis = new Redis();
$connected = $redis->connect('127.0.0.1', 6379);
if ($connected) {
    echo 'Connected to Redis';
}
```
## Output example
 `Connected to Redis`
7. You can now start using Redis commands in your PHP code.

onelinerhub: [How can I set up a Redis server on a Linux system using PHP?](https://onelinerhub.com/predis/how-can-i-set-up-a-redis-server-on-a-linux-system-using-php)