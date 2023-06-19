# How can I create nested routes in Express.js?
// plain

Nested routes are routes that are nested within other routes in Express.js. This allows us to create a hierarchical structure for our routes. Here is an example of how to create nested routes in Express.js:

```js
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.get('/users', (req, res) => {
  res.send('Users page');
});

app.get('/users/:userId', (req, res) => {
  res.send(`User ${req.params.userId}`);
});

app.listen(3000);
```

This example code will create 3 routes: `/`, `/users` and `/users/:userId`. The `/users/:userId` route is nested within the `/users` route. When a request is made for `/users/:userId`, the `:userId` parameter will be passed to the route handler.

## Code explanation


- `const express = require('express');` - This imports the Express.js module.
- `const app = express();` - This creates an Express.js application.
- `app.get('/', (req, res) => {...});` - This creates a route handler for the `/` route.
- `app.get('/users', (req, res) => {...});` - This creates a route handler for the `/users` route.
- `app.get('/users/:userId', (req, res) => {...});` - This creates a route handler for the `/users/:userId` route.
- `res.send(`User ${req.params.userId}`);` - This sends the `userId` parameter passed in the request back as a response.

## Helpful links
- [Express.js Documentation](https://expressjs.com/en/guide/routing.html)
- [Creating Nested Routes in Express.js](https://medium.com/@jimmy_dee/creating-nested-routes-in-express-js-6c4e4f7d9b3e)

onelinerhub: [How can I create nested routes in Express.js?](https://onelinerhub.com/expressjs/how-can-i-create-nested-routes-in-express-js)