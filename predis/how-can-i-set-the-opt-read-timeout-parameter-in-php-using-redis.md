# How can I set the opt_read_timeout parameter in PHP using Redis?
// plain

Setting the opt_read_timeout parameter in PHP using Redis is done using the setOption() method of the Redis class. This method takes two parameters, the option to set and the value to set it to. The opt_read_timeout option controls the amount of time the client will wait for a response from the server before timing out.

## Example code

```
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
$redis->setOption(Redis::OPT_READ_TIMEOUT, 10);
```

This will set the opt_read_timeout option to 10 seconds. The value must be an integer representing the number of seconds to wait for a response from the server before timing out.

## Code explanation


- `$redis = new Redis();` - creates a new Redis instance.
- `$redis->connect('127.0.0.1', 6379);` - connects to the Redis server on localhost.
- `$redis->setOption(Redis::OPT_READ_TIMEOUT, 10);` - sets the opt_read_timeout option to 10 seconds.

For more information on using the setOption() method, please see the [Redis documentation](https://redis.io/commands/setoption).

onelinerhub: [How can I set the opt_read_timeout parameter in PHP using Redis?](https://onelinerhub.com/predis/how-can-i-set-the-opt-read-timeout-parameter-in-php-using-redis)