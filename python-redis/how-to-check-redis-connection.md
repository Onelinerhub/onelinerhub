# How to check Redis connection

```python
import redis
r = redis.from_url('redis://localhost:6379')
print(r.ping())
```

- `import redis` - import Redis module
- `redis.from_url` - connect to Redis server using URI
- `r.ping()` - pings Redis server (will return `True` on success)

group: connect

## Example: 
```python
import redis
r = redis.from_url('redis://localhost:6379')
print(r.ping())
```
```
True
```

