# Redis hash usage example

```php
$redis->hset('h1', 'name', 'Donald');
$redis->hset('h1', 'age', '120');

$redis->hgetall('h1');
```


## Example: 
```php
<?php

$r = new Redis(); 
$r->connect('127.0.0.1', 6379);

$r->hset('h1', 'name', 'Donald');
$r->hset('h1', 'age', '120');

print_r($r->hgetall('h1'));
```
```
Array
(
    [name] => Donald
    [age] => 120
)

```

