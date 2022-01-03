# Using transactions in Redis

```bash
redis-cli
> MULTI
> INCR test
> INCR test
> EXEC
```

- `redis-cli` - launch Redis CLI interface in interactive mode
- `MULTI` - start transaction
- `INCR test` - sample commands within transaction
- `EXEC` - commit transaction

## Example: 
```bash
127.0.0.1:6379> MULTI
OK
127.0.0.1:6379> INCR test
QUEUED
127.0.0.1:6379> INCR test
QUEUED
127.0.0.1:6379> EXEC
```
```
1) (integer) 124
2) (integer) 125
```

