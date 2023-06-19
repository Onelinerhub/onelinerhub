# How can I use Node.js and Express together to create a web application?
// plain

Node.js and Express can be used together to create a web application. Express is a web application framework for Node.js that provides a set of features to help build web applications. The following example code block shows how to use Express to create a web application:

```
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.listen(3000, () => {
  console.log('Example app listening on port 3000!');
});
```

The output of the example code block would be:
```
Example app listening on port 3000!
```

## Code explanation


1. `const express = require('express');` - This line requires the Express module, which is used to create the web application.

2. `const app = express();` - This line creates an Express application instance.

3. `app.get('/', (req, res) => {` - This line creates a route handler for a GET request to the root path of the application.

4. `res.send('Hello World!');` - This line sends a response to the client with the message "Hello World!".

5. `app.listen(3000, () => {` - This line starts the Express application and listens for requests on port 3000.

6. `console.log('Example app listening on port 3000!');` - This line logs a message to the console when the Express application is ready to handle requests.

## Helpful links

- [Node.js](https://nodejs.org/en/)
- [Express](https://expressjs.com/)

onelinerhub: [How can I use Node.js and Express together to create a web application?](https://onelinerhub.com/expressjs/how-can-i-use-node-js-and-express-together-to-create-a-web-application)