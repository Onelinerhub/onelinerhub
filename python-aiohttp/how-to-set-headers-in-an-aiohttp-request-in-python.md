# How to set headers in an aiohttp request in Python?
// plain

To set headers in an aiohttp request in Python, you can use the `add_headers` method. This method takes a dictionary of headers as an argument. For example:

```
import aiohttp

async with aiohttp.ClientSession() as session:
    async with session.get('http://example.com', headers={'User-Agent': 'My custom user agent'}) as response:
        print(response.status)
```

## Output example

```
200
```

The code above sets the `User-Agent` header to `My custom user agent` and prints the response status code.

The code consists of the following parts:

1. `import aiohttp` - imports the aiohttp library
2. `async with aiohttp.ClientSession() as session` - creates a client session
3. `async with session.get('http://example.com', headers={'User-Agent': 'My custom user agent'}) as response` - sends a GET request to `http://example.com` with the `User-Agent` header set to `My custom user agent`
4. `print(response.status)` - prints the response status code

## Helpful links

- [aiohttp Documentation](https://docs.aiohttp.org/en/stable/)

group: aiohttp

onelinerhub: [How to set headers in an aiohttp request in Python?](https://onelinerhub.com/python-aiohttp/how-to-set-headers-in-an-aiohttp-request-in-python)