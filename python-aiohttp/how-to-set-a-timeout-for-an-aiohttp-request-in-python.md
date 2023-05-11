# How to set a timeout for an aiohttp request in Python?
// plain

Setting a timeout for an aiohttp request in Python can be done using the `timeout` parameter of the `ClientSession.get()` method.

## Example code

```
import aiohttp

async with aiohttp.ClientSession() as session:
    async with session.get('http://example.com', timeout=10) as response:
        print(response.status)
```

## Output example

```
200
```

## Code explanation


1. `import aiohttp`: imports the aiohttp library.
2. `async with aiohttp.ClientSession() as session`: creates a ClientSession object.
3. `async with session.get('http://example.com', timeout=10) as response`: sends a GET request to the specified URL with a timeout of 10 seconds.
4. `print(response.status)`: prints the response status code.

## Helpful links

- [aiohttp Documentation](https://docs.aiohttp.org/en/stable/)

group: aiohttp

onelinerhub: [How to set a timeout for an aiohttp request in Python?](https://onelinerhub.com/python-aiohttp/how-to-set-a-timeout-for-an-aiohttp-request-in-python)