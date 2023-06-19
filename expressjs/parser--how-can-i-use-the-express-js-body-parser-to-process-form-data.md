# parser

How can I use the Express.js body parser to process form data?
// plain

The Express.js body parser is a middleware that parses incoming request bodies in a middleware before your handlers, available under the req.body property. It is used to process form data, and can be used to parse both application/x-www-form-urlencoded and multipart/form-data formats.

To use the body parser, you must first install it:

```
npm install --save body-parser
```

Once installed, you can use it in your Express.js application. For example, if you have a form with a text field and a submit button, you can use the body parser to process the form data:

```
const express = require('express')
const bodyParser = require('body-parser')

const app = express()

// parse application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: false }))

// parse application/json
app.use(bodyParser.json())

app.post('/form', (req, res) => {
  const formData = req.body
  console.log(formData) // { text: 'some text' }
  res.send('Form data processed!')
})
```

The code above will parse the form data (sent as application/x-www-form-urlencoded or application/json) and make it available in the req.body object.

Parts of the code above:
- `npm install --save body-parser` - command to install the body-parser package
- `app.use(bodyParser.urlencoded({ extended: false }))` - use the body parser to parse application/x-www-form-urlencoded data
- `app.use(bodyParser.json())` - use the body parser to parse application/json data
- `const formData = req.body` - access the parsed form data from the req.body object

## Helpful links
- [Express.js body parser documentation](https://expressjs.com/en/resources/middleware/body-parser.html)
- [npm body-parser package page](https://www.npmjs.com/package/body-parser)

onelinerhub: [parser

How can I use the Express.js body parser to process form data?](https://onelinerhub.com/expressjs/parser--how-can-i-use-the-express-js-body-parser-to-process-form-data)