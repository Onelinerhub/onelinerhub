# How can I use HTTPS with Express.js?
// plain

HTTPS (Hypertext Transfer Protocol Secure) is a secure protocol that can be used to protect communication between a web server and a client. Express.js is a popular web framework for Node.js which provides an easy way to set up HTTPS.

Here is an example of how to set up HTTPS with Express.js:

```
const express = require('express');
const https = require('https');
const fs = require('fs');

const app = express();

// set up the HTTPS server
const httpsOptions = {
  key: fs.readFileSync('server.key'),
  cert: fs.readFileSync('server.cert')
};

const server = https.createServer(httpsOptions, app);

server.listen(443);
```

The code above sets up an HTTPS server with Express.js. It requires two files, `server.key` and `server.cert`, which are the server's private key and certificate. It then creates an HTTPS server using the options and the Express app, and listens on port 443.

## Code explanation


1. `const express = require('express');` - Require the Express.js module.
2. `const https = require('https');` - Require the HTTPS module.
3. `const fs = require('fs');` - Require the file system module.
4. `const app = express();` - Create an Express.js app.
5. `const httpsOptions = {...};` - Create an options object containing the server's private key and certificate.
6. `const server = https.createServer(httpsOptions, app);` - Create an HTTPS server using the options and the Express app.
7. `server.listen(443);` - Listen on port 443.

For more information, see the [Express.js documentation](https://expressjs.com/en/guide/behind-proxies.html#configuring-https-and-http2).

onelinerhub: [How can I use HTTPS with Express.js?](https://onelinerhub.com/expressjs/how-can-i-use-https-with-express-js)