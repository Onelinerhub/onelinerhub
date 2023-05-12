# How to get headers using Python Aiohttp?
// plain

Using Python Aiohttp, you can get headers from a web page by making a GET request.

```
import aiohttp

async with aiohttp.ClientSession() as session:
    async with session.get('https://www.example.com') as response:
        print(response.headers)
```

```
{'Content-Type': 'text/html; charset=UTF-8', 'Date': 'Sun, 28 Jun 2020 11:45:02 GMT', 'Server': 'Apache', 'Vary': 'Accept-Encoding', 'X-Powered-By': 'PHP/7.2.24', 'Content-Length': '1256', 'Connection': 'close'}
```

1. `import aiohttp`: imports the aiohttp library.
2. `async with aiohttp.ClientSession() as session`: creates a ClientSession object.
3. `async with session.get('https://www.example.com') as response`: makes a GET request to the specified URL.
4. `print(response.headers)`: prints the response headers.

## Helpful links

- [aiohttp Documentation](https://docs.aiohttp.org/en/stable/)
- [Python Aiohttp Tutorial](https://realpython.com/async-io-python/)

group: aiohttp

onelinerhub: [How to get headers using Python Aiohttp?](https://onelinerhub.com/python-aiohttp/how-to-get-headers-using-python-aiohttp)