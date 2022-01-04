# Redis async await example

```python
import asyncio, aioredis

async def aset_val(r, key, val):
  r.set(key, val)
  await asyncio.sleep(1)

async def main():
  r = aioredis.Redis()
  
  t1 = asyncio.create_task(aset_val(r, 'a1', 1));
  await t1
  
  print(wait r.get('a1'))

asyncio.run(main())
```


group: async

## Example: 
```python
import asyncio, aioredis

async def aset_val(r, key, val):
  await r.set(key, val)
  await asyncio.sleep(1)

async def main():
  r = aioredis.Redis()
  
  t1 = asyncio.create_task(aset_val(r, 'a1', 1));
  t2 = asyncio.create_task(aset_val(r, 'a2', 2));
  t3 = asyncio.create_task(aset_val(r, 'a3', 3));
  
  await t1
  
  v = await r.get('a1')
  print(v)

asyncio.run(main())
```
```
b'1'

```

