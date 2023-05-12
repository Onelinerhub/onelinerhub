# How to use Python Aiohttp and FastAPI?
// plain

Python Aiohttp and FastAPI are two popular web frameworks used for building asynchronous web applications.

```
import aiohttp
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://example.com') as resp:
            return await resp.text()
```

The example code above shows how to use both Aiohttp and FastAPI together. The code creates a FastAPI application and defines a route that uses Aiohttp to make a GET request to an external URL.

## Code explanation


1. `import aiohttp` - imports the Aiohttp library
2. `from fastapi import FastAPI` - imports the FastAPI library
3. `app = FastAPI()` - creates a FastAPI application
4. `@app.get("/")` - defines a route for the application
5. `async with aiohttp.ClientSession() as session` - creates an Aiohttp client session
6. `async with session.get('http://example.com') as resp` - makes a GET request to an external URL
7. `return await resp.text()` - returns the response text

The output of the example code is the response text from the external URL.

## Helpful links

- [Aiohttp Documentation](https://docs.aiohttp.org/en/stable/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)

group: aiohttp

onelinerhub: [How to use Python Aiohttp and FastAPI?](https://onelinerhub.com/python-aiohttp/how-to-use-python-aiohttp-and-fastapi)