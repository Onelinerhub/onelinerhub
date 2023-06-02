# How do I use the php redis blpop command?
// plain

The `BLPOP` command is used to remove and get the first element in a list, blocking until one is available. It is part of the Redis `List` data structure.

Example usage:
```
$redis->blpop('list', 10);
```

This command will block for up to 10 seconds until an element is available. If an element is available, it will be removed from the list and returned.

## Code explanation

- `$redis`: The Redis instance.
- `blpop`: The command used to remove and get the first element in a list.
- `list`: The list from which to remove the element.
- `10`: The number of seconds to block until an element is available.

## Helpful links
- [Redis BLPOP Command](https://redis.io/commands/blpop)

onelinerhub: [How do I use the php redis blpop command?](https://onelinerhub.com/predis/how-do-i-use-the-php-redis-blpop-command)