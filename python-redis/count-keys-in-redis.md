# Count keys in Redis

```python
r = redis.Redis()
total_keys = r.dbsize()
```

- `redis.Redis` - connect to Redis server
- `r.dbsize` - return all keys count from current DB

## Example: 
```python
import redis

r = redis.Redis()
print(r.dbsize())
```
```
2

```

