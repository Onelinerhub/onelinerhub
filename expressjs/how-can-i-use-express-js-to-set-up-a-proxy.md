# How can I use Express.js to set up a proxy?
// plain

Express.js can be used to set up a proxy by using its `proxy` middleware. This middleware allows you to proxy HTTP requests to other servers. The following example code shows how to use the `proxy` middleware to proxy requests to an API server:

```
const express = require('express');
const proxy = require('express-http-proxy');

const app = express();

app.use('/api', proxy('http://api.example.com'));

app.listen(3000, () => console.log('Proxy server listening on port 3000'));
```

The code above will start a proxy server on port 3000 that will proxy all requests to `/api` to `http://api.example.com`.

The `proxy` middleware takes two arguments:

1. The target URL to proxy requests to.
2. An options object (optional).

The options object can contain various settings to customize the proxy request, such as setting the timeout, or setting a custom proxy header.

For more information about the `proxy` middleware, please see the [Express.js documentation](https://expressjs.com/en/4x/api.html#app.use).

onelinerhub: [How can I use Express.js to set up a proxy?](https://onelinerhub.com/expressjs/how-can-i-use-express-js-to-set-up-a-proxy)