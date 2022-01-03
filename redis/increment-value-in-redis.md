# Increment value in Redis

```bash
redis-cli INCR test
```

- `redis-cli` - launch Redis CLI interface in interactive mode
- `INCR` - will increment specified key by `1`
- `test` - key to increment

## Example: 
```bash
redis-cli INCR test
```
```
(integer) 3
```

