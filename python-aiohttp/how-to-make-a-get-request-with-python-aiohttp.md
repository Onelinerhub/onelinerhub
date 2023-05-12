# How to make a GET request with Python Aiohttp?
// plain

Making a GET request with Python Aiohttp is easy and straightforward.

```
import aiohttp

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'http://python.org')
        print(html)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
```

The output of the example code will be the HTML content of the page http://python.org.

## Code explanation


1. `import aiohttp` - imports the aiohttp library
2. `async def fetch(session, url)` - defines an asynchronous function to make a GET request
3. `async with session.get(url) as response` - makes a GET request to the specified URL
4. `return await response.text()` - returns the response as text
5. `async with aiohttp.ClientSession() as session` - creates a client session
6. `html = await fetch(session, 'http://python.org')` - calls the fetch function to make a GET request
7. `print(html)` - prints the response
8. `loop = asyncio.get_event_loop()` - creates an event loop
9. `loop.run_until_complete(main())` - runs the main function until it is complete

## Helpful links

- [Aiohttp Documentation](https://aiohttp.readthedocs.io/en/stable/)
- [Python Asyncio Documentation](https://docs.python.org/3/library/asyncio.html)

group: aiohttp

onelinerhub: [How to make a GET request with Python Aiohttp?](https://onelinerhub.com/python-aiohttp/how-to-make-a-get-request-with-python-aiohttp)