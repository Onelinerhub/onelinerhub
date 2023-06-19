# How do I use Express.js to send HTML?
// plain

Express.js is a web application framework for Node.js. It is used to create web applications and APIs. It can be used to serve HTML pages to the client.

Here is an example of how to use Express.js to send HTML:

```
// Require the Express module
const express = require('express');

// Create a new Express application
const app = express();

// Serve an HTML page
app.get('/', (req, res) => {
  res.send(`
    <html>
      <head>
        <title>My Page</title>
      </head>
      <body>
        <h1>Hello World!</h1>
      </body>
    </html>
  `);
});

// Start the server
app.listen(3000, () => {
  console.log('Server started on port 3000');
});
```

The output of the above code will be:

```
Server started on port 3000
```

This code does the following:

1. Requires the Express module
2. Creates a new Express application
3. Serves an HTML page with a `GET` request
4. Starts the server on port 3000

## Helpful links

- [Express.js Documentation](https://expressjs.com/en/starter/installing.html)
- [Node.js Documentation](https://nodejs.org/en/docs/)

onelinerhub: [How do I use Express.js to send HTML?](https://onelinerhub.com/expressjs/how-do-i-use-express-js-to-send-html)