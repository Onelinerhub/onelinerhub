# Get all keys from Redis

```python
r = redis.Redis()
all_keys = r.keys('*')
```

- `redis.Redis` - connect to Redis server
- `r.keys('*')` - get all keys from Redis

group: keys

## Example: 
```python
import redis

r = redis.Redis()
print(r.keys('*'))
```
```
[b'test2', b'test']

```

