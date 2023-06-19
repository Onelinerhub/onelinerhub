# How do I use Express.js to create the next route?
// plain

Express.js is a web application framework for Node.js used to create web applications and APIs. To create a route using Express.js, you need to first require the Express module, create an Express application, and then use the `app.METHOD()` function to create the route.

For example, to create a GET route for the path `/example`, you would use the following code:

```
const express = require('express');
const app = express();

app.get('/example', (req, res) => {
  res.send('This is an example route!');
});
```

The output of the code above would be `This is an example route!` when a GET request is made to `/example`.

## Code explanation


* `const express = require('express');` - This line requires the Express module.
* `const app = express();` - This line creates an Express application.
* `app.get('/example', (req, res) => {` - This line creates a GET route for the path `/example`.
* `res.send('This is an example route!');` - This line sends a response with the message `This is an example route!` when a GET request is made to `/example`.

## Helpful links

* [Express.js](https://expressjs.com/)
* [Creating a Basic Express.js App](https://expressjs.com/en/starter/hello-world.html)

onelinerhub: [How do I use Express.js to create the next route?](https://onelinerhub.com/expressjs/how-do-i-use-express-js-to-create-the-next-route)