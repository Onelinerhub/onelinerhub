# Increment key by value

```php
$redis->incr('counter', 5);
```

- `$redis` - Redis object after [connection](/php-redis/how-to-connect-to-redis)
- `incr` - increments given key by given value
- `counter` - name of the key to increment
- `5` - value to add to the given key

group: inc_dec

## Example: 
```php
<?php

$r = new Redis(); 
$r->connect('127.0.0.1', 6379);

$r->set('counter', 1);
$r->incr('counter', 5);

echo $r->get('counter');
```
```
6
```

