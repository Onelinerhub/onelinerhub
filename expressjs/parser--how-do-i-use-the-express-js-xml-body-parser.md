# parser

How do I use the Express.js XML body parser?
// plain

The Express.js XML body parser is used to parse XML data sent in an HTTP request body and make it available to your application. It is built on top of the [xml2js](https://www.npmjs.com/package/xml2js) library and is available as an npm package.

To use the Express.js XML body parser, you first need to install it using npm:

```
$ npm install body-parser
```

Then you need to add the parser to your Express.js app:

```javascript
const express = require('express')
const bodyParser = require('body-parser')

const app = express()

// parse application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: false }))

// parse application/xml
app.use(bodyParser.xml())
```

Once the parser is added to your app, you can access the parsed XML data in the `req.body` object in your route handler. For example, if the request body contains the following XML data:

```xml
<person>
  <name>John Doe</name>
  <age>30</age>
</person>
```

Then you can access the data in your route handler like this:

```javascript
app.post('/', (req, res) => {
  const { name, age } = req.body.person
  console.log(name, age) // John Doe, 30
})
```

For more information, see the [Express.js documentation](https://expressjs.com/en/guide/using-middleware.html#middleware.body-parser).

onelinerhub: [parser

How do I use the Express.js XML body parser?](https://onelinerhub.com/expressjs/parser--how-do-i-use-the-express-js-xml-body-parser)