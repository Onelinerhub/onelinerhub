# Bearer token request example with Python Aiohttp?
// plain

This example uses the Aiohttp library to make a request for a bearer token.

```python
import aiohttp

async def get_token():
    async with aiohttp.ClientSession() as session:
        async with session.post('https://example.com/token',
                                data={'grant_type': 'client_credentials'},
                                auth=aiohttp.BasicAuth('client_id', 'client_secret')) as resp:
            token = await resp.json()
            return token

token = await get_token()
```

The output of the code will be a JSON object containing the bearer token:

```
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
}
```

## Code explanation


1. `import aiohttp` - imports the Aiohttp library
2. `async def get_token()` - defines an asynchronous function to make the request
3. `async with session.post('https://example.com/token', data={'grant_type': 'client_credentials'}, auth=aiohttp.BasicAuth('client_id', 'client_secret')) as resp:` - makes a POST request to the token endpoint with the grant type and authentication credentials
4. `token = await resp.json()` - parses the response as JSON
5. `return token` - returns the token

## Helpful links

- [Aiohttp Documentation](https://docs.aiohttp.org/en/stable/)
- [Bearer Token Documentation](https://tools.ietf.org/html/rfc6750)

group: aiohttp

onelinerhub: [Bearer token request example with Python Aiohttp?](https://onelinerhub.com/python-aiohttp/bearer-token-request-example-with-python-aiohttp)