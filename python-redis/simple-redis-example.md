# Simple Redis example

```python
import redis

r = redis.Redis()
r.set('k', 'hi')
print(r.get('k').decode('utf-8'))
```

- `import redis` - import Redis module
- `redis.Redis` - connect to Redis server
- `r.set` - sets value by key in Redis
- `'k'` - name of the key to set value
- `'hi'` - value we set for our key
- `r.get('k')` - get our key value from Redis
- `decode('utf-8')` - convert Redis bytes to utf-8 string

## Example: 
```python
import redis

r = redis.Redis()
r.set('k', 'hi')

print(r.get('k').decode('utf-8'))
```
```
hi

```

