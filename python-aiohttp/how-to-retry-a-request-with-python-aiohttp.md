# How to retry a request with Python Aiohttp?
// plain

Retrying a request with Python Aiohttp can be done using the `aiohttp.ClientSession.request` method. The `retry` parameter can be used to specify the number of times the request should be retried.

## Example code

```
import aiohttp

async with aiohttp.ClientSession() as session:
    async with session.request('GET', 'http://example.com', retry=3) as response:
        print(response.status)
```

## Output example

```
200
```

## Code explanation


1. `import aiohttp`: imports the aiohttp library.
2. `async with aiohttp.ClientSession() as session`: creates an asynchronous session object.
3. `async with session.request('GET', 'http://example.com', retry=3) as response`: sends a GET request to the specified URL with the `retry` parameter set to 3.
4. `print(response.status)`: prints the response status code.

## Helpful links

- [aiohttp Documentation](https://docs.aiohttp.org/en/stable/)

group: aiohttp

onelinerhub: [How to retry a request with Python Aiohttp?](https://onelinerhub.com/python-aiohttp/how-to-retry-a-request-with-python-aiohttp)