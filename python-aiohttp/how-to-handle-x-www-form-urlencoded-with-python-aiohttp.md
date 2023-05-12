# How to handle x-www-form-urlencoded with Python Aiohttp?
// plain

X-www-form-urlencoded is a format used to send data to a server. It can be handled with Python Aiohttp by using the `aiohttp.FormData` class.

```
import aiohttp

async with aiohttp.ClientSession() as session:
    form_data = aiohttp.FormData()
    form_data.add_field('name', 'value')
    async with session.post('http://example.com', data=form_data) as resp:
        print(resp.status)
```

## Output example

```
200
```

## Code explanation

- `import aiohttp`: imports the aiohttp library
- `aiohttp.FormData`: creates a FormData object
- `form_data.add_field('name', 'value')`: adds a field to the FormData object
- `session.post('http://example.com', data=form_data)`: sends the FormData object to the server
- `resp.status`: prints the response status code

## Helpful links
- [aiohttp Documentation](https://docs.aiohttp.org/en/stable/)
- [FormData Documentation](https://docs.aiohttp.org/en/stable/client_reference.html#aiohttp.FormData)

group: aiohttp

onelinerhub: [How to handle x-www-form-urlencoded with Python Aiohttp?](https://onelinerhub.com/python-aiohttp/how-to-handle-x-www-form-urlencoded-with-python-aiohttp)