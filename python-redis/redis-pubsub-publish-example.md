# Redis pubsub publish example

### This is messages listener that subscribes to specified channel and waits for messages infinitely:

```python
r = redis.Redis()
r.publish('test', 'hi')
```

- `redis.Redis` - connect to Redis server
- `publish` - publish message to the specified channel
- `'test'` - name of the channel to publish message to
- `'hi'` - message to publish

group: pubsub


