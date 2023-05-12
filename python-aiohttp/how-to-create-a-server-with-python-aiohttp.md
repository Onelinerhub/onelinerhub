# How to create a server with Python Aiohttp?
// plain

Creating a server with Python Aiohttp is easy and straightforward.

```
from aiohttp import web

async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)

app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/{name}', handle)])

web.run_app(app)
```

This code will create a server that will respond to requests with a greeting.

1. `from aiohttp import web` imports the web module from the aiohttp library.
2. `async def handle(request):` defines a function that will handle requests.
3. `name = request.match_info.get('name', "Anonymous")` gets the name parameter from the request.
4. `text = "Hello, " + name` creates a greeting string.
5. `return web.Response(text=text)` returns the greeting string as a response.
6. `app = web.Application()` creates an application instance.
7. `app.add_routes([web.get('/', handle), web.get('/{name}', handle)])` adds routes to the application.
8. `web.run_app(app)` starts the server.

## Helpful links

- [Aiohttp Documentation](https://docs.aiohttp.org/en/stable/)
- [Python Aiohttp Tutorial](https://realpython.com/async-io-python/)

group: aiohttp

onelinerhub: [How to create a server with Python Aiohttp?](https://onelinerhub.com/python-aiohttp/how-to-create-a-server-with-python-aiohttp)