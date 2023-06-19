# parser

How do I use the Express.js JSON body parser?
// plain

The Express.js JSON body parser is a middleware that parses incoming requests with JSON payloads and is based on body-parser. It is used to parse the body of an incoming request and make it available as a JavaScript object.

To use the Express.js JSON body parser, first install it using npm:
```
npm install body-parser
```

Then, import it into the application and use the `json` method to enable the middleware:
```
const bodyParser = require('body-parser')

app.use(bodyParser.json())
```

The `json` method will parse the body of the incoming request and make it available as a JavaScript object in the `req.body` property. This object can then be used in the application logic.

Parts of the code:
- `npm install body-parser`: Installs the body-parser middleware from npm.
- `const bodyParser = require('body-parser')`: Imports the body-parser middleware into the application.
- `app.use(bodyParser.json())`: Enables the middleware and makes the body of the request available as a JavaScript object in the `req.body` property.

## Helpful links
- [Express.js Documentation](https://expressjs.com/en/4x/api.html#req.body)
- [body-parser Documentation](https://www.npmjs.com/package/body-parser)

onelinerhub: [parser

How do I use the Express.js JSON body parser?](https://onelinerhub.com/expressjs/parser--how-do-i-use-the-express-js-json-body-parser)