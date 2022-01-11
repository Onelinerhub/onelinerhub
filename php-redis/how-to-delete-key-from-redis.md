# How to delete a key

```php
$redis->delete('key');
```

- `$redis` - Redis object after [connection](/php-redis/how-to-connect-to-redis)
- `delete` - deletes specified key
- `key` - name of the key to delete

group: delete

## Example: 
```php
<?php

$r = new Redis(); 
$r->connect('127.0.0.1', 6379);

$r->set('a', 1);
var_dump($r->get('a'));

$r->delete('a');
var_dump($r->get('a'));
```
```
string(1) "1"
bool(false)

```

