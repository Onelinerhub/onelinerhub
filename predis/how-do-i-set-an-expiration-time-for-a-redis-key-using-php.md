# How do I set an expiration time for a Redis key using PHP?
// plain

Using PHP, you can set an expiration time for a Redis key by calling the `setex()` command. This command takes three parameters: the key, the expiration time in seconds, and the value.

For example, the following code sets the key `mykey` to expire in 10 seconds:

```php
$redis->setex('mykey', 10, 'myvalue');
```

The output of this command is `true` if the key was set successfully.

## Code explanation


1. `$redis`: the Redis instance
2. `setex()`: the Redis command for setting an expiration time
3. `mykey`: the key to set
4. `10`: the expiration time in seconds
5. `myvalue`: the value to set

## Helpful links

- [Redis setex command](https://redis.io/commands/setex)
- [PHP Redis documentation](https://github.com/phpredis/phpredis#setex)

onelinerhub: [How do I set an expiration time for a Redis key using PHP?](https://onelinerhub.com/predis/how-do-i-set-an-expiration-time-for-a-redis-key-using-php)