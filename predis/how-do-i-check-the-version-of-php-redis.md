# How do I check the version of PHP Redis?
// plain

To check the version of PHP Redis, you can use the `Redis::info()` method. This method returns an associative array with information about the server, including the version.

## Example

```php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);

$info = $redis->info();
echo $info['redis_version'];
```
## Output example

```
5.0.5
```

The `Redis::info()` method has the following parts:

- `$redis`: The instance of the Redis class.
- `connect()`: A method to connect to a Redis server.
- `$info`: The associative array containing information about the server.
- `redis_version`: The key of the associative array containing the version of the Redis server.

For more information, please refer to the [PHP Redis Documentation](https://redis.io/clients/php).

onelinerhub: [How do I check the version of PHP Redis?](https://onelinerhub.com/predis/how-do-i-check-the-version-of-php-redis)