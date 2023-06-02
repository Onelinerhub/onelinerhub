# How do I use a Redis queue in PHP?
// plain

Using Redis queues in PHP is easy. Here's an example of how to do it:

```php
<?php

// Connect to Redis server
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);

// Push a new item to the queue
$redis->rpush('queue', 'item1');

// Pop the item from the queue
$item = $redis->lpop('queue');
echo $item; // Outputs: item1
```

1. Connect to the Redis server using `$redis = new Redis();` and `$redis->connect('127.0.0.1', 6379);`
2. Push a new item to the queue using `$redis->rpush('queue', 'item1');`
3. Pop the item from the queue using `$item = $redis->lpop('queue');`
4. Output the item using `echo $item;`

## Helpful links
- [Redis PHP Client](https://github.com/phpredis/phpredis)
- [Redis List Commands](https://redis.io/commands#list)

onelinerhub: [How do I use a Redis queue in PHP?](https://onelinerhub.com/predis/how-do-i-use-a-redis-queue-in-php)