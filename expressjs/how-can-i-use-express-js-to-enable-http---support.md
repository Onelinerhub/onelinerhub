# How can I use Express.js to enable HTTP/2 support?
// plain

Express.js is a popular web application framework for Node.js that can be used to enable HTTP/2 support. To do so, you will need to use the `spdy` module, which is included in the Express.js installation.

Here is an example of how to enable HTTP/2 support in Express.js:

```javascript
const express = require('express');
const spdy = require('spdy');

const app = express();

spdy
  .createServer({
    key: fs.readFileSync('server.key'),
    cert: fs.readFileSync('server.crt')
  }, app)
  .listen(3000, (error) => {
    if (error) {
      console.error(error);
      return process.exit(1);
    } else {
      console.log('Listening on port: 3000.');
    }
  });
```

This code will create an HTTPS server on port 3000 using the `server.key` and `server.crt` files. It will also enable HTTP/2 support for the Express.js application.

## Code explanation


* `const express = require('express')` - This imports the Express.js module.
* `const spdy = require('spdy')` - This imports the `spdy` module which is used to enable HTTP/2 support.
* `const app = express()` - This creates an Express.js application.
* `spdy.createServer()` - This creates an HTTPS server and enables HTTP/2 support.
* `key: fs.readFileSync('server.key')` - This provides the server key which is used to create the HTTPS server.
* `cert: fs.readFileSync('server.crt')` - This provides the server certificate which is used to create the HTTPS server.
* `listen()` - This starts the server on the specified port.

Here is a list of ## Helpful links

* [Express.js Documentation](https://expressjs.com/en/4x/api.html)
* [Node.js Documentation](https://nodejs.org/api/http2.html)
* [HTTP/2 Documentation](https://http2.github.io/)

onelinerhub: [How can I use Express.js to enable HTTP/2 support?](https://onelinerhub.com/expressjs/how-can-i-use-express-js-to-enable-http---support)