# Redis ping example

```php
$redis->ping();
```

- `$redis` - Redis object after [connection](/php-redis/how-to-connect-to-redis)
- `ping()` - send `ping` command to Redis and returns `true` on successful reply from server

## Example: 
```php
<?php

$r = new Redis(); 
$r->connect('127.0.0.1', 6379); 
var_dump($r->ping());
```
```
bool(true)

```

