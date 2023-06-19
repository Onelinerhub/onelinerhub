# How do I create a REST API with Express.js?
// plain

Creating a REST API with Express.js is relatively simple. The following example code shows how to create a basic API with two endpoints: `GET /hello` and `POST /hello`.

```javascript
const express = require('express')
const app = express()

app.get('/hello', (req, res) => {
  res.send('Hello World!')
})

app.post('/hello', (req, res) => {
  res.send('You just called the post method at "/hello"')
})

app.listen(3000)
```

The code above will create an Express.js server listening on port 3000. When a `GET` request is sent to `/hello`, it will respond with `Hello World!` and when a `POST` request is sent to `/hello`, it will respond with `You just called the post method at "/hello"`.

The code above includes the following parts:

- `const express = require('express')`: This imports the Express.js module.
- `const app = express()`: This creates an Express.js application.
- `app.get('/hello', (req, res) => {...})`: This creates a `GET` endpoint at `/hello`.
- `app.post('/hello', (req, res) => {...})`: This creates a `POST` endpoint at `/hello`.
- `app.listen(3000)`: This starts the server and makes it listen on port 3000.

For more information on creating a REST API with Express.js, see the following links:

- [Express.js Documentation](https://expressjs.com/)
- [Building a RESTful API with Node.js and Express](https://www.sitepoint.com/building-a-restful-api-with-node-js-and-express/)

onelinerhub: [How do I create a REST API with Express.js?](https://onelinerhub.com/expressjs/how-do-i-create-a-rest-api-with-express-js)