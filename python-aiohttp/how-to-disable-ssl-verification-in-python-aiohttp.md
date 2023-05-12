# How to disable SSL verification in Python Aiohttp?
// plain

To disable SSL verification in Python Aiohttp, you can use the `verify_ssl` parameter in the `ClientSession` constructor. This parameter takes a boolean value, and when set to `False`, it will disable SSL verification.

## Example code

```
import aiohttp

async with aiohttp.ClientSession(verify_ssl=False) as session:
    async with session.get('https://example.com') as response:
        print(response.status)
```

## Output example

```
200
```

## Code explanation

- `import aiohttp`: imports the aiohttp library
- `async with aiohttp.ClientSession(verify_ssl=False) as session`: creates a ClientSession object with SSL verification disabled
- `async with session.get('https://example.com') as response`: makes a GET request to the specified URL
- `print(response.status)`: prints the response status code

## Helpful links
- [aiohttp Documentation](https://aiohttp.readthedocs.io/en/stable/)

group: aiohttp

onelinerhub: [How to disable SSL verification in Python Aiohttp?](https://onelinerhub.com/python-aiohttp/how-to-disable-ssl-verification-in-python-aiohttp)