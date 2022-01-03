# Key expire in Redis

```bash
redis-cli EXPIRE test 60
```

- `redis-cli` - launch Redis CLI interface in interactive mode
- `EXPIRE` - set expiration (in seconds) for the specified key
- `test` - name of the key to set expiration for
- `60` - amount of seconds to expire key after

## Example: 
```bash
redis-cli EXPIRE test 60
```
```
(integer) 1
```

