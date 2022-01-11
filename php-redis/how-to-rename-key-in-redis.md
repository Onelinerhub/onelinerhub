# How to rename key in Redis

```php
$redis->rename('old', 'new');
```

- `$redis` - Redis object after [connection](/php-redis/how-to-connect-to-redis)
- `rename` - renames old key name to the new one
- `old` - current name of the key
- `new` - new name of the key

## Example: 
```php
<?php

$r = new Redis(); 
$r->connect('127.0.0.1', 6379);

$r->set('a', 123);
$r->rename('a', 'aa');

echo $r->get('aa');
```
```
123
```

