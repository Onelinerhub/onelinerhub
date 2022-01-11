# Using username and password to connect to Redis

```php
$r = new Redis();
$r->connect('127.0.0.1', 6379); 
$r->auth('user', 'pwd');
```

- `new Redis()` - create Redis object
- `connect(` - connect to specified host and port
- `auth(` - authenticate using specified password
- `'user', 'pwd'` - username and password used to authenticate

group: auth


