# Redis batch insert

### In order to batch insert many values into Redis we should use pipelines:

```python
r = redis.Redis()
pipe = r.pipeline()

for i in range(10):
  pipe.set('p' + str(i), i)
  
pipe.execute()
```

- `redis.Redis` - connect to Redis server
- `r.pipeline()` - create Redis pipeline to execute batch commands
- `for i in range(10):` - do something 10 times
- `pipe.set` - plan setting value by key later (at this point - we just insert this command to a pipeline, but don't execute it)
- `pipe.execute()` - execute all commands in pipeline (actually inserts everything to Redis we have added before)

## Example: 
```python
import redis

r = redis.Redis()
pipe = r.pipeline()

for i in range(10):
  pipe.set('p' + str(i), i)
  
pipe.execute()

print(r.get('p5'))
```
```
b'5'

```

