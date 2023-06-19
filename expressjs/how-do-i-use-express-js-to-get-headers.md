# How do I use Express.js to get headers?
// plain

Express.js is a web application framework for Node.js. It can be used to get headers from incoming requests. Here is an example of how to do this:

```
const express = require('express')
const app = express()

app.get('/', (req, res) => {
  const headers = req.headers
  console.log(headers)
  res.send('Headers received')
})

app.listen(3000)
```

This example code will create an Express.js server that will log the headers from incoming requests and respond with the message `Headers received`.

The code consists of the following parts:

1. `const express = require('express')` - This line imports the Express.js module.
2. `const app = express()` - This line creates an Express.js application.
3. `app.get('/', (req, res) => {` - This line creates a route handler for the `GET` request to the root URL.
4. `const headers = req.headers` - This line retrieves the headers from the incoming request.
5. `console.log(headers)` - This line logs the headers to the console.
6. `res.send('Headers received')` - This line sends the response `Headers received` to the client.
7. `app.listen(3000)` - This line starts the Express.js server on port 3000.

For more information about Express.js, see the [documentation](https://expressjs.com/en/api.html).

onelinerhub: [How do I use Express.js to get headers?](https://onelinerhub.com/expressjs/how-do-i-use-express-js-to-get-headers)