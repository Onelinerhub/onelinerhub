# How do I use Express.js to handle x-www-form-urlencoded data?
// plain

Express.js is a web application framework for Node.js. It can be used to handle x-www-form-urlencoded data. To do this, you need to install the body-parser middleware. This middleware is used to parse incoming request bodies. Here is an example of how to use body-parser to handle x-www-form-urlencoded data:

```
const express = require('express');
const bodyParser = require('body-parser');

const app = express();

// parse application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: false }));

app.post('/form', (req, res) => {
  console.log(req.body);
  res.send('Form Received');
});
```

This example creates an Express server that listens for POST requests to the `/form` endpoint. The body-parser middleware is used to parse the x-www-form-urlencoded data in the request body. The parsed data is then available in the `req.body` object.

## Code explanation


1. `const express = require('express');` - This imports the Express module.
2. `const bodyParser = require('body-parser');` - This imports the body-parser middleware.
3. `const app = express();` - This creates an Express application.
4. `app.use(bodyParser.urlencoded({ extended: false }));` - This configures the body-parser middleware to parse x-www-form-urlencoded data.
5. `app.post('/form', (req, res) => {` - This defines a route handler for POST requests to the `/form` endpoint.
6. `console.log(req.body);` - This logs the parsed x-www-form-urlencoded data from the request body.
7. `res.send('Form Received');` - This sends a response to the client.

## Helpful links

- [Express.js](https://expressjs.com/)
- [body-parser](https://www.npmjs.com/package/body-parser)

onelinerhub: [How do I use Express.js to handle x-www-form-urlencoded data?](https://onelinerhub.com/expressjs/how-do-i-use-express-js-to-handle-x-www-form-urlencoded-data)