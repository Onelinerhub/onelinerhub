# Clear all keys in Redis

```python
r = redis.Redis()
keys = r.keys('*')
r.delete(*keys)
```

- `redis.Redis` - connect to Redis server
- `r.keys('*')` - get all keys from Redis
- `r.delete(*keys)` - delete all specified keys (thus, all keys from Redis)

group: delete

## Example: 
```python
import redis

r = redis.Redis()
keys = r.keys('*')
r.delete(*keys)
print( r.keys('*') )
```
```
[]
```

