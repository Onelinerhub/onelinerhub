# Using Redis persistent (keepalive) connections

```php
$redis->pconnect('127.0.0.1', 6379); 
```

- `$redis` - Redis object after [connection](/php-redis/how-to-connect-to-redis)

group: connect

## Example: 
```php
<?php

$r = new Redis();
$r->pconnect('127.0.0.1', 6379); 

echo $p->
```

