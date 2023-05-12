# How to create a websocket server using Python Aiohttp?
// plain

Creating a websocket server using Python Aiohttp is easy and straightforward.

```
import asyncio
from aiohttp import web

async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:
        if msg.type == web.WSMsgType.text:
            await ws.send_str(msg.data + '/answer')
        elif msg.type == web.WSMsgType.binary:
            await ws.send_bytes(msg.data)
        elif msg.type == web.WSMsgType.close:
            break

    return ws

app = web.Application()
app.add_routes([web.get('/', websocket_handler)])

web.run_app(app)
```

The code above creates a websocket server using Python Aiohttp. It creates a websocket handler which handles incoming websocket requests. It then adds a route to the application and runs the application.

The code consists of the following parts:

1. Importing the necessary modules: `import asyncio` and `from aiohttp import web`
2. Creating a websocket handler: `async def websocket_handler(request)`
3. Creating a websocket response: `ws = web.WebSocketResponse()`
4. Preparing the websocket response: `await ws.prepare(request)`
5. Handling incoming messages: `async for msg in ws`
6. Sending a response: `await ws.send_str(msg.data + '/answer')`
7. Creating an application: `app = web.Application()`
8. Adding a route to the application: `app.add_routes([web.get('/', websocket_handler)])`
9. Running the application: `web.run_app(app)`

## Helpful links

- [Aiohttp Documentation](https://docs.aiohttp.org/en/stable/)
- [Websockets Tutorial](https://realpython.com/python-websockets/)

group: aiohttp

onelinerhub: [How to create a websocket server using Python Aiohttp?](https://onelinerhub.com/python-aiohttp/how-to-create-a-websocket-server-using-python-aiohttp)