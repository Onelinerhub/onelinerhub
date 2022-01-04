# Async Redis client example

```python
import asyncio, aioredis

async def main():
  redis = aioredis.Redis()
  await redis.set('some', 'val1')
  value = await redis.get('some')
  print(value)

asyncio.run(main())
```

- `aioredis` - async client redis (see [how to install](/python-redis/install-redis-async-client))
- `aioredis.Redis()` - connect to Redis server
- `await redis.set` - wait for async Redis method call (setting value)
- `'some', 'val1'` - set `val1` value of `some` key
- `await redis.get('some')` - async get of key value from Redis (`some` key)
- `asyncio.run` - runs main procedure

group: async

## Example: 
```python
import asyncio, aioredis

async def main():
  redis = aioredis.Redis()
  await redis.set('some', 'val1')
  value = await redis.get('some')
  print(value)

asyncio.run(main())
```
```
b'val1'

```

