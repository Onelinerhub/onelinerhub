# How can I use Express.js to parse JSON data?
// plain

Express.js is a web application framework for Node.js that makes it easier to create web applications and APIs. It can be used to parse JSON data in a few different ways.

1. Using `body-parser` middleware:

```javascript
const express = require('express')
const bodyParser = require('body-parser')

const app = express()

// parse application/json
app.use(bodyParser.json())

app.post('/', (req, res) => {
  const data = req.body
  console.log(data)
  // { name: 'John', age: 30 }
})
```

2. Using `express.json()` middleware:

```javascript
const express = require('express')

const app = express()

// parse application/json
app.use(express.json())

app.post('/', (req, res) => {
  const data = req.body
  console.log(data)
  // { name: 'John', age: 30 }
})
```

3. Using `express.text()` middleware:

```javascript
const express = require('express')

const app = express()

// parse application/json
app.use(express.text())

app.post('/', (req, res) => {
  const data = JSON.parse(req.body)
  console.log(data)
  // { name: 'John', age: 30 }
})
```

- `body-parser` is a third-party middleware library that can be used to parse incoming request bodies.
- `express.json()` is a built-in middleware that can be used to parse incoming request bodies in JSON format.
- `express.text()` is a built-in middleware that can be used to parse incoming request bodies in plain text format.

## Helpful links

- [Express.js Documentation](https://expressjs.com/en/4x/api.html#req)
- [body-parser Documentation](https://www.npmjs.com/package/body-parser)

onelinerhub: [How can I use Express.js to parse JSON data?](https://onelinerhub.com/expressjs/how-can-i-use-express-js-to-parse-json-data)