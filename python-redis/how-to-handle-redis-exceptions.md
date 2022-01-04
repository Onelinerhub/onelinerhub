# How to handle Redis exceptions

```python
r = redis.Redis()

try:
  r.set('a', [1])
except redis.RedisError as re:
  print(re)
```

- `redis.Redis` - connect to Redis server
- `r.set('a', [1])` - do some wrong stuff with Redis
- `except redis.RedisError` - catch Redis error
- `print(re)` - print error message

## Example: 
```python
import redis
r = redis.Redis()

try:
  r.set('a', [1])
except redis.RedisError as re:
  print(re)
```
```
Invalid input of type: 'list'. Convert to a bytes, string, int or float first.
ok

```

