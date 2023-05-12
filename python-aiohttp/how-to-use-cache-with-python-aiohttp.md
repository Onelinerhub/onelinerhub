# How to use cache with Python Aiohttp?
// plain

Using cache with Python Aiohttp is easy and straightforward.

```
import aiohttp
from aiohttp_cache import Cache

cache = Cache(ttl=60)

async with aiohttp.ClientSession(cache=cache) as session:
    async with session.get('http://example.com') as response:
        print(await response.text())
```

The output of the above code will be the text content of the page http://example.com.

## Code explanation


1. `import aiohttp`: This imports the aiohttp library.
2. `from aiohttp_cache import Cache`: This imports the Cache class from the aiohttp_cache library.
3. `cache = Cache(ttl=60)`: This creates a Cache object with a time-to-live (ttl) of 60 seconds.
4. `async with aiohttp.ClientSession(cache=cache) as session`: This creates an aiohttp ClientSession object with the cache object created in the previous step.
5. `async with session.get('http://example.com') as response`: This makes a GET request to the URL http://example.com and stores the response in the response variable.
6. `print(await response.text())`: This prints the text content of the response.

## Helpful links

- [aiohttp Documentation](https://aiohttp.readthedocs.io/en/stable/)
- [aiohttp_cache Documentation](https://aiohttp-cache.readthedocs.io/en/stable/)

group: aiohttp

onelinerhub: [How to use cache with Python Aiohttp?](https://onelinerhub.com/python-aiohttp/how-to-use-cache-with-python-aiohttp)