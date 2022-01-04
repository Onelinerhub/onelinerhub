# Delete keys in Redis by pattern

```python
r = redis.Redis()
keys = r.keys('ke*')
r.delete(*keys)
```

- `redis.Redis` - connect to Redis server
- `r.keys` - get all keys from Redis that match specified pattern
- `r.delete(*keys)` - delete all specified keys (thus, all keys from Redis)
- `'ke*'` - pattern to obtain all keys starting with `ke`

group: delete

## Example: 
```python
import redis

r = redis.Redis()
keys = r.keys('ke*')
r.delete(*keys)
print( r.keys('ke*') )
```
```
[]

```

