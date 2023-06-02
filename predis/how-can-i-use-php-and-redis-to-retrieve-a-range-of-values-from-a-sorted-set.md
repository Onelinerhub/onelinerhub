# How can I use PHP and Redis to retrieve a range of values from a sorted set?
// plain

PHP and Redis can be used together to retrieve a range of values from a sorted set. The following example code can be used to demonstrate this:
```
<?php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
$values = $redis->zRange('mySortedSet', 0, -1);
print_r($values);
```
This code will output an array of the values from the sorted set:
```
Array
(
    [0] => value1
    [1] => value2
    [2] => value3
)
```
The code consists of the following parts:

1. Establish a connection to the Redis server:
   ```$redis = new Redis();
   $redis->connect('127.0.0.1', 6379);```

2. Retrieve a range of values from the sorted set:
   ```$values = $redis->zRange('mySortedSet', 0, -1);```

3. Output the values:
   ```print_r($values);```

For more information on using PHP and Redis together, see the [PHP Redis documentation](https://redis.io/clients/php).

onelinerhub: [How can I use PHP and Redis to retrieve a range of values from a sorted set?](https://onelinerhub.com/predis/how-can-i-use-php-and-redis-to-retrieve-a-range-of-values-from-a-sorted-set)