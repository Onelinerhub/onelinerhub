# Get all keys in Redis

```bash
redis-cli KEYS '*'
```

- `redis-cli` - launch Redis CLI interface in interactive mode
- `KEYS` - find keys using specified pattern
- `'*'` - will match all keys

group: find

## Example: 
```bash
redis-cli KEYS '*'
```
```
1) "test"
2) "key2"
3) "key1"
...
```

