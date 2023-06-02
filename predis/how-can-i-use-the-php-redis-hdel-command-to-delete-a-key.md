# How can I use the PHP Redis HDEL command to delete a key?
// plain

The PHP Redis HDEL command can be used to delete a key from a hash. To use the command, the key and the name of the hash must be provided.

For example:
```
$redis->hdel('myhash', 'mykey');
```
This will delete the key `mykey` from the hash `myhash`.

The parts of the command are:
- `$redis->hdel`: the HDEL command
- `'myhash'`: the name of the hash
- `'mykey'`: the key to delete

No output is returned when the command is successful.

## Helpful links
- [PHP Redis Documentation](https://github.com/phpredis/phpredis#hdel)

onelinerhub: [How can I use the PHP Redis HDEL command to delete a key?](https://onelinerhub.com/predis/how-can-i-use-the-php-redis-hdel-command-to-delete-a-key)