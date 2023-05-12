# How to get response text with Python Aiohttp?
// plain

Using the Aiohttp library, you can get response text with Python. The following example code block shows how to do this:
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
The output of the example code is the HTML of the Python website:
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
1. `import aiohttp` imports the Aiohttp library.
2. `async def fetch(session, url)` defines a function that takes a session and a URL as parameters and returns the response text.
3. `async def main()` defines a function that creates a session and calls the `fetch` function with the URL of the Python website.
4. `if __name__ == '__main__'` checks if the script is being run directly and calls the `main` function.

For more information, see the [Aiohttp documentation](https://aiohttp.readthedocs.io/en/stable/).

group: aiohttp

onelinerhub: [How to get response text with Python Aiohttp?](https://onelinerhub.com/python-aiohttp/how-to-get-response-text-with-python-aiohttp)