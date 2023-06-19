# How do I use the Express.js template engine to create dynamic HTML pages?
// plain

Express.js template engine is a popular and powerful tool for creating dynamic HTML pages. It allows developers to use JavaScript code to generate HTML pages with dynamic content. Here is an example of how to use the Express.js template engine:

```
// Require the Express.js template engine
const express = require('express');

// Create an Express.js application
const app = express();

// Set the view engine to use the Express.js template engine
app.set('view engine', 'ejs');

// Define the view path
app.set('views', './views');

// Create a route to render the view
app.get('/', (req, res) => {
  // Render the view with dynamic data
  res.render('index', {
    message: 'Hello World'
  });
});

// Listen for requests
app.listen(3000);
```

The example code above will create a server on port 3000 that will render the view `index.ejs` with the dynamic data `{ message: 'Hello World' }`. The view `index.ejs` should look like this:

```
<h1><%= message %></h1>
```

The output of the example code above is an HTML page with the message `Hello World` rendered in an `<h1>` tag.

Parts of the example code explained:

- `const express = require('express');` - Require the Express.js template engine.
- `const app = express();` - Create an Express.js application.
- `app.set('view engine', 'ejs');` - Set the view engine to use the Express.js template engine.
- `app.set('views', './views');` - Define the view path.
- `res.render('index', { message: 'Hello World' });` - Render the view with dynamic data.

## Helpful links

- [Express.js Template Engine](https://expressjs.com/en/guide/using-template-engines.html)
- [Express.js Documentation](https://expressjs.com/en/4x/api.html#res.render)

onelinerhub: [How do I use the Express.js template engine to create dynamic HTML pages?](https://onelinerhub.com/expressjs/how-do-i-use-the-express-js-template-engine-to-create-dynamic-html-pages)