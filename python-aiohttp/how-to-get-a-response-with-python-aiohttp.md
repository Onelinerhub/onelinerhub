# How to get a response with Python Aiohttp?
// plain

Using Python Aiohttp, you can get a response from a web server by making an asynchronous HTTP request.

## Example code

```
import aiohttp

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'http://python.org')
        print(html)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
```

## Output example

```
<!doctype html>
<!--[if lt IE 7]>   <html class="no-js ie6 lt-ie7 lt-ie8 lt-ie9">   <![endif]-->
<!--[if IE 7]>      <html class="no-js ie7 lt-ie8 lt-ie9">          <![endif]-->
<!--[if IE 8]>      <html class="no-js ie8 lt-ie9">                 <![endif]-->
<!--[if gt IE 8]><!--><html class="no-js" lang="en" dir="ltr">  <!--<![endif]-->

<head>
    ...
```

The code consists of the following parts:

1. Importing the aiohttp library: `import aiohttp`
2. Defining an asynchronous function to make the request: `async def fetch(session, url)`
3. Creating a ClientSession object: `async with aiohttp.ClientSession() as session`
4. Making the request and getting the response: `html = await fetch(session, 'http://python.org')`
5. Printing the response: `print(html)`
6. Running the asynchronous function: `loop.run_until_complete(main())`

## Helpful links

- [Python Aiohttp Documentation](https://aiohttp.readthedocs.io/en/stable/)
- [Python Asyncio Documentation](https://docs.python.org/3/library/asyncio.html)

group: aiohttp

onelinerhub: [How to get a response with Python Aiohttp?](https://onelinerhub.com/python-aiohttp/how-to-get-a-response-with-python-aiohttp)