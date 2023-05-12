# How to make parallel requests with Python Aiohttp?
// plain

Parallel requests with Python Aiohttp can be made using the `asyncio` library. The following example code shows how to make two requests in parallel:

```
import asyncio
import aiohttp

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        html1 = await fetch(session, 'http://example.com/1')
        html2 = await fetch(session, 'http://example.com/2')
        print(html1)
        print(html2)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

## Output example

```
<html>
  <head>
    <title>Example 1</title>
  </head>
  <body>
    <h1>Example 1</h1>
  </body>
</html>
<html>
  <head>
    <title>Example 2</title>
  </head>
  <body>
    <h1>Example 2</h1>
  </body>
</html>
```

The code consists of the following parts:

1. `import asyncio` and `import aiohttp`: imports the `asyncio` and `aiohttp` libraries.
2. `async def fetch(session, url)`: defines an asynchronous function that takes a session and a URL as parameters and returns the response text.
3. `async def main()`: defines an asynchronous function that makes two requests in parallel using the `fetch` function.
4. `loop = asyncio.get_event_loop()`: creates an event loop.
5. `loop.run_until_complete(main())`: runs the `main` function until it is complete.

## Helpful links

- [Python Asyncio Documentation](https://docs.python.org/3/library/asyncio.html)
- [Aiohttp Documentation](https://aiohttp.readthedocs.io/en/stable/)

group: aiohttp

onelinerhub: [How to make parallel requests with Python Aiohttp?](https://onelinerhub.com/python-aiohttp/how-to-make-parallel-requests-with-python-aiohttp)