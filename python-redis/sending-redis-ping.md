# Sending Redis ping

```python
r = redis.Redis()
r.ping()
```

- `redis.Redis` - connect to Redis server
- `r.ping()` - pings Redis server (will return `True` on success)

## Example: 
```python
import redis

r = redis.Redis()
print(r.ping())
```
```
True

```

