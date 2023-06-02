# How can I install and configure PHP and Redis on a Windows system?
// plain

1. Download and install the latest version of [PHP for Windows](https://windows.php.net/download/) and [Redis for Windows](https://github.com/microsoftarchive/redis/releases).
2. Edit the `php.ini` file and add the following line to enable the Redis extension: `extension=php_redis.dll`.
3. Create a `redis.conf` file and add the following lines to configure Redis:
```
port 6379
bind 127.0.0.1
```
4. Open a command prompt and start the Redis server with the `redis-server` command.
5. Open a second command prompt and start the Redis client with the `redis-cli` command.
6. Test the connection to the Redis server with the `ping` command. If successful, it should return `PONG`.
7. Test the PHP Redis extension by running the following code:
```
<?php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
echo $redis->ping();
```

## Output example
 `PONG`

onelinerhub: [How can I install and configure PHP and Redis on a Windows system?](https://onelinerhub.com/predis/how-can-i-install-and-configure-php-and-redis-on-a-windows-system)