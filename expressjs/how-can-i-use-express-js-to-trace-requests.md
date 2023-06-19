# How can I use Express.js to trace requests?
// plain

Express.js is a popular web application framework for Node.js. It can be used to trace requests by using the `app.use` middleware. This middleware allows you to intercept every incoming request and log the request information.

For example, the following code block will log the request method, URL, and timestamp for every incoming request:

```
const express = require('express')
const app = express()

app.use((req, res, next) => {
    console.log(`${req.method} ${req.url} - ${Date.now()}`)
    next()
})

// ...
```

## Output example


```
GET / - 1567885313863
```

The code above consists of three parts:

1. `const express = require('express')` - This imports the Express.js module.
2. `app.use((req, res, next) => {...})` - This is the middleware that intercepts the request and logs the request information. `req` contains information about the incoming request, `res` contains information about the response, and `next` is a function that must be called to continue to the next middleware.
3. `console.log(...)` - This logs the request method, URL, and timestamp.

For more information about Express.js middleware, please refer to the following link:

[Express.js Middleware Guide](https://expressjs.com/en/guide/using-middleware.html)

onelinerhub: [How can I use Express.js to trace requests?](https://onelinerhub.com/expressjs/how-can-i-use-express-js-to-trace-requests)