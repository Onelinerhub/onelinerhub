# Redis scan example

```php
while( $it !== 0 ) {
  foreach ( $redis->scan($it, 't*') as $k) {
    # do something with $k
  }
}
```

- `while( $it !== 0 )` - we should call scan till returned iterator is not zero
- `$redis` - Redis object after [connection](/php-redis/how-to-connect-to-redis)
- `scan` - scans keys based on specified pattern and returns iterator
- `'t*'` - sample [pattern](https://redis.io/commands/KEYS) to search keys (in this case, all keys starting with `t`)
- `$it` - iterator object

group: keys

## Example: 
```php
<?php

$r = new Redis(); 
$r->connect('127.0.0.1', 6379); 

while( $it !== 0 ) {
  foreach ( $r->scan($it, 't*') as $k) {
    echo $k . "\n";
  }
}
```
```
top
test
t1
test2

```

