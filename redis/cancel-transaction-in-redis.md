# Cancel transaction in Redis

```bash
redis-cli
> MULTI
> INCR test
> DISCARD
```

- `redis-cli` - launch Redis CLI interface in interactive mode
- `MULTI` - start transaction
- `INCR test` - sample commands within transaction
- `DISCARD` - cancels all queued operation inside transaction

group: transaction

## Example: 
```bash
127.0.0.1:6379> MULTI
OK
127.0.0.1:6379> INCR test
QUEUED
127.0.0.1:6379> DISCARD
```
```
OK
```

