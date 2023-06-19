# How can I make an XHR request using Express.js?
// plain

An XHR request can be made using Express.js by using the `express.json()` middleware. This middleware will parse the body of the request and make it available in the `req.body` object.

## Example code

```
const express = require('express');
const app = express();

// Parse request body as JSON
app.use(express.json());

// Make an XHR request
app.post('/data', (req, res) => {
  // req.body will contain the parsed JSON data
  console.log(req.body);
  res.send('Success!');
});

app.listen(3000);
```

## Output example

```
Success!
```

The code consists of the following parts:
- `const express = require('express')` - imports the `express` module
- `const app = express()` - creates an instance of an Express application
- `app.use(express.json())` - adds the `express.json()` middleware to the application, which will parse the body of the request as JSON
- `app.post('/data', (req, res) => {...})` - adds a POST endpoint to the application, which will be called when an XHR request is made to the `/data` endpoint
- `console.log(req.body)` - logs the parsed JSON data from the request body to the console
- `res.send('Success!')` - sends a response back to the client

## Helpful links
- [Express.js documentation](https://expressjs.com/en/4x/api.html#express.json)

onelinerhub: [How can I make an XHR request using Express.js?](https://onelinerhub.com/expressjs/how-can-i-make-an-xhr-request-using-express-js)