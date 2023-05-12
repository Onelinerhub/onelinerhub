# How to check if a session is closed with Python Aiohttp?
// plain

To check if a session is closed with Python Aiohttp, you can use the `closed` property of the `ClientSession` object. This property returns a boolean value indicating whether the session is closed or not.

## Example code

```
import aiohttp

async with aiohttp.ClientSession() as session:
    print(session.closed)
```

## Output example

```
False
```

## Code explanation

- `import aiohttp`: imports the aiohttp library
- `async with aiohttp.ClientSession() as session`: creates a ClientSession object
- `session.closed`: returns a boolean value indicating whether the session is closed or not

## Helpful links
- [aiohttp Documentation](https://docs.aiohttp.org/en/stable/)

group: aiohttp

onelinerhub: [How to check if a session is closed with Python Aiohttp?](https://onelinerhub.com/python-aiohttp/how-to-check-if-a-session-is-closed-with-python-aiohttp)