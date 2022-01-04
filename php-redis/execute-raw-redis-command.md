# Execute raw Redis command

```php
$redis->rawCommand('get', 'test');
```

- `$redis` - Redis object after [connection](/php-redis/how-to-connect-to-redis)
- `rawCommand` - execute specified [Redis command](https://redis.io/commands)
- `get` - gets value by key
- `test` - name of the key to get value from

## Example: 
```php
<?php

$r = new Redis();
$r->connect('127.0.0.1');

print( $r->rawCommand('get', 'test') );
```
```
1
```

