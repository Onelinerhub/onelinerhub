# Connecting to Redis with from_url()

```python
import redis
r = redis.from_url('redis://localhost:6379')
```

- `import redis` - import Redis module
- `redis.from_url` - connect to Redis server using URI
- `localhost` - host to connect to
- `6379` - port to connect to

group: connect

## Example: 
```python
import redis
r = redis.from_url('redis://localhost:6379')
print(r.ping())
```
```
True

```

