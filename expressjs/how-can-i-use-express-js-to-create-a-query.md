# How can I use Express.js to create a query?
// plain

Express.js is a web application framework for Node.js that allows you to create a query. To do this, you need to set up a route and a function to handle the query.

For example, this code block will create a query route that will return the value of `queryParam` when a `GET` request is sent to `/query`:
```js
// Setup the query route
app.get('/query', (req, res) => {
  // Get the query parameter
  const queryParam = req.query.param;
  // Send the response
  res.send(queryParam);
});
```

When a `GET` request is sent to `/query?param=hello`, the response will be `hello`.

The code block above consists of the following parts:
1. `app.get('/query', (req, res) => {` - This sets up the query route. It specifies that when a `GET` request is sent to `/query`, the following function will be called.
2. `const queryParam = req.query.param;` - This gets the query parameter (`param`) from the request.
3. `res.send(queryParam);` - This sends the response. In this case, it's the value of `queryParam`.

For more information on Express.js, see the [documentation](https://expressjs.com/en/4x/api.html).

onelinerhub: [How can I use Express.js to create a query?](https://onelinerhub.com/expressjs/how-can-i-use-express-js-to-create-a-query)