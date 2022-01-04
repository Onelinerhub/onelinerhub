# Save value to Redis key

```python
r = redis.Redis()
r.set('test', 'hi')
```

- `redis.Redis` - connect to Redis server
- `r.set` - sets value by key in Redis
- `test` - key to save value to
- `hi` - value to save

group: values

## Example: 
```python
import redis
r = redis.Redis()
r.set('test', 'hi')
print(r.get('test'))
```
```
b'hi'

```

