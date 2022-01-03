# Delete key in Redis

```bash
redis-cli DEL key
```

- `redis-cli` - executes Redis command in bash
- `DEL` - deletes selected key
- `key` - key name to delete

group: delete_key

## Example: 
```bash
redis-cli DEL a
```
```
(integer) 1
```

