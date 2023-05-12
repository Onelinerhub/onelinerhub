# Example of using Python Aiohttp for requests
// plain

Python Aiohttp is an asynchronous HTTP client/server framework. It allows you to make requests to web servers and receive responses asynchronously.

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

The code above uses the `aiohttp` library to make an asynchronous request to the Python website. It creates a `ClientSession` object, which is used to make the request. The `fetch` function is used to make the request and the `main` function is used to execute the request. Finally, the `run_until_complete` method is used to run the `main` function.

## Helpful links
- [aiohttp Documentation](https://docs.aiohttp.org/en/stable/)
- [Python Asyncio Documentation](https://docs.python.org/3/library/asyncio.html)

group: aiohttp

onelinerhub: [Example of using Python Aiohttp for requests](https://onelinerhub.com/python-aiohttp/example-of-using-python-aiohttp-for-requests)