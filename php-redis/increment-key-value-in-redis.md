# Increment key value in Redis

```php
$redis->incr('counter');
```

- `$redis` - Redis object after [connection](/php-redis/how-to-connect-to-redis)
- `incr` - increments given key value
- `counter` - name of the key to increment

group: inc_dec

## Example: 
```php
<?php

$r = new Redis(); 
$r->connect('127.0.0.1', 6379);

$r->set('counter', 1);
$r->incr('counter');

echo $r->get('counter');
```
```
2
```

