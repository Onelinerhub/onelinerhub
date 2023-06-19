# How can I use Express.js to handle a request?
// plain

Express.js is a web application framework for Node.js that simplifies the process of handling requests. To use Express.js to handle a request, you need to create a server and define the routes.

## Example code

```
// Include the Express.js library
const express = require('express');

// Create an Express.js server
const app = express();

// Define the route
app.get('/', (req, res) => {
  res.send('Hello World!');
});

// Start the server
app.listen(3000, () => {
  console.log('Server listening on port 3000');
});
```

## Output example

```
Server listening on port 3000
```

The code consists of the following parts:

1. `const express = require('express');` - This line includes the Express.js library.
2. `const app = express();` - This line creates an Express.js server.
3. `app.get('/', (req, res) => {` - This line defines the route for the request.
4. `res.send('Hello World!');` - This line sends a response to the request.
5. `app.listen(3000, () => {` - This line starts the server on port 3000.

## Helpful links

- [Express.js](https://expressjs.com/)
- [Node.js](https://nodejs.org/)

onelinerhub: [How can I use Express.js to handle a request?](https://onelinerhub.com/expressjs/how-can-i-use-express-js-to-handle-a-request)