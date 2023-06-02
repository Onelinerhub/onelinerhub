# How do I use PHP to subscribe to Redis?
// plain

Using PHP to subscribe to Redis is easy.

First, you need to install the phpredis extension for PHP. This can be done with `pecl install redis`.

Then you can use the following code to subscribe to a Redis channel:

```php
<?php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
$redis->subscribe(array('channel1', 'channel2'), function($redis, $channel, $message) {
    echo "Channel $channel received $message\n";
});
?>
```
This will subscribe to the two channels `channel1` and `channel2`. When a message is sent to either of these channels, the callback function will be called with the channel name and the message as parameters.

## Code explanation

- `$redis = new Redis();`: Creates a new Redis instance.
- `$redis->connect('127.0.0.1', 6379);`: Connects to the Redis server.
- `$redis->subscribe(array('channel1', 'channel2'), function($redis, $channel, $message) {...});`: Subscribes to the channels `channel1` and `channel2`.
- `echo "Channel $channel received $message\n";`: Prints the channel name and message when a message is received.

## Helpful links
- [phpredis](https://github.com/phpredis/phpredis#subscribe)
- [Redis Pub/Sub](https://redis.io/topics/pubsub)

onelinerhub: [How do I use PHP to subscribe to Redis?](https://onelinerhub.com/predis/how-do-i-use-php-to-subscribe-to-redis)