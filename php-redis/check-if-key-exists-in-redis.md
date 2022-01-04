# Check if key exists in Redis

```php
$redis->exists('test');
```

- `$redis` - Redis object after [connection](/php-redis/how-to-connect-to-redis)

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

