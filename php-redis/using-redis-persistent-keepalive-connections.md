# Using Redis persistent (keepalive) connections

```php
$r = new Redis();
$r->pconnect('127.0.0.1', 6379); 
```

- `new Redis` - Redis object creation
- `pconnect` - setup persistent connection to Redis server

group: connect

## Example: 
```php
<?php

$r = new Redis();
$r->pconnect('127.0.0.1', 6379); 

echo $r->ping();
```
```
1
```

