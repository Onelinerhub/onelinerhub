# How to use HTTP2 with Python Aiohttp?
// plain

HTTP2 can be used with Python Aiohttp by using the `http2` parameter in the `ClientSession` constructor.

```python
import aiohttp

async with aiohttp.ClientSession(http2=True) as session:
    async with session.get('https://example.com') as response:
        print(response.status)
```

The output of the above code will be `200`.

## Code explanation


1. `import aiohttp`: This imports the aiohttp library.
2. `async with aiohttp.ClientSession(http2=True) as session`: This creates a ClientSession object with http2 enabled.
3. `async with session.get('https://example.com') as response`: This makes a GET request to the specified URL.
4. `print(response.status)`: This prints the response status code.

## Helpful links

- [Aiohttp Documentation](https://docs.aiohttp.org/en/stable/)
- [HTTP2 Documentation](https://http2.github.io/)

group: aiohttp

onelinerhub: [How to use HTTP2 with Python Aiohttp?](https://onelinerhub.com/python-aiohttp/how-to-use-http2-with-python-aiohttp)