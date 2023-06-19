# How do I use Express.js to read the body of a request?
// plain

Express.js is a web application framework for Node.js that allows you to create web applications. One of the things you can do with Express.js is read the body of a request. To do this, you need to use the `body-parser` middleware. Here is an example of how to use it:

```javascript
const express = require('express')
const bodyParser = require('body-parser')

const app = express()

// parse application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: false }))

// parse application/json
app.use(bodyParser.json())

app.post('/', (req, res) => {
  console.log(req.body)
})
```

This example sets up the `body-parser` middleware to parse both `application/x-www-form-urlencoded` and `application/json` data. Then, when a `POST` request is made to `/`, the body of the request is printed to the console.

The `body-parser` middleware can also be used to read data from `PUT` and `DELETE` requests.

## Code explanation

1. `const express = require('express')`: This line imports the Express.js module.
2. `const bodyParser = require('body-parser')`: This line imports the `body-parser` middleware.
3. `app.use(bodyParser.urlencoded({ extended: false }))`: This line sets up the `body-parser` middleware to parse `application/x-www-form-urlencoded` data.
4. `app.use(bodyParser.json())`: This line sets up the `body-parser` middleware to parse `application/json` data.
5. `app.post('/', (req, res) => { console.log(req.body) })`: This line sets up a `POST` route that will print the body of the request to the console.

## Helpful links
- [Express.js Documentation](https://expressjs.com/en/guide/routing.html)
- [body-parser Documentation](https://www.npmjs.com/package/body-parser)

onelinerhub: [How do I use Express.js to read the body of a request?](https://onelinerhub.com/expressjs/how-do-i-use-express-js-to-read-the-body-of-a-request)