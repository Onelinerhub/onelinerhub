# How to set query parameters with Python Aiohttp?
// plain

Query parameters can be set with Python Aiohttp using the `params` argument of the `aiohttp.ClientSession.get()` method.

## Example code

```
import aiohttp

async with aiohttp.ClientSession() as session:
    params = {'key1': 'value1', 'key2': 'value2'}
    async with session.get('http://example.com', params=params) as resp:
        print(resp.status)
```

## Output example

```
200
```

## Code explanation


1. `import aiohttp` - imports the aiohttp library
2. `async with aiohttp.ClientSession() as session` - creates a client session
3. `params = {'key1': 'value1', 'key2': 'value2'}` - creates a dictionary of query parameters
4. `async with session.get('http://example.com', params=params) as resp` - sends a GET request to the specified URL with the query parameters
5. `print(resp.status)` - prints the response status code

## Helpful links

- [aiohttp Documentation](https://docs.aiohttp.org/en/stable/)

group: aiohttp

onelinerhub: [How to set query parameters with Python Aiohttp?](https://onelinerhub.com/python-aiohttp/how-to-set-query-parameters-with-python-aiohttp)