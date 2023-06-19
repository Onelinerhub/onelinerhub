# How do I use query params with Express.js?
// plain

Query params are a way to pass data from a client to a server. With Express.js, you can access query params using the `req.query` object. Here is an example of how to use query params with Express.js:

```
// server.js
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  const name = req.query.name;
  res.send(`Hello ${name}`);
});

app.listen(3000);
```

If we make a request to `http://localhost:3000/?name=John`, the output would be `Hello John`.

## Code explanation


1. `const express = require('express');` - This line imports the Express.js library.
2. `const app = express();` - This line creates an Express.js app.
3. `app.get('/', (req, res) => {` - This line creates a GET route for the root path.
4. `const name = req.query.name;` - This line accesses the query param `name` from the `req.query` object.
5. `res.send(`Hello ${name}`);` - This line sends a response with the value of the `name` query param.
6. `app.listen(3000);` - This line starts the Express.js server on port 3000.

## Helpful links

- [Express.js Query Params](https://expressjs.com/en/api.html#req.query)
- [Express.js Routing](https://expressjs.com/en/guide/routing.html)

onelinerhub: [How do I use query params with Express.js?](https://onelinerhub.com/expressjs/how-do-i-use-query-params-with-express-js)