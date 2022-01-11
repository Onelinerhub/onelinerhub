# Redis getset example

```php
$previous = $redis->getset('a', 25);
```

- `$redis` - Redis object after [connection](/php-redis/how-to-connect-to-redis)
- `$previous` - will be set to previous value of `a` key
- `getset` - returns current key value and sets new value after that
- `'a'` - name of the key to getset
- `25` - new value to set

## Example: 
```php
<?php

$r = new Redis(); 
$r->connect('127.0.0.1', 6379);

$r->set('a', 5);
echo $r->getset('a', 25);

echo "\n";
echo $r->get('a');
```
```
5
25
```

