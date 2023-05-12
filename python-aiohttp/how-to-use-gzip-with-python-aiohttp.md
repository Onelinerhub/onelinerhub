# How to use Gzip with Python Aiohttp?
// plain

Gzip is a popular compression algorithm used to reduce the size of files. Python Aiohttp provides a convenient way to use Gzip with its `ClientSession` class.

```python
import aiohttp

async with aiohttp.ClientSession(headers={'Accept-Encoding': 'gzip'}) as session:
    async with session.get('http://example.com') as response:
        response_data = await response.read()
```

The above code will make a request to `http://example.com` with the `Accept-Encoding` header set to `gzip`. The response data will be compressed with Gzip and stored in the `response_data` variable.

## Code explanation


1. `import aiohttp` - imports the aiohttp library
2. `async with aiohttp.ClientSession(headers={'Accept-Encoding': 'gzip'}) as session` - creates a ClientSession object with the `Accept-Encoding` header set to `gzip`
3. `async with session.get('http://example.com') as response` - makes a request to `http://example.com`
4. `response_data = await response.read()` - reads the response data and stores it in the `response_data` variable

## Helpful links

- [aiohttp Documentation](https://docs.aiohttp.org/en/stable/)
- [Gzip Compression](https://en.wikipedia.org/wiki/Gzip)

group: aiohttp

onelinerhub: [How to use Gzip with Python Aiohttp?](https://onelinerhub.com/python-aiohttp/how-to-use-gzip-with-python-aiohttp)