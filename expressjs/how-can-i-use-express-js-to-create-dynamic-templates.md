# How can I use Express.js to create dynamic templates?
// plain

Express.js is a web application framework for Node.js that can be used to create dynamic templates. It allows you to define routes, which are URLs that your application responds to, and render HTML pages based on the response from the routes.

For example, the following code block can be used to create a dynamic template in Express.js:

```
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send(`
    <html>
      <body>
        <h1>Hello World!</h1>
      </body>
    </html>
  `);
});

app.listen(3000, () => console.log('Server started'));
```

This code will create a server listening on port 3000 and will respond to the '/' route with a simple HTML page displaying the text "Hello World!".

The code consists of the following parts:

1. `const express = require('express');` - This line imports the Express.js module.
2. `const app = express();` - This line creates a new Express.js application.
3. `app.get('/', (req, res) => { ... })` - This line defines a route for the application. It will respond to requests for the '/' route with the code block inside the arrow function.
4. `res.send(` ... `)` - This line sends a response to the client. The response is a string containing an HTML page.
5. `app.listen(3000, () => console.log('Server started'));` - This line starts the server, listening on port 3000.

For more information on Express.js, please refer to the [documentation](https://expressjs.com/en/api.html).

onelinerhub: [How can I use Express.js to create dynamic templates?](https://onelinerhub.com/expressjs/how-can-i-use-express-js-to-create-dynamic-templates)