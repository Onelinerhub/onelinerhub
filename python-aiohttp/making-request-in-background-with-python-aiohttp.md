# Making request in background with Python Aiohttp?
// plain

Making requests in background with Python Aiohttp is a great way to make asynchronous requests. It allows you to make multiple requests at once, without having to wait for each one to finish before making the next.

## Example code

```
import aiohttp

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'http://example.com')
        print(html)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
```

## Output example

```
<html>
    <head>
        <title>Example Domain</title>
    </head>
    <body>
        <h1>Example Domain</h1>
        <p>This domain is established to be used for illustrative examples in documents. You may use this
        domain in examples without prior coordination or asking for permission.</p>
    </body>
</html>
```

## Code explanation


1. `import aiohttp`: This imports the aiohttp library, which is used to make asynchronous requests.

2. `async def fetch(session, url):`: This defines a function that takes a session and a URL as parameters. It then makes an asynchronous request to the URL and returns the response text.

3. `async def main():`: This defines a function that is used to make the actual requests. It creates a ClientSession object, which is used to make the requests, and then calls the fetch function to make the requests.

4. `if __name__ == '__main__':`: This is used to check if the code is being run directly, and if so, it creates an event loop and runs the main function.

## Helpful links

- [Aiohttp Documentation](https://aiohttp.readthedocs.io/en/stable/)
- [Python Asyncio Documentation](https://docs.python.org/3/library/asyncio.html)

group: aiohttp

onelinerhub: [Making request in background with Python Aiohttp?](https://onelinerhub.com/python-aiohttp/making-request-in-background-with-python-aiohttp)