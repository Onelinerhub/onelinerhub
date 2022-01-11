# Set key value in Redis

```php
$redis->set('a', 'hi');
```

- `$redis` - Redis object after [connection](/php-redis/how-to-connect-to-redis)
- `set` - save string value to the specified Redis key
- `'a'` - name of the key to set value for
- `'hi'` - value to store

group: value

## Example: 
```php
<?php

$r = new Redis(); 
$r->connect('127.0.0.1', 6379);

$r->set('a', 'hi');

echo $r->get('a');
```
```
hi
```

