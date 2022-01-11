# Redis simple example

```php
$r = new Redis(); 
$r->connect('127.0.0.1', 6379);

$r->set('my_key', 'hello');

$r->get('my_key');
```

- `new Redis()` - create Redis object
- `connect(` - connect to specified host and port
- `127.0.0.1` - Redis host IP
- `6379` - Redis port to connect to
- `set` - save string value to the specified Redis key
- `my_key` - name of the key
- `get` - get string key value

## Example: 
```php
<?php

$r = new Redis(); 
$r->connect('127.0.0.1', 6379); 

$r->set('my_key', 'hello');

echo $r->get('my_key');
```
```
hello
```

