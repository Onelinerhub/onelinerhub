# Get key TTL in Redis

```python
r = redis.Redis()
seconds = r.ttl('a')
```

- `redis.Redis` - connect to Redis server
- `r.ttl(` - returns number of seconds left for a key to live
- `'a'` - key to get TTL for
- `seconds` - variable will store seconds to live

group: ttl

## Example: 
```python
import redis, time
r = redis.Redis()

r.set('a', '1')
r.expire('a', 5) # will expire in 5 sec
time.sleep(2) # wait for 2 sec

seconds = r.ttl('a')
print(seconds)
```
```
3

```

