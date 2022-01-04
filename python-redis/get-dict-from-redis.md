# Get dict from Redis

### We'll use [Redis hash structure](https://redis.io/topics/data-types-intro#redis-hashes) to save dicts:

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

