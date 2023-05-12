# How to redirect with Python Aiohttp?
// plain

Redirecting with Python Aiohttp is easy and straightforward. To redirect a request, you can use the `redirect()` method of the `aiohttp.web.Response` class. The `redirect()` method takes two arguments: the URL to redirect to and the status code to use for the redirect.

## Example code

```
from aiohttp import web

async def redirect_handler(request):
    return web.Response(status=302, headers={'location': 'http://example.com'})
```

## Output example

```
HTTP/1.1 302 Found
Location: http://example.com
```

## Code explanation

- `web.Response`: This is the class used to create a response object.
- `status=302`: This is the status code used for redirects.
- `headers={'location': 'http://example.com'}`: This is the header used to specify the URL to redirect to.

## Helpful links
- [Aiohttp Documentation](https://docs.aiohttp.org/en/stable/)
- [HTTP Status Codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)

group: aiohttp

onelinerhub: [How to redirect with Python Aiohttp?](https://onelinerhub.com/python-aiohttp/how-to-redirect-with-python-aiohttp)