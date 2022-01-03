# Usage of LUA scripts in Redis

```bash
redis-cli EVAL "return redis.call('get', KEYS[1]) + redis.call('get', KEYS[2]);" 2 key1 key2
```

- `redis-cli` - executes Redis command in bash
- `EVAL` - evaluates specified LUA code
- `redis.call` - call Redis method
- `'get'` - gets value by Redis key
- `KEYS[1]` - refers to first argument passed to `EVAL` command (`key1`)
- `KEYS[2]` - refers to second argument passed to `EVAL` command (`key2`)
- `2` - number of arguments we'll pass to the comman

group: eval

## Example: 
```bash
redis-cli EVAL "return redis.call('get', KEYS[1]) + redis.call('get', KEYS[2]);" 2 key1 key2
```
```
(integer) 138
```

