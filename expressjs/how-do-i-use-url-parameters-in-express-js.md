# How do I use URL parameters in Express.js?
// plain

URL parameters are a way to pass data from the client to the server in an Express.js application. They are typically used to pass information that is used to customize the response for a particular request.

For example, to use URL parameters in an Express.js application, you can use the `req.params` object. Here is an example of how to use this object in a route:

```javascript
app.get('/user/:name', (req, res) => {
  const name = req.params.name;
  res.send(`Welcome, ${name}!`);
});
```

If we make a request to `/user/John`, we will get the output `Welcome, John!`

## Code explanation

- `app.get()`: the Express.js method used to register a route
- `/user/:name`: the route URL, where `:name` is a parameter
- `req.params.name`: the object used to access the URL parameter
- `res.send()`: the Express.js method used to send a response

For more information about URL parameters in Express.js, see the [documentation](https://expressjs.com/en/4x/api.html#req.params).

onelinerhub: [How do I use URL parameters in Express.js?](https://onelinerhub.com/expressjs/how-do-i-use-url-parameters-in-express-js)