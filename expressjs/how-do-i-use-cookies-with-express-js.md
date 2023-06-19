# How do I use cookies with Express.js?
// plain

Cookies are small pieces of data stored in the browser of a user that can be used to identify the user and enable user-specific functionality in the application. Express.js provides a middleware to handle cookie-based authentication.

To use cookies with Express.js, first install the cookie-parser middleware:

```
npm install cookie-parser
```

Then, add the cookie-parser middleware to your Express.js application:

```javascript
const express = require('express');
const cookieParser = require('cookie-parser');

const app = express();
app.use(cookieParser());
```

Now, you can set and get cookies from the request and response objects:

```javascript
// Set cookie
res.cookie('name', 'value', { maxAge: 3600 });

// Get cookie
const name = req.cookies.name;
```

The code above sets a cookie with the name `name` and the value `value` that will expire after one hour. You can also use the cookie-parser middleware to sign and verify cookies.

## Helpful links

- [Cookie-Parser](https://www.npmjs.com/package/cookie-parser)
- [Express.js Cookies](https://expressjs.com/en/resources/middleware/cookie-parser.html)

onelinerhub: [How do I use cookies with Express.js?](https://onelinerhub.com/expressjs/how-do-i-use-cookies-with-express-js)