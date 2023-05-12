# How to use Python Aiohttp with Asyncio?
// plain

Python Aiohttp with Asyncio can be used to create asynchronous web applications. To use Aiohttp with Asyncio, first import the necessary modules:

```
import asyncio
from aiohttp import web
```

Then, create a function that will be used as a handler for the web application:

```
async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)
```

The output of the above code will be "Hello, [name]".

Next, create an instance of the web application:

```
app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/{name}', handle)])
```

Finally, run the web application:

```
web.run_app(app)
```

The web application will now be running and can be accessed at http://localhost:8080.

## Code explanation


1. Importing modules: `import asyncio` and `from aiohttp import web`
2. Creating a handler function: `async def handle(request)`
3. Creating an instance of the web application: `app = web.Application()`
4. Adding routes to the web application: `app.add_routes([web.get('/', handle), web.get('/{name}', handle)])`
5. Running the web application: `web.run_app(app)`

## Helpful links

- [Aiohttp Documentation](https://docs.aiohttp.org/en/stable/)
- [Asyncio Documentation](https://docs.python.org/3/library/asyncio.html)

group: aiohttp

onelinerhub: [How to use Python Aiohttp with Asyncio?](https://onelinerhub.com/python-aiohttp/how-to-use-python-aiohttp-with-asyncio)