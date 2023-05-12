# How to close a Python Aiohttp session?
// plain

Aiohttp sessions can be closed using the `close()` method. This method will close the underlying transport and all connections associated with the session.

```python
import aiohttp

async with aiohttp.ClientSession() as session:
    # Do something with the session
    await session.close()
```

The `close()` method will:

1. Close the underlying transport
2. Close all connections associated with the session

## Helpful links

- [aiohttp Documentation](https://docs.aiohttp.org/en/stable/)

group: aiohttp

onelinerhub: [How to close a Python Aiohttp session?](https://onelinerhub.com/python-aiohttp/how-to-close-a-python-aiohttp-session)