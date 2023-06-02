# How do I install Redis on Windows using PHP?
// plain

1. Download Redis for Windows from the [official website](https://github.com/microsoftarchive/redis/releases).
2. Extract the files to the desired location.
3. Open the command prompt and navigate to the Redis folder.
4. Run the following command to start the Redis server:
```
redis-server.exe
```
5. To check the server is running, run the command:
```
redis-cli.exe ping
```
## Output example

```
PONG
```
6. Install the Redis extension for PHP using the following command:
```
pecl install redis
```
7. To enable the extension in PHP, add the following line to php.ini:
```
extension=redis.so
```

onelinerhub: [How do I install Redis on Windows using PHP?](https://onelinerhub.com/predis/how-do-i-install-redis-on-windows-using-php)