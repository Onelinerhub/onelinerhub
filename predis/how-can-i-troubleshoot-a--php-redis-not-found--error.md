# How can I troubleshoot a "PHP Redis Not Found" error?
// plain

1. First, check that the [Redis](https://redis.io/) server is running and that the connection is established. To check the connection, use the `redis-cli` command line tool:
```
$ redis-cli ping
PONG
```

2. If the connection is established, then the issue is likely a configuration issue. Check the `php.ini` file for the correct settings for Redis. The settings should look something like this:
```
extension=redis.so
session.save_handler = redis
session.save_path = "tcp://hostname:6379?auth=password"
```

3. If the settings are correct, then check the version of PHP and Redis installed. Make sure that they are compatible.

4. If the version is not compatible, then try to upgrade either PHP or Redis to the latest version.

5. If the issue persists, then check the logs for more information. This could provide clues as to why the connection is not working.

6. If the logs do not provide any useful information, then try to restart the Redis server and try to connect again.

7. If the issue still persists, then check the [official documentation](https://redis.io/documentation) for troubleshooting tips.

onelinerhub: [How can I troubleshoot a "PHP Redis Not Found" error?](https://onelinerhub.com/predis/how-can-i-troubleshoot-a--php-redis-not-found--error)