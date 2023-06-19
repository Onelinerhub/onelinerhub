# How do I use Express.js to create a web application?
// plain

Express.js is a web application framework for Node.js. It is designed to make creating web applications easy and fast. It is used to create routes, handle requests, and render HTML pages, as well as many other features. Here is an example of how to use Express.js to create a web application:

```
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.listen(3000, () => console.log('Example app listening on port 3000!'));
```

## Output example

```
Example app listening on port 3000!
```

This code consists of the following parts:

1. `const express = require('express');` - This line imports the Express.js module.
2. `const app = express();` - This line creates an Express application.
3. `app.get('/', (req, res) => {` - This line creates a route for the application. It will handle requests to the root URL.
4. `res.send('Hello World!');` - This line sends a response with the text "Hello World!"
5. `app.listen(3000, () => console.log('Example app listening on port 3000!'));` - This line starts the server on port 3000.

For more information on Express.js, please see the following links:

- [Express.js Official Website](https://expressjs.com/)
- [Express.js Guide](https://expressjs.com/en/guide/routing.html)
- [Express.js API Reference](https://expressjs.com/en/4x/api.html)

onelinerhub: [How do I use Express.js to create a web application?](https://onelinerhub.com/expressjs/how-do-i-use-express-js-to-create-a-web-application)