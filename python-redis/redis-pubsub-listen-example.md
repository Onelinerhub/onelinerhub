# Redis pubsub listen example

### This is messages listener that subscribes to specified channel and waits for messages infinitely:

```python
import redis

r = redis.Redis()

q = r.pubsub()
q.subscribe('test')

for m in q.listen():
  print(m)
```


group: pubsub

## Example: 
```python
import redis

r = redis.Redis()

q = r.pubsub()
# assume someone will publish something to this channel
q.subscribe('test')

for m in q.listen():
  print(m)
```
```
{'type': 'subscribe', 'pattern': None, 'channel': b'test', 'data': 1}
{'type': 'message', 'pattern': None, 'channel': b'test', 'data': b'hi'}
{'type': 'message', 'pattern': None, 'channel': b'test', 'data': b'hello'}
...
```

