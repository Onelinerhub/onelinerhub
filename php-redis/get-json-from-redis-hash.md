# Get JSON from Redis hash

### If our JSON is stored as a hash:

```php
$redis->hgetall('json');
```

- `$redis` - Redis object after [connection](/php-redis/how-to-connect-to-redis)
- `hgetall` - gets all key/values from hash
- `json` - name of the hash to get JSON from

group: json

## Example: 
```php
<?php

$r = new Redis(); 
$r->connect('127.0.0.1', 6379);

print_r($r->hgetall('json'));
```
```
Array
(
    [a] => 1
    [b] => 2
)

```

