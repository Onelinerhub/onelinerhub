# How to use Redis auth

### No need to use `AUTH` command directly, as you can authenticate using password in constructor:

```python
import redis
r = redis.Redis( host='localhost', port=6379, password='123')
```

- `import redis` - import Redis module
- `redis.Redis` - connect to Redis server
- `password='123'` - specify your password in this argument

group: connect


