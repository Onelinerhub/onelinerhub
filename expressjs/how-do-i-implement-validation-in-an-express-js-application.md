# How do I implement validation in an Express.js application?
// plain

Validation is an important part of any application, and Express.js makes it easy to implement. Here's an example of how to do it in an Express.js application:

```
const express = require('express')
const app = express()

app.use(express.json()) // This line is necessary

app.post('/user', (req, res) => {
  const { name, age } = req.body

  if (!name || !age) {
    return res.status(400).json({ error: 'Name and age are required' })
  }

  res.json({ name, age })
})
```

The `express.json()` line is necessary to parse the body of the request into a JavaScript object. Then, the code checks if the `name` and `age` fields are present in the request body, and if they're not, it returns an error response.

## Code explanation

- `const express = require('express')` - importing the Express.js library
- `const app = express()` - creating an Express.js application
- `app.use(express.json())` - parsing the body of the request into a JavaScript object
- `if (!name || !age)` - checking if the `name` and `age` fields are present in the request body
- `return res.status(400).json({ error: 'Name and age are required' })` - returning an error response if either `name` or `age` is not present
- `res.json({ name, age })` - sending a response with the `name` and `age` fields if they are present in the request body

## Helpful links
- [Express.js Documentation](https://expressjs.com/en/4x/api.html)
- [Using Middleware](https://expressjs.com/en/guide/using-middleware.html)

onelinerhub: [How do I implement validation in an Express.js application?](https://onelinerhub.com/expressjs/how-do-i-implement-validation-in-an-express-js-application)