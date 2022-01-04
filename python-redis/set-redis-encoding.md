# Set Redis encoding

```python
r = redis.StrictRedis('localhost', 6379, charset="utf-8", decode_responses=True)
str = r.get('test')
```

- `redis.StrictRedis` - connect to Redis server
- `utf-8` - chosen charset to automatically decode bytes
- `decode_responses` - will automatically decode bytes to strings using specified charset
- `str` - will contain utf-8 string automatically decoded from Redis bytes

## Example: 
```python
import redis
r = redis.StrictRedis('localhost', 6379, charset="utf-8", decode_responses=True)
str = r.get('test')

print(str)
```
```
hi

```

