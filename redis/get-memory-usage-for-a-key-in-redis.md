# Get memory usage for a key in Redis

```bash
redis-cli MEMORY USAGE test
```

- `redis-cli` - launch Redis CLI interface in interactive mode
- `MEMORY USAGE` - returns amount of bytes used for specified key
- `test` - name of the key to get memory usage for

group: mem

## Example: 
```bash
redis-cli MEMORY USAGE test1
```
```
(integer) 62
```

