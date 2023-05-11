# How to use a proxy with a Python aiohttp client?
// plain

Using a proxy with a Python aiohttp client is easy. All you need to do is to pass the proxy URL as an argument to the `ProxyConnector` class.

```python
import aiohttp

proxy_url = 'http://user:pass@10.10.1.10:3128'

async with aiohttp.ClientSession(connector=aiohttp.ProxyConnector(proxy_url=proxy_url)) as session:
    async with session.get('http://example.org') as response:
        print(response.status)
```

## Output example

```
200
```

The code above creates a `ClientSession` object with a `ProxyConnector` object as an argument. The `ProxyConnector` object takes the proxy URL as an argument. The `ClientSession` object is then used to make a `GET` request to `http://example.org` using the proxy.

## Code explanation


1. `import aiohttp`: imports the `aiohttp` library.
2. `proxy_url = 'http://user:pass@10.10.1.10:3128'`: sets the proxy URL.
3. `aiohttp.ClientSession(connector=aiohttp.ProxyConnector(proxy_url=proxy_url))`: creates a `ClientSession` object with a `ProxyConnector` object as an argument.
4. `session.get('http://example.org')`: makes a `GET` request to `http://example.org` using the proxy.

## Helpful links

- [aiohttp Documentation](https://aiohttp.readthedocs.io/en/stable/)
- [ProxyConnector Documentation](https://aiohttp.readthedocs.io/en/stable/client_reference.html#aiohttp.connector.ProxyConnector)

group: aiohttp-client

onelinerhub: [How to use a proxy with a Python aiohttp client?](https://onelinerhub.com/python-aiohttp/how-to-use-a-proxy-with-a-python-aiohttp-client)