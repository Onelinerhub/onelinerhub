# Check if key exists in Redis

```python
r = redis.Redis()
does_exist = r.exists('test')
```

- `redis.Redis` - connect to Redis server
- `r.exists` - returns `1` if specified key exists, otherwise returns `0`
- `test` - name of the key to check existence of
- `does_exist` - variable will store `1` (or `0`) if the key exists (or not)

## Example: 
```python
import redis

r = redis.Redis()
if r.exists('test'):
  print('Key exists!')
```
```
Key exists!

```

