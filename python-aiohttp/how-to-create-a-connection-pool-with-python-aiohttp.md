# How to create a connection pool with Python Aiohttp?
// plain

Creating a connection pool with Python Aiohttp is a simple process.

```
import aiohttp

async with aiohttp.ClientSession() as session:
    async with session.get('http://example.com') as resp:
        print(resp.status)
```

The output of the above code will be `200`.

## Code explanation


1. `import aiohttp`: This imports the aiohttp library which is used to create the connection pool.
2. `async with aiohttp.ClientSession() as session`: This creates a connection pool with the aiohttp library.
3. `async with session.get('http://example.com') as resp`: This creates a request to the specified URL.
4. `print(resp.status)`: This prints the status code of the response.

## Helpful links

- [Aiohttp Documentation](https://docs.aiohttp.org/en/stable/)
- [Python Aiohttp Tutorial](https://realpython.com/async-io-python/)

group: aiohttp

onelinerhub: [How to create a connection pool with Python Aiohttp?](https://onelinerhub.com/python-aiohttp/how-to-create-a-connection-pool-with-python-aiohttp)