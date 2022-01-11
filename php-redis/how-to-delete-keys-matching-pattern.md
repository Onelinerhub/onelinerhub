# How to delete keys matching pattern

```php
$redis->delete($redis->keys('pref*'));
```

- `$redis` - Redis object after [connection](/php-redis/how-to-connect-to-redis)
- `delete` - deletes specified keys
- `keys` - returns keys that match selected pattern
- `'pref*'` - patter to match keys for deletion (in our case: keys starting with `pref...`)

group: delete

## Example: 
```php
<?php

$r = new Redis(); 
$r->connect('127.0.0.1', 6379);

$r->set('prefa', 1);
$r->set('prefb', 1);
print_r($r->keys('pref*'));

$r->delete($r->keys('pref*'));
print_r($r->keys('pref*'));
```
```
Array
(
    [0] => prefb
    [1] => prefa
)
Array
(
)

```

