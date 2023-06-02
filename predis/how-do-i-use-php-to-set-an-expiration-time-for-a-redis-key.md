# How do I use PHP to set an expiration time for a Redis key?
// plain

You can use PHP to set an expiration time for a Redis key using the `expire()` function. This function takes two parameters: the name of the key and the number of seconds until the key will expire.

For example, the following code will set the key "mykey" to expire after 5 minutes:
```
$redis->expire('mykey', 300);
```

The following is a list of parts of the code and a brief explanation of each:

- `$redis`: The Redis instance.
- `expire()`: The function used to set the expiration time for a Redis key.
- `mykey`: The name of the key.
- `300`: The number of seconds until the key will expire.

For more information, please refer to the [Redis documentation](https://redis.io/commands/expire).

onelinerhub: [How do I use PHP to set an expiration time for a Redis key?](https://onelinerhub.com/predis/how-do-i-use-php-to-set-an-expiration-time-for-a-redis-key)