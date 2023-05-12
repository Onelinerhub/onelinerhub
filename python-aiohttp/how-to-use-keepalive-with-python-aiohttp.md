# How to use keepalive with Python Aiohttp?
// plain

Using keepalive with Python Aiohttp is easy. To enable keepalive, you need to set the `keepalive` parameter to `True` when creating the `ClientSession` object.

```python
import aiohttp

async with aiohttp.ClientSession(keepalive=True) as session:
    async with session.get('http://example.com') as response:
        print(response.status)
```

## Output example

```
200
```

The code above creates a `ClientSession` object with keepalive enabled, then makes a `GET` request to `http://example.com` and prints the response status.

The parts of the code are:

1. `import aiohttp` - imports the `aiohttp` module.
2. `async with aiohttp.ClientSession(keepalive=True) as session:` - creates a `ClientSession` object with keepalive enabled.
3. `async with session.get('http://example.com') as response:` - makes a `GET` request to `http://example.com`.
4. `print(response.status)` - prints the response status.

## Helpful links

- [aiohttp Documentation](https://aiohttp.readthedocs.io/en/stable/)
- [Keep-Alive and HTTP Connection Pooling](https://developer.mozilla.org/en-US/docs/Web/HTTP/Connection_management_in_HTTP)

group: aiohttp

onelinerhub: [How to use keepalive with Python Aiohttp?](https://onelinerhub.com/python-aiohttp/how-to-use-keepalive-with-python-aiohttp)