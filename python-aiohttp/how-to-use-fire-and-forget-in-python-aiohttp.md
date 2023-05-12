# How to use fire and forget in Python Aiohttp?
// plain

Fire and forget is a pattern used to send a request and forget about the response. It is useful when the response is not needed or when the response is expected to take a long time. In Python Aiohttp, this can be achieved by using the `ClientSession.post()` method.

## Example code

```python
import aiohttp

async def fire_and_forget(url):
    async with aiohttp.ClientSession() as session:
        await session.post(url)

asyncio.run(fire_and_forget('http://example.com'))
```

## Output example

```
None
```

## Code explanation


1. `import aiohttp`: This imports the aiohttp library, which is used to make asynchronous HTTP requests.
2. `async def fire_and_forget(url):`: This defines a function called `fire_and_forget` which takes a URL as an argument.
3. `async with aiohttp.ClientSession() as session:`: This creates an asynchronous client session, which is used to make the HTTP request.
4. `await session.post(url)`: This sends an asynchronous HTTP POST request to the given URL and does not wait for a response.

## Helpful links

- [aiohttp Documentation](https://docs.aiohttp.org/en/stable/)

group: aiohttp

onelinerhub: [How to use fire and forget in Python Aiohttp?](https://onelinerhub.com/python-aiohttp/how-to-use-fire-and-forget-in-python-aiohttp)