# Using retry_on_timeout in Redis

```python
r = redis.Redis(retry_on_timeout=True)
```

- `redis.Redis` - connect to Redis server
- `retry_on_timeout` - will ask python to retry commands once if timeout error occurs

## Example: 
```python
import redis

r = redis.Redis(retry_on_timeout=True)
print(r.get('test'))
```
```
b'1'

```

