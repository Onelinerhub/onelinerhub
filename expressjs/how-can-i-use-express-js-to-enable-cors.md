# How can I use Express.js to enable CORS?
// plain

Enabling Cross-Origin Resource Sharing (CORS) in Express.js is easy. CORS is a mechanism that allows resources on a web page to be requested from another domain outside the domain from which the resource originated.

To enable CORS in Express.js, you need to install the cors package from npm:

```
npm install cors
```

Then, you need to require the cors module in your main Express.js file:

```
const cors = require('cors');
```

Finally, you need to add the cors() middleware to your Express.js application:

```
app.use(cors());
```

This will enable CORS for all routes in your Express.js application. If you only want to enable CORS for specific routes, you can use the cors() middleware with the routes you want to enable CORS for:

```
app.get('/someRoute', cors(), (req, res) => {
  // Your route code here
});
```

This will enable CORS only for the specified route.

## Code explanation


1. `npm install cors` - Installs the cors package from npm.
2. `const cors = require('cors');` - Imports the cors module.
3. `app.use(cors());` - Adds the cors() middleware to the Express.js application.
4. `app.get('/someRoute', cors(), (req, res) => {` - Adds the cors() middleware to the specified route.

## Helpful links

- [Express.js CORS Documentation](https://expressjs.com/en/resources/middleware/cors.html)
- [MDN CORS Documentation](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)

onelinerhub: [How can I use Express.js to enable CORS?](https://onelinerhub.com/expressjs/how-can-i-use-express-js-to-enable-cors)