# Get Redis key size

```python
r = redis.Redis()
size = r.debug_object('test')['serializedlength']
```

- `redis.Redis` - connect to Redis server
- `debug_object` - return Redis system info on specified key
- `test` - key to get size of
- `serializedlength` - will return size of the value of specified key

group: keys

## Example: 
```python
import redis

r = redis.Redis()
size = r.debug_object('test')['serializedlength']

print(size)
```
```
2

```

