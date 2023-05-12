# How to reuse a session with Python Aiohttp?
// plain

Reusing a session with Python Aiohttp is easy and straightforward. You can use the `session.get()` method to make a request and reuse the same session for subsequent requests.

```python
import aiohttp

async with aiohttp.ClientSession() as session:
    async with session.get('http://example.com') as response:
        print(response.status)
    async with session.get('http://example.com/other') as response:
        print(response.status)
```

## Output example

```
200
200
```

The code above creates a session with `aiohttp.ClientSession()` and then uses the `session.get()` method to make two requests to the same URL. The session is reused for both requests, so the same cookies and other session data are sent with both requests.

## Code explanation


1. `aiohttp.ClientSession()`: creates a session object.
2. `session.get()`: makes a request and reuses the same session for subsequent requests.

## Helpful links

- [aiohttp Documentation](https://aiohttp.readthedocs.io/en/stable/)
- [Python Aiohttp Tutorial](https://realpython.com/async-io-python/)

group: aiohttp

onelinerhub: [How to reuse a session with Python Aiohttp?](https://onelinerhub.com/python-aiohttp/how-to-reuse-a-session-with-python-aiohttp)