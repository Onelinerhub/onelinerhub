# Save dict to Redis

### We'll use [Redis hash structure](https://redis.io/topics/data-types-intro#redis-hashes) to save dicts:

```python
dict = {'name': 'Donald', 'age': 102}

r = redis.Redis()
r.hmset('dict', dict)
```

- `dict = ` - sample dict to save to Redis
- `redis.Redis` - connect to Redis server
- `hmset` - saves specified dict to Redis hash
- `'dict'` - name of the Redis hash to save dict to

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

