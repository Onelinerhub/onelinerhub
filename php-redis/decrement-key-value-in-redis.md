# Decrement key value in Redis

```php
$redis->decr('counter');
```

- `$redis` - Redis object after [connection](/php-redis/how-to-connect-to-redis)
- `incrdecr` - Decrements given key value
- `counter` - name of the key to increment

group: inc_dec

## Example: 
```php
<?php

$r = new Redis(); 
$r->connect('127.0.0.1', 6379);

$r->set('counter', 10);
$r->decr('counter');

echo $r->get('counter');
```
```
9
```

