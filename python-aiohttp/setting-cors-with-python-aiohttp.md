# Setting CORS with Python Aiohttp?
// plain

Python Aiohttp supports setting CORS (Cross-Origin Resource Sharing) headers. This allows web applications to access resources from other domains.

## Example code

```
from aiohttp import web

async def handle(request):
    response = web.Response()
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

app = web.Application()
app.router.add_get('/', handle)

web.run_app(app)
```

## Output example

```
======== Running on http://0.0.0.0:8080 ========
(Press CTRL+C to quit)
```

## Code explanation

- `from aiohttp import web`: imports the web module from the aiohttp library
- `response.headers['Access-Control-Allow-Origin'] = '*'`: sets the Access-Control-Allow-Origin header to allow requests from any domain
- `app.router.add_get('/', handle)`: adds a route to the application that will handle GET requests
- `web.run_app(app)`: starts the web application

## Helpful links
- [Aiohttp Documentation](https://docs.aiohttp.org/en/stable/)
- [MDN Web Docs - CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)

group: aiohttp

onelinerhub: [Setting CORS with Python Aiohttp?](https://onelinerhub.com/python-aiohttp/setting-cors-with-python-aiohttp)