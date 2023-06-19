# How do I use Express.js JSON middleware?
// plain

Express.js JSON middleware is a middleware that enables Express.js applications to parse incoming JSON data. It is designed to be used as an alternative to body-parser, which is the standard middleware used by Express.js applications for parsing incoming data.

To use Express.js JSON middleware, you need to first install it using npm:

```
npm install express-json
```

Then, you need to require it in your Express.js application:

```
const expressJson = require('express-json');
```

Once the middleware is required, you can add it to your Express.js application:

```
app.use(expressJson());
```

Now, the Express.js application is able to parse incoming JSON data. For example, if you have an endpoint that accepts a JSON object:

```
app.post('/api/create-user', (req, res) => {
  const { username, email } = req.body;
  // ...
});
```

You can test it by sending a POST request with a JSON body:

```
{
  "username": "john",
  "email": "john@example.com"
}
```

The Express.js application will be able to parse the incoming JSON data and make it available via the `req.body` object.

## Helpful links
- [Express.js JSON Middleware](https://www.npmjs.com/package/express-json)
- [Express.js Documentation](https://expressjs.com/en/guide/using-middleware.html)

onelinerhub: [How do I use Express.js JSON middleware?](https://onelinerhub.com/expressjs/how-do-i-use-express-js-json-middleware)