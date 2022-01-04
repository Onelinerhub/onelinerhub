# Add element to the list in Redis

```python
r = redis.Redis()
r.lpush('list', 'value')
```

- `redis.Redis` - connect to Redis server
- `lpush` - pushes specified element to the beginning of the list
- `list` - name of the list to add element to
- `value` - value of the new element to add to the list

group: lists

## Example: 
```python
import redis

r = redis.Redis()
r.lpush('list', 2)

print(r.lrange('list', 0, -1))
```
```
[b'2', b'1']

```

