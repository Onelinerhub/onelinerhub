# Redis key watch example

### Pipelines use transactions by default, so we have to `watch()` our key from pipeline:

```python
r = redis.Redis()
val = r.get('some_counter')

p = r.pipeline()
p.watch('some_counter')
p.set('some_counter', val + 10)
p.execute()
```

- `redis.Redis` - connect to Redis server
- `r.get('some_counter')` - get value of some key from Redis (assume it has numeric value stored in it already)
- `r.pipeline()` - create Redis pipeline to execute batch commands
- `p.watch` - watch specified key within pipeline transaction
- `p.set` - set key value within pipeline
- `p.execute()` - execute pipeline

group: transactions

## Example: 
```python
import redis, time

r = redis.Redis()

val = r.get('some_counter')

p = r.pipeline()
p.watch('some_counter')
time.sleep(10)
p.set('some_counter', val + 10)
p.execute()
```
```
Traceback (most recent call last):
...
redis.exceptions.WatchError: Watched variable changed.

```

