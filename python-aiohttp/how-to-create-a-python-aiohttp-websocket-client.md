# How to create a Python aiohttp websocket client?
// plain

Creating a Python aiohttp websocket client is relatively straightforward. The following example code creates a websocket client that connects to a websocket server and prints out any messages it receives:

```
import asyncio
from aiohttp import web

async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:
        if msg.type == web.WSMsgType.TEXT:
            if msg.data == 'close':
                await ws.close()
            else:
                print('Received:', msg.data)
        elif msg.type == web.WSMsgType.ERROR:
            print('ws connection closed with exception %s' %
                  ws.exception())

    print('websocket connection closed')

    return ws
```

## Output example

```
Received: Hello
Received: World
websocket connection closed
```

The code consists of the following parts:

1. `import asyncio` and `from aiohttp import web`: imports the necessary libraries for the websocket client.
2. `async def websocket_handler(request):`: defines the websocket handler function.
3. `ws = web.WebSocketResponse()`: creates a websocket response object.
4. `await ws.prepare(request)`: prepares the websocket response object.
5. `async for msg in ws:`: starts an asynchronous loop to receive messages from the websocket server.
6. `if msg.type == web.WSMsgType.TEXT:`: checks if the message type is text.
7. `if msg.data == 'close':`: checks if the message data is 'close'.
8. `await ws.close()`: closes the websocket connection.
9. `else:`: prints out the message data.
10. `elif msg.type == web.WSMsgType.ERROR:`: checks if the message type is an error.
11. `print('ws connection closed with exception %s' % ws.exception())`: prints out the exception.
12. `print('websocket connection closed')`: prints out a message when the websocket connection is closed.
13. `return ws`: returns the websocket response object.

## Helpful links

- [aiohttp Documentation](https://docs.aiohttp.org/en/stable/)
- [Websockets with aiohttp](https://docs.aiohttp.org/en/stable/web_advanced.html#websockets)

group: aiohttp-client

onelinerhub: [How to create a Python aiohttp websocket client?](https://onelinerhub.com/python-aiohttp/how-to-create-a-python-aiohttp-websocket-client)