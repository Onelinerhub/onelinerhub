# Get value from Redis key

```python
r = redis.Redis()
val = r.get('test')
```

- `redis.Redis` - connect to Redis server
- `r.get` - gets value by key from Redis
- `test` - key to get value from
- `val` - variable will store value obtained from Redis

group: values

## Example: 
```python
import redis
r = redis.Redis()

print(r.get('test'))
```
```
b'hi'
```

