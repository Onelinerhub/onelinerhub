# Get JSON from Redis

```python
r = redis.Redis()
obj = json.loads(r.get('d2'))
```

- `redis.Redis` - connect to Redis server
- `'d2'` - name of the key to get our JSON from (assume [JSON string](/python-redis/save-json-to-redis) is stored there already)
- `json.loads` - converts JSON string to dict object
- `obj =` - variable will store resulting dict object

group: json

## Example: 
```python
import redis, json

obj = {'name': 'Donald', 'years': [4, 8, 12]}

r = redis.Redis()
r.set('d2', json.dumps(obj))

res = json.loads(r.get('d2'))
print(res)
```
```
{'name': 'Donald', 'years': [4, 8, 12]}

```

