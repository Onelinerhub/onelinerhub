# How can I fix PHP Redis when it is not working?
// plain

1. First, check to make sure that the Redis server is running and listening on the correct port. To do this, open a terminal and enter the command `redis-cli ping`. If the output is `PONG`, the server is running.

2. If the server is running, check your PHP configuration and make sure that the Redis extension is installed and enabled. To check if the extension is installed, enter the command `php -m` and look for `redis` in the output. To enable the extension, open `php.ini` and uncomment the line `extension=redis`.

3. If the extension is installed and enabled, check the connection parameters in your code. Make sure that the host, port, and authentication parameters are correct. Here is an example of code that connects to a Redis server:

```
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
$redis->auth('password');
```

4. If the connection parameters are correct, try resetting the connection. Here is an example of code that resets the connection:

```
$redis->close();
$redis->connect('127.0.0.1', 6379);
$redis->auth('password');
```

5. If the connection is still not working, check the firewall rules on the server. Make sure that the port is open and that traffic is allowed.

6. If the firewall rules are correct, try restarting the Redis server. To do this, enter the command `sudo service redis restart`.

7. If the server still isn't working, try reinstalling the Redis server. First, enter the command `sudo apt-get remove redis-server` to remove the existing server. Then, enter the command `sudo apt-get install redis-server` to install the new server.

## Helpful links
- [Redis Quick Start](https://redis.io/topics/quickstart)
- [PHP Redis Documentation](https://www.php.net/manual/en/book.redis.php)

onelinerhub: [How can I fix PHP Redis when it is not working?](https://onelinerhub.com/predis/how-can-i-fix-php-redis-when-it-is-not-working)