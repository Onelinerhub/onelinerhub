# How do I use middleware with Express.js?
// plain

Middleware functions are functions that have access to the request object (req), the response object (res), and the next middleware function in the application’s request-response cycle.

Express.js allows you to use middleware functions in the following way:

```
const express = require('express');
const app = express();

app.use(function (req, res, next) {
  console.log('Time:', Date.now());
  next();
});

app.get('/', function (req, res) {
  res.send('Hello World!');
});

app.listen(3000);
```

This example will log the current time before responding with ‘Hello World!’ when a request is made to the root URL.

## Code explanation


1. `const express = require('express');` - This imports the Express.js module.
2. `const app = express();` - This creates an Express.js application.
3. `app.use(function (req, res, next) {` - This adds a middleware function to the Express.js application.
4. `console.log('Time:', Date.now());` - This logs the current time.
5. `next();` - This passes control to the next middleware function.
6. `app.get('/', function (req, res) {` - This adds a route handler for the root URL.
7. `res.send('Hello World!');` - This sends a response with ‘Hello World!’.
8. `app.listen(3000);` - This starts the Express.js application on port 3000.

For more information on using middleware with Express.js, please see [the official Express.js documentation](https://expressjs.com/en/guide/using-middleware.html).

onelinerhub: [How do I use middleware with Express.js?](https://onelinerhub.com/expressjs/how-do-i-use-middleware-with-express-js)