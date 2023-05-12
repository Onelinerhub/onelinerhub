# How to download a file with Python Aiohttp?
// plain

Using the Aiohttp library, you can download a file with Python in a few simple steps.

```
import aiohttp

async with aiohttp.ClientSession() as session:
    async with session.get('http://example.com/file.zip') as resp:
        with open('file.zip', 'wb') as f_handle:
            while True:
                chunk = await resp.content.read(1024)
                if not chunk:
                    break
                f_handle.write(chunk)
```

This code will download the file `file.zip` from `http://example.com/file.zip` and save it to the current directory.

The code consists of the following parts:

1. `import aiohttp` - imports the Aiohttp library.
2. `async with aiohttp.ClientSession() as session` - creates a client session.
3. `async with session.get('http://example.com/file.zip') as resp` - sends a GET request to the specified URL.
4. `while True` - loops until the end of the file is reached.
5. `chunk = await resp.content.read(1024)` - reads the response content in chunks of 1024 bytes.
6. `if not chunk` - checks if the chunk is empty.
7. `break` - breaks out of the loop.
8. `f_handle.write(chunk)` - writes the chunk to the file.

## Helpful links

- [Aiohttp Documentation](https://docs.aiohttp.org/en/stable/)

group: aiohttp

onelinerhub: [How to download a file with Python Aiohttp?](https://onelinerhub.com/python-aiohttp/how-to-download-a-file-with-python-aiohttp)