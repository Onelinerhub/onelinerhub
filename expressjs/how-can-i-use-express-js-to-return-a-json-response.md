# How can I use Express.js to return a JSON response?
// plain

Express.js is a web application framework for Node.js that provides a simple way to return a JSON response. To use Express.js to return a JSON response, you need to set up your server, create a route to handle the request, and send the response in JSON format.

For example:

```
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send({
    message: 'Hello World!'
  });
});

app.listen(3000);
```

The above code will create a server and listen on port 3000. When a request is sent to the `/` path, the server will respond with a JSON object containing a message.

The code consists of the following parts:

1. `const express = require('express');` - This imports the Express.js library.
2. `const app = express();` - This creates an Express.js application.
3. `app.get('/', (req, res) => { ... });` - This creates a route that will handle requests sent to the `/` path.
4. `res.send({ ... });` - This sends a JSON response containing the message `Hello World!`.

For more information, see the [Express.js documentation](https://expressjs.com/en/4x/api.html#res.send).

onelinerhub: [How can I use Express.js to return a JSON response?](https://onelinerhub.com/expressjs/how-can-i-use-express-js-to-return-a-json-response)