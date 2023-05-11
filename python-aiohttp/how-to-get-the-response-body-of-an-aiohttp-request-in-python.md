# How to get the response body of an aiohttp request in Python?
// plain

To get the response body of an aiohttp request in Python, you can use the `read()` method of the response object. The following example code will print the response body of a GET request to a given URL:

```
import aiohttp

async with aiohttp.ClientSession() as session:
    async with session.get('https://example.com') as response:
        response_body = await response.read()
        print(response_body)
```

## Output example

```
b'<!doctype html>\n<html>\n<head>\n    <title>Example Domain</title>\n\n    <meta charset="utf-8" />\n    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />\n    <meta name="viewport" content="width=device-width, initial-scale=1" />\n    <style type="text/css">\n    body {\n        background-color: #f0f0f2;\n        margin: 0;\n        padding: 0;\n        font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;\n        \n    }\n    div {\n        width: 600px;\n        margin: 5em auto;\n        padding: 50px;\n        background-color: #fdfdff;\n        border-radius: 1em;\n    }\n    a:link, a:visited {\n        color: #38488f;\n        text-decoration: none;\n    }\n    @media (max-width: 700px) {\n        body {\n            background-color: #fff;\n        }\n        div {\n            width: auto;\n            margin: 0 auto;\n            border-radius: 0;\n            padding: 1em;\n        }\n    }\n    </style>    \n</head>\n\n<body>\n<div>\n    <h1>Example Domain</h1>\n    <p>This domain is for use in illustrative examples in documents. You may use this\n    domain in literature without prior coordination or asking for permission.</p>\n    <p><a href="https://www.iana.org/domains/example">More information...</a></p>\n</div>\n</body>\n</html>\n'
```

## Code explanation

- `import aiohttp`: imports the aiohttp library
- `async with aiohttp.ClientSession() as session`: creates a client session object
- `async with session.get('https://example.com') as response`: sends a GET request to the given URL and stores the response in the `response` variable
- `response_body = await response.read()`: reads the response body and stores it in the `response_body` variable
- `print(response_body)`: prints the response body

## Helpful links
- [aiohttp Documentation](https://docs.aiohttp.org/en/stable/)

group: aiohttp

onelinerhub: [How to get the response body of an aiohttp request in Python?](https://onelinerhub.com/python-aiohttp/how-to-get-the-response-body-of-an-aiohttp-request-in-python)