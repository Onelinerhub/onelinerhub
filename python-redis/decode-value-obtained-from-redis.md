# Decode bytes obtained from Redis to string

```python
r = redis.Redis()
val = r.get('test').decode('utf-8')
```

- `redis.Redis` - connect to Redis server
- `r.get` - gets value by key from Redis
- `test` - key to get value from
- `decode('utf-8')` - decodes bytes into string (using `utf-8` charset in our case)

group: values

## Example: 
```python
import redis
r = redis.Redis()
val = r.get('test').decode('utf-8')

print(val)
```
```
hi

```

