# Redis transactions using multi and exec

```php
$redis->multi()
->set('a', 1)
->get('a')
->set('b', 2)
->get('b')
->exec();
```

- `$redis` - Redis object after [connection](/php-redis/how-to-connect-to-redis)
- `multi` - execute set of commands within single transaction
- `exec` - commit transaction and return list of results of each executed command

## Example: 
```php
<?php

$r = new Redis(); 
$r->connect('127.0.0.1', 6379);

$res = $r->multi()
       ->set('a', 1)
       ->get('a')
       ->set('b', 2)
       ->get('b')
       ->exec();

var_dump($res);
```
```
array(4) {
  [0]=>
  bool(true)
  [1]=>
  string(1) "1"
  [2]=>
  bool(true)
  [3]=>
  string(1) "2"
}

```

