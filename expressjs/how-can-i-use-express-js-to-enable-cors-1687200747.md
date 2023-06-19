# How can I use Express.js to enable CORS?
// plain

CORS (Cross-Origin Resource Sharing) is a mechanism that uses additional HTTP headers to tell a browser to let a web application running at one origin (domain) have permission to access selected resources from a server at a different origin.

Using Express.js, you can enable CORS with various options. The simplest way is to use the `cors` package from npm.

```
$ npm install cors
```

Then, require the package and use it with Express:

```
const express = require('express')
const cors = require('cors')
const app = express()

app.use(cors())
```

The `cors()` function can also take an options object as an argument. This object can contain various settings, such as `origin`, `methods`, `allowedHeaders`, `credentials`, etc.

```
app.use(cors({
  origin: 'http://example.com',
  methods: ['GET', 'POST'],
  allowedHeaders: ['Content-Type', 'Authorization']
}))
```

For more information, see [the CORS documentation](https://expressjs.com/en/resources/middleware/cors.html) on the Express website.

You can also find more information on [MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS).

onelinerhub: [How can I use Express.js to enable CORS?](https://onelinerhub.com/expressjs/how-can-i-use-express-js-to-enable-cors-1687200747)