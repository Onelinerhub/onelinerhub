# How do I use an Express.js HTML template?
// plain

Using an Express.js HTML template is a simple process. Here is an example of how to do it:

```
// Require the Express.js module
const express = require('express');

// Create an Express.js app
const app = express();

// Set the view engine to use HTML
app.set('view engine', 'html');

// Set the path to the HTML template
app.set('views', __dirname + '/views');

// Render the HTML template
app.get('/', (req, res) => {
  res.render('index');
});

// Start the Express.js server
app.listen(3000, () => {
  console.log('Listening on port 3000!');
});
```

## Code explanation


1. `const express = require('express');` - require the Express.js module
2. `const app = express();` - create an Express.js app
3. `app.set('view engine', 'html');` - set the view engine to use HTML
4. `app.set('views', __dirname + '/views');` - set the path to the HTML template
5. `res.render('index');` - render the HTML template
6. `app.listen(3000, () => {` - start the Express.js server

## Helpful links
- [Express.js Documentation](https://expressjs.com/en/4x/api.html)
- [Express.js View System](https://expressjs.com/en/guide/using-template-engines.html)

onelinerhub: [How do I use an Express.js HTML template?](https://onelinerhub.com/expressjs/how-do-i-use-an-express-js-html-template)