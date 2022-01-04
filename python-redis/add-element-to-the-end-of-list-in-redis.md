# Add element to the end of list in Redis

```python
r = redis.Redis()
r.rpush('list', 'value')
```

- `redis.Redis` - connect to Redis server
- `rpush` - pushes specified element to the end of the list
- `list` - name of the list to add element to
- `value` - value of the new element to add to the list

group: lists

## Example: 
```python
import redis

r = redis.Redis()
r.rpush('listr', 1)
r.rpush('listr', 2)

print(r.lrange('listr', 0, -1))
```
```
[b'1', b'2']

```

