# Iterate through Redis keys

```python
r = redis.Redis()

for k in r.scan_iter('*'):
  r.get(k)
```

- `redis.Redis` - connect to Redis server
- `r.scan_iter` - returns iterator with all keys matching specified pattern
- `'*'` - [pattern](https://redis.io/commands/KEYS) to search for keys (all keys in our case)
- `r.get` - gets value by key from Redis (just random example of something to do with the key)

## Example: 
```python
import redis

r = redis.Redis()

for k in r.scan_iter("*"):
  print(k, ': ', r.get(k))
```
```
b'a' :  b'1'
b'bool' :  b'1'
b'd1' :  b'{"name": "Donald", "family": {"wife": "Melany"}}'
b'test' :  b'1'
b'c' :  b'3'
b'counter1' :  b'5'

```

