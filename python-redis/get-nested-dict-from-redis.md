# Get nested dict from Redis

### We'll use JSON encoding and decoding to store and read nested dicts:

```python
r = redis.Redis()
dict = json.loads(r.get('nd'))
```

- `redis.Redis` - connect to Redis server
- `r.get` - gets value by key from Redis
- `'nd'` - name of the Redis key to get our dict from
- `json.loads` - converts JSON string to dict object

group: dict_nested

## Example: 
```python
import redis, json

dict = {'name': 'Donald', 'family': {'wife': 'Melany'}}

r = redis.Redis()
r.set('d1', json.dumps(dict))

res = json.loads(r.get('d1'))
print(res)
```
```
{'name': 'Donald', 'family': {'wife': 'Melany'}, 'test': 1}

```

