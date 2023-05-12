# How to make a POST request with Python Aiohttp?
// plain

Making a POST request with Python Aiohttp is easy. You can use the `aiohttp.ClientSession.post()` method to make a POST request.

## Example code

```
import aiohttp

async with aiohttp.ClientSession() as session:
    async with session.post('http://example.com/post', data={'key':'value'}) as resp:
        print(resp.status)
        print(await resp.text())
```

## Output example

```
200
<html>...</html>
```

## Code explanation

- `import aiohttp`: imports the aiohttp library
- `async with aiohttp.ClientSession() as session`: creates a ClientSession object
- `async with session.post('http://example.com/post', data={'key':'value'}) as resp`: makes a POST request to the specified URL with the given data
- `print(resp.status)`: prints the response status code
- `print(await resp.text())`: prints the response body

## Helpful links
- [aiohttp Documentation](https://docs.aiohttp.org/en/stable/)

group: aiohttp

onelinerhub: [How to make a POST request with Python Aiohttp?](https://onelinerhub.com/python-aiohttp/how-to-make-a-post-request-with-python-aiohttp)