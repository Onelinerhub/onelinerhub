# Delete keys by pattern in Redis

```bash
redis-cli KEYS "pattern"
```

- `redis-cli` - executes Redis command in bash
- `KEYS` - find keys using specified pattern
- `pattern` - patter to search keys based on

## Example: 
```bash
redis-cli KEYS "key*" | xargs redis-cli DEL
```
```
(integer) 3
```

