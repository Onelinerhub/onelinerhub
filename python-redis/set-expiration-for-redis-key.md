# Set expiration (TTL) for Redis key

### TTL

```python
r = redis.Redis()
r.expire('a', 60)
```

- `redis.Redis` - connect to Redis server
- `expire` - sets key expiration in seconds (from now)
- `'a'` - key to set expiration for
- `60` - number of seconds that key will expire in

group: ttl

## Example: 
```python
import redis, time
r = redis.Redis()

r.set('a', '1')
r.expire('a', 5) # will expire in 5 sec

print(r.get('a')) # make sure it has some value

time.sleep(5) # wait for 5 sec

print(r.get('a')) # now it's empty
```
```
b'1'
None

```

