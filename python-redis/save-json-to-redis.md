# Save JSON to Redis

```python
import redis, json

obj = {'name': 'Donald', 'years': [4, 8, 12]}

r = redis.Redis()
r.set('d2', json.dumps(obj))
```

- `redis.Redis` - connect to Redis server
- `obj = ` - sample object to store as JSON
- `r.set` - sets value by key in Redis
- `'d2'` - name of the key to store our JSON
- `json.dumps(obj)` - converts `obj` object to JSON string

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

