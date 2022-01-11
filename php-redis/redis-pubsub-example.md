# Redis pub/sub example

```php
# run from first script
$redis->subscribe(['ch1'], function($m) {
  # do something with message
});

# run from second script
$redis->publish('chl', 'hi');
```

- `$redis` - Redis object after [connection](/php-redis/how-to-connect-to-redis)
- `subscribe` - subscribe to a specified channel(will wait till message arrived)
- `ch1` - channel name to subscribe/publish to
- `function($m)` - callback will be called when new messages arrives
- `publish` - publish message to specified channel
- `'hi'` - message to publish

## Example: 
```php
<?php

$r = new Redis(); 
$r->connect('127.0.0.1', 6379); 

$r->subscribe(['ch1'], function($r, $c, $m) {
  die($m);
});

# run this from different script
# $r->publish('chl', 'hi');
```
```
PHP Fatal error:  Uncaught Error: Object of class Redis could not be converted to string in /tmp/test.php:9
Stack trace:
#0 [internal function]: {closure}()
#1 /tmp/test.php(11): Redis->subscribe()
#2 {main}
  thrown in /tmp/test.php on line 9
```

