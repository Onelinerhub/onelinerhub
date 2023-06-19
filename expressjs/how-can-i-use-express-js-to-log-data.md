# How can I use Express.js to log data?
// plain

Express.js is a web application framework for Node.js. It is designed to make creating web applications easier and faster. One way to use Express.js is to log data. Here is an example of how to do this:

```
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  console.log('Logging data...');
  res.send('Hello World!');
});

app.listen(3000, () => console.log('Server started'));
```
## Output example

```
Server started
```

This example code uses Express.js to create a web application that logs data when a user visits the root page. It starts by importing the Express.js library and creating an Express application. Then, it defines a route for the root page, which logs a message to the console and sends a response to the user. Finally, it starts the application on port 3000.

## Code explanation

- `const express = require('express')`: imports the Express.js library.
- `const app = express()`: creates an Express application.
- `app.get('/', (req, res) => {...})`: defines a route for the root page.
- `console.log('Logging data...')`: logs a message to the console.
- `res.send('Hello World!')`: sends a response to the user.
- `app.listen(3000, () => console.log('Server started'))`: starts the application on port 3000.

## Helpful links
- [Express.js official website](https://expressjs.com/)
- [Express.js documentation](https://expressjs.com/en/4x/api.html)

onelinerhub: [How can I use Express.js to log data?](https://onelinerhub.com/expressjs/how-can-i-use-express-js-to-log-data)