# Redis pipeline usage

```python
r = redis.Redis()

pipe = r.pipeline()

pipe.set('first', 'value')
pipe.set('second', 'value')

pipe.execute()
```

- `redis.Redis` - connect to Redis server
- `r.pipeline()` - create Redis pipeline to execute batch commands
- `pipe.set` - plan setting value by key later (at this point - we just insert this command to a pipeline, but don't execute it)
- `pipe.execute()` - execute all commands in pipeline (actually inserts everything to Redis we have added before)

## Example: 
```python
import redis

r = redis.Redis()

pipe = r.pipeline()

pipe.set('first', 'value')
pipe.set('second', 'value')

print(r.get('first'))
  
pipe.execute()

print(r.get('first'))
```
```
None
b'value'

```

