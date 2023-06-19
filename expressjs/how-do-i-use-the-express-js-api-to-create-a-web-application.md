# How do I use the Express.js API to create a web application?
// plain

To create a web application using Express.js API, you need to install the Express.js framework and its dependencies. After installation, you can create an Express.js application using the following code:

```
const express = require('express')
const app = express()

app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.listen(3000, () => console.log('Server running on port 3000'))
```

This code will create a web application that will listen on port 3000 and will respond with "Hello World!" when it receives a GET request on the root URL.

The code contains the following parts:

1. The `require('express')` statement imports the Express.js library and assigns it to the `express` variable.
2. The `express()` statement creates an Express.js application and assigns it to the `app` variable.
3. The `app.get()` statement sets up a route handler for the root URL.
4. The `res.send()` statement sends a response with the given string.
5. The `app.listen()` statement starts the web server and listens on the given port.

## Output example


```
Server running on port 3000
```

## Helpful links

- [Express.js Documentation](https://expressjs.com/en/api.html)
- [Getting Started with Express.js](https://expressjs.com/en/starter/installing.html)

onelinerhub: [How do I use the Express.js API to create a web application?](https://onelinerhub.com/expressjs/how-do-i-use-the-express-js-api-to-create-a-web-application)