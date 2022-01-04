# Delete key in Redis

```python
r = redis.Redis()
r.delete('test')
```

- `redis.Redis` - connect to Redis server
- `delete` - deletes specified key
- `test` - name of the key to remove

## Example: 
```python
import redis

r = redis.Redis()
r.delete('test')

print(r.get('test'))
```
```
None

```

