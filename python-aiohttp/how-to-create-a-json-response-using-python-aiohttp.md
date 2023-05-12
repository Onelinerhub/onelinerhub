# How to create a JSON response using Python Aiohttp?
// plain

Creating a JSON response using Python Aiohttp is easy. The following example code block shows how to create a JSON response using Aiohttp:
```
import aiohttp

async def handle(request):
    response_obj = {'status': 'success'}
    return aiohttp.web.json_response(response_obj)
```
The output of the above code will be a JSON response object:
```
{'status': 'success'}
```
The code consists of the following parts:
1. Importing the aiohttp library: `import aiohttp`
2. Defining an asynchronous function to handle the request: `async def handle(request)`
3. Creating a response object: `response_obj = {'status': 'success'}`
4. Returning the response object as a JSON response: `return aiohttp.web.json_response(response_obj)`

## Helpful links
- [Aiohttp Documentation](https://docs.aiohttp.org/en/stable/)
- [Python Aiohttp Tutorial](https://realpython.com/async-io-python/)

group: aiohttp

onelinerhub: [How to create a JSON response using Python Aiohttp?](https://onelinerhub.com/python-aiohttp/how-to-create-a-json-response-using-python-aiohttp)