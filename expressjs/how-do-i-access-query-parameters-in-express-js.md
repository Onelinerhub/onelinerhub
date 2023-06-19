# How do I access query parameters in Express.js?
// plain

In Express.js, you can access query parameters by using the `req.query` object. This object contains the query string parameters in the URL as key-value pairs. For example, if the URL is `http://localhost:3000/search?q=express`, then `req.query` will be:

```
{
  q: 'express'
}
```

To access a specific query parameter, you can use bracket notation, like so:

```
const query = req.query['q'];
console.log(query); // 'express'
```

In the code above:

- `req` is the request object
- `req.query` is the object containing the query string parameters
- `req.query['q']` is the specific query parameter we are accessing

For more information, see [this page](https://expressjs.com/en/api.html#req.query).

onelinerhub: [How do I access query parameters in Express.js?](https://onelinerhub.com/expressjs/how-do-i-access-query-parameters-in-express-js)