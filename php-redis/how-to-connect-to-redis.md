# How to connect to Redis

```php
$r = new Redis(); 
$r->connect('127.0.0.1', 6379); 
```

- `new Redis()` - create Redis object
- `connect(` - connect to specified host and port
- `127.0.0.1` - Redis host IP
- `6379` - Redis port to connect to

group: connect

## Example: 
```php
<?php

$r = new Redis(); 
$r->connect('127.0.0.1', 6379); 
echo $r->ping();
```
```
1
```

