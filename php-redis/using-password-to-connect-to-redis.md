# Using password to connect to Redis

```php
$r = new Redis();
$r->connect('127.0.0.1', 6379); 
$r->auth('pwd');
```

- `new Redis()` - create Redis object
- `connect(` - connect to specified host and port
- `auth(` - authenticate using specified password

group: connect


