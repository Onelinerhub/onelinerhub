# How do I create a route in Express.js?
// plain

Creating routes in Express.js is a simple process. Here is an example of creating a route:

```
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.listen(3000, () => {
  console.log('Server started on port 3000');
});
```

## Output example

```
Server started on port 3000
```

The code consists of four parts:

1. Require the Express.js module: `const express = require('express')`
2. Create an Express.js application instance: `const app = express()`
3. Create a route handler for the route path: `app.get('/', (req, res) => { ... })`
4. Start the server: `app.listen(3000, () => { ... })`

The first two parts of the code are necessary for all Express.js applications. The third part is where the route is created. The route path is provided as the first argument and the route handler is provided as the second argument. The route handler is a function that is called when the route is requested. In this example, the route handler sends a response with the text `Hello World!`. The fourth part of the code starts the server on port 3000.

For more information about creating routes in Express.js, see the [documentation](https://expressjs.com/en/guide/routing.html).

onelinerhub: [How do I create a route in Express.js?](https://onelinerhub.com/expressjs/how-do-i-create-a-route-in-express-js)