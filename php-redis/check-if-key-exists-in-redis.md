# Check if key exists in Redis

```php
$redis->exists('test');
```

- `$redis` - Redis object after [connection](/php-redis/how-to-connect-to-redis)
- `exists` - returns `true` if specified key exists in Redis
- `test` - name of the key to check existence of

## Example: 
```php
<?php

$r = new Redis(); 
$r->connect('127.0.0.1', 6379); 

if ( $r->exists('test') ) {
  echo 'Key exists!';
}
```
```
1
```

