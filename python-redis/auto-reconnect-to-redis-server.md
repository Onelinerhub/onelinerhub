# Auto reconnect to Redis server

### We're demonstrating an infinite loop which can meet situation of Redis server being unavailable:

```python
import redis
import time

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)

while True:
    try:
        r = redis.Redis(connection_pool=pool)
        print(r.ping())
    except Exception as e:
        print(e)

    time.sleep(1)
```

- `import redis` - import Redis module
- `redis.ConnectionPool` - creates Redis connection pool to be used later
- `redis.Redis` - connect to Redis server using connection pool (will automatically reconnect when server is available again)
- `r.ping()` - pings Redis server (will return `True` on success)
- `except Exception as e` - intercept and print error message so the script will not break 
- `time.sleep(1)` - wait for 1 second till next iteration

group: connect

## Example: 
```python
import redis
import time

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)

while True:
    try:
        r = redis.Redis(connection_pool=pool)
        print(r.ping())
    except Exception as e:
        print(e)

    time.sleep(1)
```
```
True
True
True
True
True
True
Error 111 connecting to localhost:6379. Connection refused.
True
True
...
```

