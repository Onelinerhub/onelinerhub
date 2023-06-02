# How do I use the PHP Redis mset command?
// plain

The `mset` command in PHP Redis is used to set multiple keys at once. It takes an array of key/value pairs as its argument.

## Example code

```
$redis->mset(array('key1' => 'value1', 'key2' => 'value2'));
```

This command will set the values `value1` and `value2` for the keys `key1` and `key2` respectively.

## Code explanation

1. `$redis`: The Redis instance.
2. `mset`: The `mset` command.
3. `array('key1' => 'value1', 'key2' => 'value2')`: Array of key/value pairs.

## Helpful links
- [PHP Redis Documentation](https://redis.io/clients/php)
- [MSET Command Documentation](https://redis.io/commands/mset)

onelinerhub: [How do I use the PHP Redis mset command?](https://onelinerhub.com/predis/how-do-i-use-the-php-redis-mset-command)