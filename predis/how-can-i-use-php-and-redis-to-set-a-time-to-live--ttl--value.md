# How can I use PHP and Redis to set a time-to-live (TTL) value?
// plain

To use PHP and Redis to set a time-to-live (TTL) value, first you need to connect to the Redis server using the `phpredis` extension.

```php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
```

Then, you can set a time-to-live (TTL) value for a key by using the `SETEX` command. The `SETEX` command takes three parameters: the key name, the TTL value in seconds, and the value to set.

```php
$key = 'mykey';
$ttl = 60; // expire in 60 seconds
$value = 'myvalue';

$redis->setex($key, $ttl, $value);
```

You can then check the TTL value of the key by using the `TTL` command.

```php
$ttl = $redis->ttl($key);

echo "TTL of $key is $ttl seconds\n";
// Output: TTL of mykey is 59 seconds
```

You can also delete a key by using the `DEL` command.

```php
$redis->del($key);
```

## Helpful links

- [phpredis](https://github.com/phpredis/phpredis)
- [SETEX command](https://redis.io/commands/setex)
- [TTL command](https://redis.io/commands/ttl)
- [DEL command](https://redis.io/commands/del)

onelinerhub: [How can I use PHP and Redis to set a time-to-live (TTL) value?](https://onelinerhub.com/predis/how-can-i-use-php-and-redis-to-set-a-time-to-live--ttl--value)