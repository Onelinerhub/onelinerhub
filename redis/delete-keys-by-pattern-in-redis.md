# Delete keys by pattern in Redis

```bash
redis-cli KEYS "pattern" | xargs redis-cli DEL
```

- `redis-cli` - executes Redis command in bash
- `KEYS` - find keys using specified pattern
- `pattern` - patter to search keys based on
- `xargs` - will use output of the left command and pass it to the right comman
- `DEL` - deletes specified keys (will be passed from output of first comman)

group: delete_key

## Example: 
```bash
redis-cli KEYS "key*" | xargs redis-cli DEL
```
```
(integer) 3
```

