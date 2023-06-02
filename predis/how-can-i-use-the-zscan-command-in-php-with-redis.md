# How can I use the zscan command in PHP with Redis?
// plain

The `zscan` command in Redis can be used in PHP to iterate over elements in a sorted set. It returns a cursor which can be used to iterate over the elements in the sorted set.

## Example code

```
<?php
    // Connect to Redis
    $redis = new Redis();
    $redis->connect('127.0.0.1', 6379);

    // Get the first cursor
    $cursor = 0;
    $elements = $redis->zscan('sorted_set', $cursor);
    $cursor = $elements[0];

    // Iterate over the elements
    while ($cursor != 0) {
        $elements = $redis->zscan('sorted_set', $cursor);
        foreach ($elements[1] as $key => $value) {
            echo "$key => $value\n";
        }
        $cursor = $elements[0];
    }
?>
```
## Output example

```
element1 => 5
element2 => 9
element3 => 1
```

This code will connect to a Redis server, get the first cursor of the sorted set, and iterate over the elements of the sorted set using the `zscan` command. For each element, it will print out the key and value to the screen.

## Code explanation

1. Connect to Redis: `$redis = new Redis(); $redis->connect('127.0.0.1', 6379);`
2. Get first cursor: `$cursor = 0; $elements = $redis->zscan('sorted_set', $cursor); $cursor = $elements[0];`
3. Iterate over elements: `while ($cursor != 0) { ... }`
4. Print out key and value: `echo "$key => $value\n";`

## Helpful links
- [Redis ZSCAN Documentation](https://redis.io/commands/zscan)
- [PHP Redis Documentation](https://www.php.net/manual/en/book.redis.php)

onelinerhub: [How can I use the zscan command in PHP with Redis?](https://onelinerhub.com/predis/how-can-i-use-the-zscan-command-in-php-with-redis)