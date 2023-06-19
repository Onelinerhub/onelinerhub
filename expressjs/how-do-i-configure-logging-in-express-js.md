# How do I configure logging in Express.js?
// plain

Express.js provides a simple and easy way to configure logging. Here is an example of how to configure logging in Express.js:

```
const express = require('express');
const logger = require('morgan');

const app = express();

// Configure logging
app.use(logger('dev'));

// Other Express.js settings

app.listen(3000);
```

This will enable logging with the [morgan](https://www.npmjs.com/package/morgan) middleware. The logger middleware is configured with the `dev` format, which is a predefined format to log requests in the Apache combined log format.

The `logger` middleware takes a format string as its first argument. This string can have the following parts:

* `:method` - HTTP request method
* `:url` - Requested URL
* `:status` - HTTP response status code
* `:response-time` - Time in milliseconds to process the request
* `:date` - Date of the request
* `:referrer` - Referrer URL
* `:user-agent` - Browser user agent

For more information, see the [Express.js documentation](https://expressjs.com/en/guide/writing-middleware.html#logging-requests).

onelinerhub: [How do I configure logging in Express.js?](https://onelinerhub.com/expressjs/how-do-i-configure-logging-in-express-js)