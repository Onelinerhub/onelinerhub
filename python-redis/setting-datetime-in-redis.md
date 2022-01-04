# Setting datetime in Redis

### We're going to save timestamp (float) to Redis and then get it as a `float` and convert it to datetime object:

```python
import redis, time
from datetime import datetime

r = redis.Redis()

r.set('dt', time.time())
r.set_response_callback('GET', float)
result = datetime.fromtimestamp(r.get('dt'))
```

- `import redis` - import Redis module
- `set_response_callback` - automatically convert objects from Redis
- `float` - convert object to float
- `datetime.fromtimestamp` - convert timestamp to datetime
- `result` - variable will contain resulting datetime object

## Example: 
```python
import redis, time
from datetime import datetime

r = redis.Redis()

r.set('dt', time.time())
r.set_response_callback('GET', float)
print(datetime.fromtimestamp(r.get('dt')))
```
```
2022-11-04 13:10:30.252984

```

