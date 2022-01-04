# Save nested dict to Redis

### We'll use JSON encoding and decoding to store and read nested dicts:

```python
dict = {'name': 'Donald', 'family': {'wife': 'Melany'}}

r = redis.Redis()
r.set('nd', json.dumps(dict))
```

- `dict = ` - sample nested dict to save to Redis
- `redis.Redis` - connect to Redis server
- `r.set` - sets value by key in Redis
- `'nd'` - name of the Redis key to save our dict to
- `json.dumps(dict)` - converts dict to JSON string

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

