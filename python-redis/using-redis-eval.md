# Using Redis eval

```python
r = redis.Redis()

val = r.eval("return redis.call('get', 'test')", 0)
```

- `redis.Redis` - connect to Redis server
- `eval` - executes Lua script
- `"return redis.call('get', 'test')"` - sample Lua script to execute (returns value of `test` key from Redis)
- `, 0)` - need to use this zero so Redis will not wait any additional data from us ("required shit")

## Example: 
```python
import redis

r = redis.Redis()

val = r.eval("return tonumber(redis.call('get', 'test'))", 0)
print(val)
```
```
1

```

