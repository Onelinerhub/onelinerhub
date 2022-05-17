# Search keys by pattern in Redis

```python
r = redis.Redis()
all_keys = r.keys('pattern')
```

- `redis.Redis` - connect to Redis server
- `r.keys` - get all keys from Redis that match specified pattern
- `pattern` - [pattern](https://redis.io/commands/KEYS) to use for key search

group: keys

## Example: 
```python
import redis

r = redis.Redis()
print(r.keys('test*'))
```
```
[b'test2', b'test']

```

## Additional keywords
- find
- get
- fetch
- retrieve

