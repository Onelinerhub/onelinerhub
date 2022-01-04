# Get list (all elements) from Redis

```python
r = redis.Redis()
list = r.lrange('list', 0, -1) 
```

- `redis.Redis` - connect to Redis server
- `lrange` - get range of elements from list in Redis
- `list` - name of the list to get elements of
- `0, -1` - start from first element and end with the last one

group: lists

## Example: 
```python
import redis

r = redis.Redis()
list = r.lrange('list', 0, -1)
print(list)
```
```
[b'2', b'1']

```

