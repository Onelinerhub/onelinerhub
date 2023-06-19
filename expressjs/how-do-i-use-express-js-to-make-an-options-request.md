# How do I use Express.js to make an options request?
// plain

An **options request** is a type of HTTP request used to determine the capabilities of a server. Express.js can be used to make such a request.

Below is an example of an options request using Express.js:

```javascript
const express = require('express');
const app = express();

app.options('/', (req, res) => {
  res.status(200).send('OK');
});

app.listen(3000);
```

This code will create a server listening on port 3000, and will respond to an options request on the root path with an HTTP status code of 200 and a message of 'OK'.

The code consists of the following parts:

1. `const express = require('express');` - This line imports the Express.js module and saves it as a constant.
2. `const app = express();` - This line creates an Express.js application and saves it as a constant.
3. `app.options('/', (req, res) => {` - This line defines a route for an options request on the root path.
4. `res.status(200).send('OK');` - This line sets the response status code to 200 and sends a message of 'OK'.
5. `app.listen(3000);` - This line starts the server listening on port 3000.

For more information on options requests and Express.js, see the following links:

- [Express.js Documentation](https://expressjs.com/en/guide/routing.html)
- [MDN Web Docs - HTTP Options Request](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/OPTIONS)

onelinerhub: [How do I use Express.js to make an options request?](https://onelinerhub.com/expressjs/how-do-i-use-express-js-to-make-an-options-request)