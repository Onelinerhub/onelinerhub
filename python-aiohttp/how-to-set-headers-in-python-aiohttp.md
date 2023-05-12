# How to set headers in Python Aiohttp?
// plain

Headers can be set in Python Aiohttp using the `add_headers` method. This method takes a dictionary of headers as an argument.

```
import aiohttp

headers = {
    'User-Agent': 'My User Agent 1.0',
    'From': 'youremail@domain.com'
}

async with aiohttp.ClientSession() as session:
    async with session.get('https://www.example.com', headers=headers) as resp:
        print(resp.status)
        print(resp.headers)

```

## Output example

```
200
{'Content-Type': 'text/html; charset=UTF-8', 'Content-Length': '1256', 'Connection': 'close', 'Date': 'Sun, 21 Jun 2020 11:45:45 GMT', 'Server': 'Apache', 'Last-Modified': 'Wed, 09 Jul 2003 23:32:50 GMT', 'ETag': '"3f80f-1b6-3e1cb03b"', 'Accept-Ranges': 'bytes', 'User-Agent': 'My User Agent 1.0', 'From': 'youremail@domain.com'}
```

## Code explanation


1. `import aiohttp` - imports the aiohttp library
2. `headers = {...}` - creates a dictionary of headers
3. `async with aiohttp.ClientSession() as session` - creates a client session
4. `async with session.get('https://www.example.com', headers=headers) as resp` - sends a GET request to the specified URL with the headers
5. `print(resp.status)` - prints the response status
6. `print(resp.headers)` - prints the response headers

## Helpful links

- [aiohttp Documentation](https://docs.aiohttp.org/en/stable/)
- [HTTP Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers)

group: aiohttp

onelinerhub: [How to set headers in Python Aiohttp?](https://onelinerhub.com/python-aiohttp/how-to-set-headers-in-python-aiohttp)