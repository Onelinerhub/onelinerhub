# Check Redis connection

```php
$r = new Redis(); 
$r->connect('127.0.0.1', 6379); 
if ( $r->ping() ) {
  echo 'Connection is ok';
}
```

- `new Redis()` - create Redis object
- `connect(` - connect to specified host and port
- `ping()` - send `ping` command to Redis and returns `true` on successful reply from server

group: connect

## Example: 
```php
<?php

$r = new Redis(); 
$r->connect('127.0.0.1', 6379); 
if ( $r->ping() ) {
  echo 'Connection is ok';
}
```
```
Connection is ok
```

