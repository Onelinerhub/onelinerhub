# Get key TTL in Redis

```bash
redis-cli TTL test
```

- `redis-cli` - launch Redis CLI interface in interactive mode
- `TTL` - returns seconds left for the key to expire
- `test` - key name to get TTL for

group: keys

## Example: 
```bash
redis-cli TTL test
```
```
(integer) 295
```

