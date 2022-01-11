# Get key value from Redis

```php
$redis->get('a');
```

- `$redis` - Redis object after [connection](/php-redis/how-to-connect-to-redis)
- `get` - get string key value
- `'a'` - name of the key to get value from

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

