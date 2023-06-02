# How do I use the hset array command in PHP with Redis?
// plain

The `hset` array command is used to set a field in a hash stored at a key in Redis. This command can be used in PHP with the [PHP Redis](https://github.com/phpredis/phpredis) extension.

## Example code

```
$redis = new Redis();
$redis->connect('127.0.0.1', 6379);
$redis->hset('mykey', 'field1', 'value1');
```

This will set the field `field1` in the hash stored at `mykey` to the value `value1`.

The code consists of the following parts:

1. Create a new instance of the Redis class.
2. Connect to the Redis server.
3. Use the `hset` command to set a field in the hash stored at `mykey` to `value1`.

## Helpful links

- [PHP Redis Documentation](https://github.com/phpredis/phpredis#hset)
- [Redis Documentation](https://redis.io/commands/hset)

onelinerhub: [How do I use the hset array command in PHP with Redis?](https://onelinerhub.com/predis/how-do-i-use-the-hset-array-command-in-php-with-redis)