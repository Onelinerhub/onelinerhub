# How can I use an Express.js JSON parser?
// plain

An Express.js JSON parser can be used to parse JSON data from an HTTP request. This is done by using the `express.json()` middleware. The middleware will parse the body of the request and make the data available in `req.body`.

For example, if you have an HTTP request with a JSON body, you can use the following code to parse the data:

```
const express = require('express')
const app = express()

app.use(express.json())

app.post('/', (req, res) => {
  console.log(req.body)
})
```

This will output the parsed JSON object in the console.

The `express.json()` middleware has some additional options that can be passed as an object to the middleware function. These options include:

- `limit`: The maximum size of the request body in bytes
- `type`: An array of allowed content types
- `verify`: A function to verify the request body

For more information, refer to the [Express.js documentation](https://expressjs.com/en/api.html#express.json).

onelinerhub: [How can I use an Express.js JSON parser?](https://onelinerhub.com/expressjs/how-can-i-use-an-express-js-json-parser)