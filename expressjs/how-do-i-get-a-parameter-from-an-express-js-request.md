# How do I get a parameter from an Express.js request?
// plain

To get a parameter from an Express.js request, you can use the `req.params` object. This object contains the route parameters that were defined when the route was registered. For example, if you had a route defined as `app.get('/user/:id', (req, res) => { ... })`, then you could access the `id` parameter in the request with `req.params.id`.

For example:
```
app.get('/user/:id', (req, res) => {
  const id = req.params.id;
  console.log(id);
});
```
## Output example
 `123` (if the request was `/user/123`)

The `req.params` object is populated with all the route parameters that were defined when the route was registered. The keys in the object are the names of the parameters, and the values are the values that were provided in the request.

Here is a list of the parts of the example code and what they do:

- `app.get('/user/:id', (req, res) => { ... })`: this is the route definition. It defines a route that will respond to requests to `/user/<id>`, where `<id>` is a variable that can be accessed with `req.params.id`.

- `const id = req.params.id;`: this line gets the `id` parameter from the request and stores it in a variable.

- `console.log(id);`: this line prints the value of the `id` parameter to the console.

## Helpful links

- [Express Documentation - req.params](https://expressjs.com/en/4x/api.html#req.params)

onelinerhub: [How do I get a parameter from an Express.js request?](https://onelinerhub.com/expressjs/how-do-i-get-a-parameter-from-an-express-js-request)