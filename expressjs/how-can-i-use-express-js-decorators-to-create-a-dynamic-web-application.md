# How can I use Express.js decorators to create a dynamic web application?
// plain

Express.js decorators allow developers to create a dynamic web application with ease. The decorators provide a way to dynamically change the behavior of an application without changing the code.

For example, the following code uses the `express.decorate()` decorator to add a `/hello` route to the application.

```
const express = require('express')
const app = express()

app.decorate('hello', (req, res) => {
  res.send('Hello World!')
})

app.listen(3000, () => {
  console.log('Server running on port 3000')
})
```

## Output example

```
Server running on port 3000
```

The code above adds a `/hello` route to the application. When a request is made to the `/hello` route, the `express.decorate()` decorator will execute the function and send the response `Hello World!`.

The decorator can also be used to add dynamic behavior to the application. For example, the following code uses the `express.decorate()` decorator to add a `/user` route with dynamic behavior.

```
app.decorate('user', (req, res) => {
  let userId = req.params.userId
  res.send(`User ${userId}`)
})
```

When a request is made to the `/user/:userId` route, the `express.decorate()` decorator will execute the function and send the response `User {userId}` where `{userId}` is the value of the `userId` parameter.

By using Express.js decorators, developers can easily create a dynamic web application.

## Helpful links
- [Express.js Decorators](https://expressjs.com/en/api.html#express.decorate)
- [Express.js Routing](https://expressjs.com/en/guide/routing.html)

onelinerhub: [How can I use Express.js decorators to create a dynamic web application?](https://onelinerhub.com/expressjs/how-can-i-use-express-js-decorators-to-create-a-dynamic-web-application)