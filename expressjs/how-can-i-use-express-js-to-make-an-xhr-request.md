# How can I use Express.js to make an XHR request?
// plain

Express.js is a web application framework for Node.js that provides a robust set of features for web and mobile applications. It is also widely used for making XHR (XMLHttpRequest) requests. To make an XHR request using Express.js, you can use the built-in `request` module.

## Example code

```
const express = require('express');
const request = require('request');
const app = express();

app.get('/', (req, res) => {
  request('https://example.com', (error, response, body) => {
    if (!error && response.statusCode == 200) {
      res.send(body);
    }
  });
});

app.listen(3000);
```

The example code above creates an Express.js server which listens on port 3000, and makes an XHR request to `https://example.com` when a user visits the root URL. The response body is then sent back to the user.

The code can be broken down into the following parts:

1. `const express = require('express');` - This line imports the Express.js module.
2. `const request = require('request');` - This line imports the `request` module, which is used for making XHR requests.
3. `const app = express();` - This line creates an Express.js application.
4. `app.get('/', (req, res) => {` - This line creates a route handler for the root URL.
5. `request('https://example.com', (error, response, body) => {` - This line makes an XHR request to `https://example.com`.
6. `if (!error && response.statusCode == 200) {` - This line checks if the request was successful.
7. `res.send(body);` - This line sends the response back to the user.

For more information, see the [Express.js documentation](https://expressjs.com/en/guide/routing.html) and the [Request documentation](https://www.npmjs.com/package/request).

*Note:* The example code provided is for demonstration purposes only and should not be used in production.

onelinerhub: [How can I use Express.js to make an XHR request?](https://onelinerhub.com/expressjs/how-can-i-use-express-js-to-make-an-xhr-request)