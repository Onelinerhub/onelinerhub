# How do I use Express.js to parse request parameters?
// plain

Express.js provides a built-in middleware function called `express.urlencoded` which can be used to parse request parameters.

The following example code will parse the request parameters that are sent in a POST request body and log them to the console:

```javascript
const express = require('express');
const app = express();

app.use(express.urlencoded({ extended: true }));

app.post('/', (req, res) => {
  console.log(req.body);
});
```

The output of the above code will be an object containing the request parameters, for example:

```
{ name: 'John', age: '30', email: 'john@example.com' }
```

The `express.urlencoded` middleware function takes an optional object as a parameter. The `extended` property of this object can be set to `true` to use the [qs module](https://www.npmjs.com/package/qs) for parsing the request parameters.

## Helpful links

- [Express.js Middleware Documentation](https://expressjs.com/en/guide/using-middleware.html)
- [Express.js `express.urlencoded` Middleware Documentation](https://expressjs.com/en/api.html#express.urlencoded)
- [qs Module Documentation](https://www.npmjs.com/package/qs)

onelinerhub: [How do I use Express.js to parse request parameters?](https://onelinerhub.com/expressjs/how-do-i-use-express-js-to-parse-request-parameters)