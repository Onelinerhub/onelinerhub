# How to set a timeout for a Python aiohttp client?
// plain

The aiohttp library provides a convenient way to set a timeout for a client. To do this, you need to create a ClientSession object and pass the timeout parameter to it. The following example code sets a timeout of 10 seconds:

```
import aiohttp

async with aiohttp.ClientSession(timeout=10) as session:
    # Do something with the session
```

The timeout parameter is a float representing the number of seconds to wait for a response before timing out. If the timeout is reached, a `asyncio.TimeoutError` will be raised.

The timeout parameter can also be set when making a request. For example:

```
import aiohttp

async with aiohttp.ClientSession() as session:
    async with session.get('http://example.com', timeout=10) as response:
        # Do something with the response
```

In this example, the request will time out after 10 seconds if no response is received.

## Helpful links

- [aiohttp Documentation](https://docs.aiohttp.org/en/stable/)

group: aiohttp-client

onelinerhub: [How to set a timeout for a Python aiohttp client?](https://onelinerhub.com/python-aiohttp/how-to-set-a-timeout-for-a-python-aiohttp-client)