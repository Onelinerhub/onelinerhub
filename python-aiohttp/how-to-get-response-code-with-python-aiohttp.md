# How to get response code with Python Aiohttp?
// plain

You can get response code with Python Aiohttp by using the `.status` attribute of the response object.

## Example code

```
import aiohttp

async with aiohttp.ClientSession() as session:
    async with session.get('https://www.example.com') as response:
        print(response.status)
```

## Output example

```
200
```

## Code explanation

- `import aiohttp`: imports the aiohttp library
- `async with aiohttp.ClientSession() as session`: creates a client session object
- `async with session.get('https://www.example.com') as response`: sends a GET request to the specified URL
- `print(response.status)`: prints the response status code

## Helpful links
- [aiohttp Documentation](https://docs.aiohttp.org/en/stable/)

group: aiohttp

onelinerhub: [How to get response code with Python Aiohttp?](https://onelinerhub.com/python-aiohttp/how-to-get-response-code-with-python-aiohttp)