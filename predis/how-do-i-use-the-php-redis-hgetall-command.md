# How do I use the PHP Redis hgetall command?
// plain

The `hgetall` command is used to retrieve all the fields and values from a hash stored at the given key in Redis. It returns an array of elements, where each element is an associative array with two items: the field name and its value.

For example, the following code will retrieve the data stored in the hash with key "user:1":

```php
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);

$data = $redis->hgetall('user:1');
```

The output of this code would be an array of elements, such as this:

```
Array
(
    [name] => John
    [age] => 30
    [city] => New York
)
```

This array can then be used to access the individual fields and values, such as `$data['name']` to get the name of the user.

Here is a list of the parts in the code:

1. `$redis = new Redis();` - Instantiates a new Redis object.
2. `$redis->connect('127.0.0.1', 6379);` - Connects to the Redis server.
3. `$data = $redis->hgetall('user:1');` - Retrieves the data stored in the hash with key "user:1".

For more information, please refer to the [PHP Redis documentation](https://redis.io/clients/php).

onelinerhub: [How do I use the PHP Redis hgetall command?](https://onelinerhub.com/predis/how-do-i-use-the-php-redis-hgetall-command)