# How can I list keys in Redis using PHP?
// plain

The easiest way to list keys in Redis using PHP is by using the `SCAN` command.

```php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
$it = NULL;
$keys = array();
while($arr_keys = $redis->scan($it)) {
    foreach($arr_keys as $str_key) {
        $keys[] = $str_key;
    }
}

print_r($keys);
```

## Output example

```
Array
(
    [0] => key1
    [1] => key2
    [2] => key3
    [3] => key4
    [4] => key5
)
```

The code above will connect to the local Redis server, then loop through the keys using the `scan` command. The `$it` variable is used to keep track of the iteration. The `$arr_keys` variable will hold the keys returned from the `scan` command and then they are added to the `$keys` array. Finally, the `$keys` array is printed using `print_r`.

Parts of the code:

- `$redis = new Redis();`: Creates a new Redis instance.
- `$redis->connect('127.0.0.1', 6379);`: Connects to the local Redis server.
- `$it = NULL;`: Initializes the `$it` variable.
- `$keys = array();`: Initializes the `$keys` array.
- `while($arr_keys = $redis->scan($it)) {`: Loops through the keys using the `scan` command.
- `foreach($arr_keys as $str_key) {`: Loops through the array of keys returned from `scan`.
- `$keys[] = $str_key;`: Adds each key to the `$keys` array.
- `print_r($keys);`: Prints the `$keys` array.

## Helpful links

- [Redis SCAN Command](https://redis.io/commands/scan)
- [PHP Redis Documentation](https://www.php.net/manual/en/book.redis.php)

onelinerhub: [How can I list keys in Redis using PHP?](https://onelinerhub.com/predis/how-can-i-list-keys-in-redis-using-php)