# Example of eval in Redis

```bash
redis-cli EVAL "return redis.call('get', 'key1') * 2;" 0
```

- `redis-cli` - executes Redis command in bash
- `EVAL` - evaluates specified LUA code
- `redis.call('get', 'key1') * 2` - sample code that gets `key1` key value and multiplies it by `2`

## Example: 
```bash
redis-cli EVAL "return redis.call('get', 'key1') * 2;" 0
```
```
(integer) 246
```

