# Redis zadd example - adds element to sorted set

```python
r = redis.Redis()
r.zadd('top', {'Donald': 2})
```

- `redis.Redis` - connect to Redis server
- `zadd` - adds element(s) to the specified sorted set
- `Donald` - name of the element
- `2` - score of the element to add
- `top` - name of the sorted set in Redis to add element to

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

