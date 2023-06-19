# How do I set a header using Express.js?
// plain

Express.js is a web application framework for Node.js. It is used to create web applications and APIs. To set a header using Express.js, use the `set` method of the `response` object.

## Example code

```
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.set('Content-Type', 'text/html');
  res.send('<h1>Hello World</h1>');
});

app.listen(3000);
```

## Output example

```
Server listening on port 3000
```

The code above sets the response header to `Content-Type: text/html`. This tells the browser to render the response as an HTML page.

The `set` method takes two parameters: the header name and the header value. It is also possible to set multiple headers at once using the `set` method.

## Example

```
res.set({
  'Content-Type': 'text/html',
  'X-Powered-By': 'Express'
});
```

## Helpful links

- [Express.js Documentation](https://expressjs.com/en/4x/api.html#res.set)
- [Express.js Tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Express_Nodejs/Introduction)

onelinerhub: [How do I set a header using Express.js?](https://onelinerhub.com/expressjs/how-do-i-set-a-header-using-express-js)