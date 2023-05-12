# How to set request cookies with Python Aiohttp?
// plain

Python Aiohttp library provides a convenient way to set request cookies.

```
import aiohttp

async with aiohttp.ClientSession() as session:
    async with session.get('http://example.com', cookies={'name': 'value'}) as resp:
        print(resp.status)
```

## Output example

```
200
```

The code above sets a cookie with name `name` and value `value` in the request.

1. `import aiohttp` imports the aiohttp library.
2. `async with aiohttp.ClientSession() as session` creates a client session.
3. `async with session.get('http://example.com', cookies={'name': 'value'}) as resp` sends a GET request to `http://example.com` with the cookie `name` set to `value`.
4. `print(resp.status)` prints the response status code.

## Helpful links

- [aiohttp Documentation](https://docs.aiohttp.org/en/stable/)

group: aiohttp

onelinerhub: [How to set request cookies with Python Aiohttp?](https://onelinerhub.com/python-aiohttp/how-to-set-request-cookies-with-python-aiohttp)