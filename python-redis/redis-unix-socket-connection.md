# Redis unix socket connection

```python
import redis
r = redis.Redis(unix_socket_path='/var/run/redis.sock')
```

- `import redis` - import Redis module
- `redis.Redis` - connect to Redis server
- `/var/run/redis.sock` - path to [Redis unix socket](/redis/configure-redis-to-use-unix-socket) to connect to

group: connect

## Example: 
```python
import redis
r = redis.Redis(unix_socket_path='/var/run/redis.sock')
print(r.ping())
```
```
True
```

