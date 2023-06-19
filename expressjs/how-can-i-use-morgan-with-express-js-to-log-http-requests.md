# How can I use Morgan with Express.js to log HTTP requests?
// plain

Morgan is a popular HTTP request logger middleware for Node.js and Express.js. It can be used to log detailed information about incoming HTTP requests, including the request method, URL, status code, response time, and more.

To use Morgan with Express.js, you can install it with the following command:

```
$ npm install morgan
```

Then, you can require it in your Express.js app and add it as middleware:

```javascript
const express = require('express');
const morgan = require('morgan');

const app = express();

// Log all requests
app.use(morgan('combined'));

// Your routes and other Express.js middleware

app.listen(3000);
```

The `morgan()` function takes a single argument, which is a string that specifies the log format. In the example above, we used the `combined` format, which gives detailed information about the request.

Here is an example output from the `combined` format:

```
::1 - - [19/Apr/2020:13:53:20 +0000] "GET / HTTP/1.1" 200 1234 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
```

The parts of the log entry are as follows:

- `::1` - The IP address of the client
- `-` - The user ID (not available)
- `-` - The user authentication (not available)
- `[19/Apr/2020:13:53:20 +0000]` - The timestamp
- `"GET / HTTP/1.1"` - The request method and URL
- `200` - The HTTP status code
- `1234` - The response time in milliseconds
- `"-"` - The referrer (not available)
- `"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"` - The user agent

For more information about Morgan and the available log formats, see the [documentation](https://github.com/expressjs/morgan).

onelinerhub: [How can I use Morgan with Express.js to log HTTP requests?](https://onelinerhub.com/expressjs/how-can-i-use-morgan-with-express-js-to-log-http-requests)