# Redis async await example

```python
import asyncio, aioredis

async def aset_val(r, key, val):
  await r.set(key, val)

async def main():
  r = aioredis.Redis()
  
  t1 = asyncio.create_task(aset_val(r, 'a1', 1));
  t1 = asyncio.create_task(aset_val(r, 'a2', 2));
  
  await t1, t2

asyncio.run(main())
```

- `import asyncio, aioredis` - import async Redis client and module for async execution
- `async def aset_val` - declare async method to set value in Redis
- `aioredis.Redis()` - connect async Redis client
- `asyncio.create_task` - creates async task to execute them asynchronously later
- `await t1, t2` - run both tasks concurrently

group: async

## Example: 
```python
import asyncio, aioredis

async def aset_val(r, key, val):
  await r.set(key, val)
  await asyncio.sleep(1) # delay for 1 second

async def main():
  r = aioredis.Redis()
  
  t1 = asyncio.create_task(aset_val(r, 'a1', 1));
  t2 = asyncio.create_task(aset_val(r, 'a2', 2));
  t3 = asyncio.create_task(aset_val(r, 'a3', 3));
  
  await t1, t2, t3 # will execute everything in 1 sec
  
  print(await r.mget('a1', 'a2', 'a3'))

asyncio.run(main())
```
```
[b'1', b'2', b'3']

```

