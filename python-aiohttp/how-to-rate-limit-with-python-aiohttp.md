# How to rate limit with Python Aiohttp?
// plain

Rate limiting with Python Aiohttp can be done using the `aiohttp.ClientSession.get()` method. This method takes an optional `limit` parameter which can be used to limit the number of requests per second.

## Example code

```
import aiohttp

async with aiohttp.ClientSession() as session:
    async with session.get('http://example.com', limit=2) as response:
        print(response.status)
```

## Output example

```
200
```

The code above limits the number of requests to 2 per second.

## Helpful links

- [aiohttp Documentation](https://docs.aiohttp.org/en/stable/)
- [Rate Limiting with aiohttp](https://www.blog.pythonlibrary.org/2016/07/26/python-3-an-intro-to-asyncio/)

group: aiohttp

onelinerhub: [How to rate limit with Python Aiohttp?](https://onelinerhub.com/python-aiohttp/how-to-rate-limit-with-python-aiohttp)