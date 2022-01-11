# Redis pub/sub example

```php
$redis->subscribe(['ch1'], function($m) {
  # do something with message
});

$redis->publish('chl', 'hi');
```

- `$redis` - Redis object after [connection](/php-redis/how-to-connect-to-redis)
- `subscribe` - subscribe to a specified channel
- `ch1` - channel name to subscribe/publish to
- `function($m)` - callback will be called when new messages arrives
- `publish` - publish message to specified channel
- `'hi'` - message to publish

## Example: 
```php
<?php

$r = new Redis(); 
$r->connect('127.0.0.1', 6379); 

$r->subscribe(['ch1'], function($m) {
  die($m);
  # do something with message
});

$r->publish('chl', 'hi');
```
```
PHP Fatal error:  Uncaught TypeError: Argument 1 passed to Redis::subscribe() must be of the type array, string given in /tmp/test.php:8
Stack trace:
#0 /tmp/test.php(8): Redis->subscribe()
#1 {main}
  thrown in /tmp/test.php on line 8
```

