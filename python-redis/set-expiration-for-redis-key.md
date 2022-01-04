# Set expiration for Redis key

```python
r = redis.Redis()
r.expire('a', 60)
```

- `redis.Redis` - connect to Redis server
- `expire` - sets key expiration in seconds (from now)
- `'a'` - key to set expiration for
- `60` - number of seconds that key will expire in

## Example: 
```python
import redis, time
r = redis.Redis()

r.set('a', '1')
r.expire('a', 5)
print(r.get('a'))

time.sleep(5)
print(r.get('a'))
```
```
b'1'
None

```

