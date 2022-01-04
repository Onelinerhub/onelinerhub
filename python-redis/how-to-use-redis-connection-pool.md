# How to use Redis connection pool

```python
import redis
pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)
```

- `import redis` - import Redis module
- `redis.ConnectionPool` - creates Redis connection pool to be used later
- `connection_pool` - specify connection pool to use connection from

group: connect

## Example: 
```python
import redis
pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)
print(r.ping())
```
```
True

```

