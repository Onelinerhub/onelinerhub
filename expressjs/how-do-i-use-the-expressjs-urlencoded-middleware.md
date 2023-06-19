# How do I use the expressjs urlencoded middleware?
// plain

The expressjs urlencoded middleware is used to parse incoming request bodies which are encoded in URL-encoded format. It is typically used to parse data from HTML forms.

## Example code

```
const express = require('express');
const app = express();

app.use(express.urlencoded({ extended: true }));
```

The `app.use` method is used to register the middleware with express. The `extended` option is set to `true` to allow for nested objects to be parsed.

The middleware will then parse the request body and make it available as `req.body` in the request handler.

## Example code

```
app.post('/', (req, res) => {
  console.log(req.body);
});
```

## Output example

```
{
  name: 'John',
  age: 30
}
```

The middleware will also parse the query string and make it available as `req.query` in the request handler.

## Example code

```
app.get('/', (req, res) => {
  console.log(req.query);
});
```

## Output example

```
{
  name: 'John',
  age: 30
}
```

## Helpful links
- [ExpressJS Documentation](https://expressjs.com/en/4x/api.html#express.urlencoded)
- [MDN Web Docs - URL Encoding](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent)

onelinerhub: [How do I use the expressjs urlencoded middleware?](https://onelinerhub.com/expressjs/how-do-i-use-the-expressjs-urlencoded-middleware)