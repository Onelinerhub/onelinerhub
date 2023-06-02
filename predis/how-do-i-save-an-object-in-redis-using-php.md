# How do I save an object in Redis using PHP?
// plain

Using PHP, you can save an object in Redis by using the `set` command. The `set` command takes two parameters, the first being the key and the second being the value.

For example:
```
$redis->set('my_object', json_encode($object));
```
This will save the object as a json-encoded string in Redis.

## Code explanation

- `$redis`: an instance of Redis created using `Redis()`
- `set`: the command used to save the object in Redis
- `my_object`: the key used to save the object
- `json_encode`: the function used to encode the object as a json string
- `$object`: the object to be saved

## Helpful links
- [Redis Documentation: SET](https://redis.io/commands/set)
- [PHP Documentation: json_encode](https://www.php.net/manual/en/function.json-encode.php)

onelinerhub: [How do I save an object in Redis using PHP?](https://onelinerhub.com/predis/how-do-i-save-an-object-in-redis-using-php)