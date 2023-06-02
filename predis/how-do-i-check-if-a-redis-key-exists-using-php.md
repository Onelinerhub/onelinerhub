# How do I check if a Redis key exists using PHP?
// plain

To check if a Redis key exists using PHP, you can use the `exists` method of the `Redis` class. This method takes the name of the key as an argument and returns a boolean value indicating whether the key exists or not.

## Example code

```
<?php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);

$key = 'mykey';

if ($redis->exists($key)) {
    echo "Key exists";
} else {
    echo "Key does not exist";
}
```

## Output example

```
Key does not exist
```

The code above does the following:
1. Creates a new Redis instance and connects to the Redis server.
2. Sets the variable `$key` to the name of the key we want to check.
3. Checks if the key exists using the `exists` method and prints out the result.

## Helpful links
- [Redis::exists](https://www.php.net/manual/en/redis.exists.php)

onelinerhub: [How do I check if a Redis key exists using PHP?](https://onelinerhub.com/predis/how-do-i-check-if-a-redis-key-exists-using-php)