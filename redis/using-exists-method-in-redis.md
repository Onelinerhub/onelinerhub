# Using exists method in Redis

```bash
redis-cli EXISTS test
```

- `redis-cli` - launch Redis CLI interface in interactive mode
- `EXISTS` - returns `1` if the specified key exists
- `test` - name of the key to check existence of

## Example: 
```bash
redis-cli EXISTS test1
redis-cli EXISTS test123
```
```
(integer) 1
(integer) 0
```

