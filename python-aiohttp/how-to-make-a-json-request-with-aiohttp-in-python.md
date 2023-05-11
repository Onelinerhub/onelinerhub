# How to make a JSON request with aiohttp in Python?
// plain

Making a JSON request with aiohttp in Python is easy and straightforward. Here is an example code block to make a JSON request:
```
import aiohttp

async with aiohttp.ClientSession() as session:
    async with session.get('https://example.com/api/endpoint') as resp:
        json_data = await resp.json()
```
The output of the code block above will be a JSON object.

## Code explanation

1. `import aiohttp` - imports the aiohttp library
2. `async with aiohttp.ClientSession() as session` - creates a client session
3. `async with session.get('https://example.com/api/endpoint') as resp` - makes a GET request to the specified endpoint
4. `json_data = await resp.json()` - stores the response as a JSON object

## Helpful links
- [aiohttp Documentation](https://docs.aiohttp.org/en/stable/)
- [Making a Request](https://docs.aiohttp.org/en/stable/client_quickstart.html#make-a-request)

group: aiohttp

onelinerhub: [How to make a JSON request with aiohttp in Python?](https://onelinerhub.com/python-aiohttp/how-to-make-a-json-request-with-aiohttp-in-python)