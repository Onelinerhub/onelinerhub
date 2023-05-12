# How to use HTTPS with Python Aiohttp?
// plain

Using HTTPS with Python Aiohttp is easy and straightforward.

```
import aiohttp

async with aiohttp.ClientSession() as session:
    async with session.get('https://example.com') as response:
        print(response.status)
```

The output of the above code will be `200`.

To use HTTPS with Python Aiohttp, you need to:

1. Import the `aiohttp` module.
2. Create an `aiohttp.ClientSession` object.
3. Use the `session.get()` method to make a request to the HTTPS URL.
4. Use the `response.status` attribute to check the status of the response.

## Helpful links

- [aiohttp Documentation](https://docs.aiohttp.org/en/stable/)
- [Python Aiohttp Tutorial](https://realpython.com/async-io-python/)

group: aiohttp

onelinerhub: [How to use HTTPS with Python Aiohttp?](https://onelinerhub.com/python-aiohttp/how-to-use-https-with-python-aiohttp)