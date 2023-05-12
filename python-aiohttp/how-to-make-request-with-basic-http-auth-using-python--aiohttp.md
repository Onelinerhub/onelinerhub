# How to make request with basic HTTP auth using Python  Aiohttp?
// plain

Using Aiohttp, you can make a request with basic HTTP auth using the `aiohttp.BasicAuth` class. The following example code will make a request to a URL with basic auth credentials:

```python
import aiohttp

async with aiohttp.ClientSession() as session:
    auth = aiohttp.BasicAuth(login='username', password='password')
    async with session.get('http://example.com', auth=auth) as resp:
        print(resp.status)
```

The output of the above code will be `200`, indicating that the request was successful.

## Code explanation


1. `import aiohttp`: imports the Aiohttp library.
2. `aiohttp.BasicAuth(login='username', password='password')`: creates an instance of the `aiohttp.BasicAuth` class with the username and password credentials.
3. `session.get('http://example.com', auth=auth)`: makes a request to the URL with the basic auth credentials.
4. `print(resp.status)`: prints the response status code.

## Helpful links

- [Aiohttp Documentation](https://docs.aiohttp.org/en/stable/)
- [Basic Auth Tutorial](https://www.codementor.io/@ilyaas97/basic-authentication-in-aiohttp-with-python-3-x-8q3qh3jbz)

group: aiohttp

onelinerhub: [How to make request with basic HTTP auth using Python  Aiohttp?](https://onelinerhub.com/python-aiohttp/how-to-make-request-with-basic-http-auth-using-python--aiohttp)