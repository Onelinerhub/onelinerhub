# request

How do I make a GET request with Express.js?
// plain

You can make a GET request with Express.js using the `app.get()` method. This method takes two arguments: a route path and a callback function. The callback function is used to process the request and return a response.

For example, to make a GET request to the route `/users`:

```javascript
app.get('/users', (req, res) => {
  res.send('This is a GET request to the users route');
});
```

This will return the following output:

```
This is a GET request to the users route
```

The `app.get()` method takes two arguments:

1. `route` - a string representing the route path
2. `callback` - a function that is called when the route is requested. It takes two arguments, `req` and `res` which are objects representing the request and response respectively.

The `req` object contains data about the request such as the query parameters, headers, and body. The `res` object is used to send a response back to the client.

You can find more information about the `app.get()` method in the [Express.js documentation](https://expressjs.com/en/4x/api.html#app.get).

onelinerhub: [request

How do I make a GET request with Express.js?](https://onelinerhub.com/expressjs/request--how-do-i-make-a-get-request-with-express-js)