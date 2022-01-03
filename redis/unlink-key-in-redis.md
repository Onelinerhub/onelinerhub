# Unlink key in Redis

```bash
redis-cli UNLINK test
```

- `redis-cli` - launch Redis CLI interface in interactive mode
- `UNLINK` - remove specified key in a non-blocking way
- `test` - name of the key to remove

group: keys

## Example: 
```bash
redis-cli UNLINK test
```
```
(integer) 1
```

