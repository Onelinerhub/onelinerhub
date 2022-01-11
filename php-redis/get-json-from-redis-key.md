# Get nested JSON from Redis key

### If our JSON is [stored as string]():

```php
$json = json_decode($redis->get('js'), 1);
```

- `$redis` - Redis object after [connection](/php-redis/how-to-connect-to-redis)
- `get` - get string key value
- `js` - name of the key with our [saved JSON string]()
- `json_decode` - decodes JSON string into associative array

group: json

## Example: 
```php
<?php

$r = new Redis(); 
$r->connect('127.0.0.1', 6379);

$r->set('js', json_encode(['name' => 'Donald', 'top' => [1, 2, 3]]));

print_r(json_decode($r->get('js'), 1));
```
```
Array
(
    [name] => Donald
    [top] => Array
        (
            [0] => 1
            [1] => 2
            [2] => 3
        )

)

```

