# How to prevent the "unclosed client session" warning in Python aiohttp?
// plain

The "unclosed client session" warning in Python aiohttp can be prevented by properly closing the client session. This can be done by using the `close()` method of the `ClientSession` class.

## Example code

```
import aiohttp

async with aiohttp.ClientSession() as session:
    # Do something with session
    await session.close()
```

## Output example

```
None
```

## Code explanation

- `import aiohttp`: imports the aiohttp library
- `async with aiohttp.ClientSession() as session`: creates a client session object
- `await session.close()`: closes the client session

## Helpful links
- [aiohttp Documentation](https://docs.aiohttp.org/en/stable/)