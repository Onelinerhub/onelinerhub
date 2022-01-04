# Redis pubsub listen example

### This is messages listener that subscribes to specified channel and waits for messages infinitely:

```python
r = redis.Redis()

q = r.pubsub()
q.subscribe('test')

for m in q.listen():
  print(m)
```

- `redis.Redis` - connect to Redis server
- `r.pubsub()` - creates pubsub instance
- `subscribe` - subscribe to specified channel
- `'test'` - name of the channel to subscribe to
- `q.listen` - will iterate through messages and wait for new 

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

