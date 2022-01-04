# Get dict from Redis

```python
r = redis.Redis()
dict = r.hgetall('dict')
```

- `redis.Redis` - connect to Redis server
- `hgetall` - gets Redis hash data and returns a dict
- `'dict'` - name of the hash in Redis

group: dict

## Example: 
```python
import redis

dict = {'name': 'Donald', 'age': 102}

r = redis.Redis()
r.hmset('d', dict)

print(r.hgetall('d'))
```
```
{b'name': b'Donald', b'age': b'102'}

```

