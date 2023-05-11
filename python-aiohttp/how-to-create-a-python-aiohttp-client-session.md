# How to create a Python aiohttp client session?
// plain

Creating a Python aiohttp client session is easy and straightforward.

```
import aiohttp

async with aiohttp.ClientSession() as session:
    async with session.get('http://example.com') as response:
        print(response.status)
```

The output of the above code will be `200`.

The code consists of two parts:

1. `import aiohttp`: This imports the aiohttp library.

2. `async with aiohttp.ClientSession() as session`: This creates a client session object.

## Helpful links

- [aiohttp Documentation](https://docs.aiohttp.org/en/stable/)
- [aiohttp Tutorial](https://docs.aiohttp.org/en/stable/tutorial.html)

group: aiohttp-client

onelinerhub: [How to create a Python aiohttp client session?](https://onelinerhub.com/python-aiohttp/how-to-create-a-python-aiohttp-client-session)