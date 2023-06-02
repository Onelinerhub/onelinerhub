# How do I decide when to use pconnect vs connect when working with PHP and Redis?
// plain

When working with PHP and Redis, the `pconnect` and `connect` functions should be used depending on the desired outcome.

`pconnect` stands for persistent connection and it allows a single connection to be reused for multiple requests. This is useful when you are expecting multiple requests to be sent to Redis within a short period of time, as it will reduce the amount of time spent creating and closing connections.

`connect` stands for connection and it will create a new connection to Redis for each request. This is useful when you are expecting a large number of requests to be sent to Redis at different times, as it will reduce the amount of resources used.

An example of using `pconnect` and `connect` is below:

```php
$redis_pconnect = new Redis();
$redis_pconnect->pconnect('127.0.0.1', 6379);

$redis_connect = new Redis();
$redis_connect->connect('127.0.0.1', 6379);
```

The output of the above code will be two Redis connections. The first connection will be a persistent connection and the second connection will be a new connection created for each request.

The decision of when to use `pconnect` or `connect` depends on the use case and the expected number of requests. It is recommended to use `pconnect` when you are expecting multiple requests to be sent to Redis within a short period of time and `connect` when you are expecting a large number of requests to be sent to Redis at different times.

## Helpful links
- [Redis PHP Documentation](https://redis.io/clients/php)
- [Redis Connections](https://redis.io/topics/connections)

onelinerhub: [How do I decide when to use pconnect vs connect when working with PHP and Redis?](https://onelinerhub.com/predis/how-do-i-decide-when-to-use-pconnect-vs-connect-when-working-with-php-and-redis)