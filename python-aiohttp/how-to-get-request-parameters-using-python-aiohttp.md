# How to get request parameters using Python Aiohttp?
// plain

Request parameters can be obtained using Python Aiohttp by using the `request.query` method. This method returns a `MultiDictProxy` object which contains all the query parameters.

## Example code

```
from aiohttp import web

async def handler(request):
    params = request.query
    return web.Response(text="Query parameters: {}".format(params))
```

## Output example

```
Query parameters: MultiDictProxy({'param1': 'value1', 'param2': 'value2'})
```

## Code explanation

- `request.query`: This method returns a `MultiDictProxy` object which contains all the query parameters.
- `MultiDictProxy`: This is a dictionary-like object which contains all the query parameters.
- `params`: This is a variable which stores the `MultiDictProxy` object.
- `web.Response`: This is used to return the response to the client.

## Helpful links
- [Aiohttp Documentation](https://docs.aiohttp.org/en/stable/)
- [MultiDictProxy Documentation](https://multidict.readthedocs.io/en/stable/multidict.html#multidict.MultiDictProxy)

group: aiohttp

onelinerhub: [How to get request parameters using Python Aiohttp?](https://onelinerhub.com/python-aiohttp/how-to-get-request-parameters-using-python-aiohttp)