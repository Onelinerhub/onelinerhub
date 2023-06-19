# How can I use query parameters in an Express.js application?
// plain

Query parameters are used to filter and sort data in an Express.js application. To use query parameters, first define a route in the Express.js application that will accept the query parameters. For example:

```
app.get('/users', (req, res) => {
  // code to handle query parameters
});
```

The `req` object contains the query parameters in the `query` property. For example, if the route is called with `/users?name=John&age=20`, then `req.query` will contain the object `{name: "John", age: 20}`.

The code to handle the query parameters can then use the `req.query` object to filter and sort the data. For example, to find all users with the name `John` and age `20`:

```
const users = [
  {name: "John", age: 20},
  {name: "Bob", age: 25},
  {name: "John", age: 30},
];

const filteredUsers = users.filter(user =>
  user.name === req.query.name && user.age === req.query.age
);

// filteredUsers = [{name: "John", age: 20}]
```

## Code explanation

1. `app.get('/users', (req, res) => { ... })`: Defines a route that accepts query parameters.
2. `req.query`: Contains the query parameters.
3. `users.filter(user => ...)`: Filters the users array based on the query parameters.

## Helpful links
- [Express.js routing documentation](http://expressjs.com/en/guide/routing.html)
- [MDN Web API: URLSearchParams](https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams)

onelinerhub: [How can I use query parameters in an Express.js application?](https://onelinerhub.com/expressjs/how-can-i-use-query-parameters-in-an-express-js-application)