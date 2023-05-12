# How to make async requests with Python Aiohttp?
// plain

Using Aiohttp, you can make asynchronous requests in Python. To do this, you need to create an `async` function and use the `aiohttp.ClientSession` object to make the request.

## Example code

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

## Output example

```
<!doctype html>
<!--[if lt IE 7]>   <html class="no-js ie6 lt-ie7 lt-ie8 lt-ie9">   <![endif]-->
<!--[if IE 7]>      <html class="no-js ie7 lt-ie8 lt-ie9">          <![endif]-->
<!--[if IE 8]>      <html class="no-js ie8 lt-ie9">                 <![endif]-->
<!--[if gt IE 8]><!--><html class="no-js" lang="en" dir="ltr">  <!--<![endif]-->

<head>
    ...
```

The code consists of the following parts:

1. `import aiohttp` - imports the aiohttp library.
2. `async def fetch(session, url)` - defines an asynchronous function that takes a session and a URL as parameters and returns the response text.
3. `async def main()` - defines an asynchronous function that creates a session and calls the `fetch` function.
4. `if __name__ == '__main__'` - checks if the script is being run directly and creates an event loop.
5. `loop.run_until_complete(main())` - runs the `main` function until it is complete.

## Helpful links

- [Aiohttp Documentation](https://aiohttp.readthedocs.io/en/stable/)
- [Asyncio Documentation](https://docs.python.org/3/library/asyncio.html)

group: aiohttp

onelinerhub: [How to make async requests with Python Aiohttp?](https://onelinerhub.com/python-aiohttp/how-to-make-async-requests-with-python-aiohttp)