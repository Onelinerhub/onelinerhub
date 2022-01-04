# Save list to Redis

```python
r = redis.Redis()

list = [1, 2, 3]
r.rpush('lst', *list)
```

- `redis.Redis` - connect to Redis server
- `list` - sample list to save to Redis
- `rpush` - push new element to the right side of the list
- `lst` - name of the Redis key to save our local list to 
- `*list` - will pass all list elements to the `rpush` method

group: lists

## Example: 
```python
import redis

list = [1, 2, 3]

r = redis.Redis()
r.delete('l1')
r.rpush('l1', *list)

print(r.lrange('l1', 0, -1))
```
```
[b'1', b'2', b'3']

```

