# Increment key value in Redis

```python
r = redis.Redis()
r.incr('counter1')
```

- `redis.Redis` - connect to Redis server
- `incr` - increments given key value (or sets it to `1` if key didn't exist)

group: values

## Example: 
```python
import redis

r = redis.Redis()
r.incr('counter1')

print(r.get('counter1'))
```
```
b'5'

```

