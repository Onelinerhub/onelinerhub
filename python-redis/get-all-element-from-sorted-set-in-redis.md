# Get all element from sorted set in Redis

```python
r = redis.Redis()
list = r.zrange('top', 0, -1)
```

- `redis.Redis` - connect to Redis server
- `zrange` - retrieves sorted set elements based on offset and limit
- `top` - name of sorted set in Redis
- `0, -1` - will return all elements from sorted set

group: sorted_sets

## Example: 
```python
import redis

r = redis.Redis()

r.zadd('top', {'Donald': 2})
r.zadd('top', {'Joe': 1})

print(r.zrange('top', 0, -1))
```
```
[b'Joe', b'Donald']

```

