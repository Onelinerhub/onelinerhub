# How can I use Express.js to yield results?
// plain

Express.js is a web application framework for Node.js. It makes it easy to create web applications and APIs. It can be used to yield results by handling requests and providing responses.

Below is an example of a simple Express.js application that yields a response when a request is made to the root path:

```
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.listen(3000, () => {
  console.log('Server started');
});

```

## Output example

```
Server started
```

The example code consists of the following parts:

1. The `require` statement imports the Express.js module.
2. The `app` variable holds an instance of the Express.js application.
3. The `app.get()` method defines a route and a callback function that will be executed when the route is requested.
4. The `res.send()` method sends a response with the specified content.
5. The `app.listen()` method starts the server and listens for requests on the specified port.

## Helpful links

- [Express.js official website](https://expressjs.com/)
- [Express.js guide](https://expressjs.com/en/guide/routing.html)

onelinerhub: [How can I use Express.js to yield results?](https://onelinerhub.com/expressjs/how-can-i-use-express-js-to-yield-results)