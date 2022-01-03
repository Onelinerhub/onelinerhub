# Find keys by pattern in Redis

```bash
redis-cli KEYS pattern
```

- `redis-cli` - launch Redis CLI interface in interactive mode
- `KEYS` - find keys using specified pattern
- `pattern` - patter to search keys based on

## Example: 
```bash
redis-cli KEYS k*

```
```
1) "key2"
2) "key1"
```

