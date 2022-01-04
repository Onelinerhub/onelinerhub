# How to auto reconnect to Redis

### Since Redis client supports automatic reconnect and has it enabled by default, we should just use standard connection method:

```php
$r = new Redis();
$r->connect('127.0.0.1', 6379);
// work with $r even if server goes away and returns
```


group: connect

## Example: 
```php
<?php

$r = new Redis();
$r->connect('127.0.0.1', 6379);

$r->set('t1', 'hi');
sleep(10);  // restart Redis server while sleeping
echo $r->get('t1');
```
```
hi
```

