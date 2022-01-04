# How to use boolean values in Redis

### Since Redis can't store native bool values, we're going to use integers (`1` is `True` and `0` is `False`) for that:

```python
bool = True

r = redis.Redis()
r.set('bool', int(bool))

result = int(r.get('bool')) == 1
```

- `bool = True` - variable with some boolean value
- `redis.Redis` - connect to Redis server
- `r.set` - sets value by key in Redis
- `int(bool)` - converts our boolean value to `1` or `0`
- `r.get` - gets value by key from Redis
- `int(r.get('bool')) == 1` - if int value from Redis equals `1` then we've saved `True` (otherwise, `False`)

## Example: 
```python
import redis

bool = True

r = redis.Redis()
r.set('bool', int(bool))

result = int(r.get('bool')) == 1

print(result)
```
```
True

```

