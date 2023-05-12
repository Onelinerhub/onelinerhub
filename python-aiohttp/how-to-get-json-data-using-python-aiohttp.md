# How to get JSON data using Python Aiohttp?
// plain

Using Python Aiohttp, you can get JSON data from a web server.

```
import aiohttp

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()

async def main():
    async with aiohttp.ClientSession() as session:
        json_data = await fetch(session, 'https://example.com/data.json')
        print(json_data)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
```

```
{
  "name": "John Doe",
  "age": 34
}
```

1. `import aiohttp` - imports the aiohttp library
2. `async def fetch(session, url)` - defines an asynchronous function to fetch the JSON data from the given URL
3. `async with session.get(url) as response` - uses the session to make a GET request to the given URL
4. `return await response.json()` - returns the response as JSON
5. `async def main()` - defines an asynchronous function to run the code
6. `async with aiohttp.ClientSession() as session` - creates a client session to make the request
7. `json_data = await fetch(session, 'https://example.com/data.json')` - calls the `fetch` function to get the JSON data from the given URL
8. `print(json_data)` - prints the JSON data
9. `loop = asyncio.get_event_loop()` - creates an event loop
10. `loop.run_until_complete(main())` - runs the `main` function until it is complete

## Helpful links

- [aiohttp Documentation](https://docs.aiohttp.org/en/stable/)
- [Python Asyncio Documentation](https://docs.python.org/3/library/asyncio.html)

group: aiohttp

onelinerhub: [How to get JSON data using Python Aiohttp?](https://onelinerhub.com/python-aiohttp/how-to-get-json-data-using-python-aiohttp)