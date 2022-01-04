# Redis transactions using multi and exec

### Pipelines use transactions by default, so we have to use pipelines for transactions instead of `MULTI` and `EXEC` methods:

```python
r = redis.Redis()

p = r.pipeline()
p.set('critical', 'val')
p.execute()
```

- `redis.Redis` - connect to Redis server
- `r.pipeline()` - create Redis pipeline to execute transaction
- `p.set` - sample `set` command inside transaction (pipeline)
- `p.execute()` - commits transaction (executes pipeline commands)

group: transactions

## Example: 
```python
import redis

r = redis.Redis()

p = r.pipeline()
p.set('critical', 'val')
p.execute()
```

