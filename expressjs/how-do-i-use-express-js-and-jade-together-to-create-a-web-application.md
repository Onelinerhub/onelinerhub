# How do I use Express.js and Jade together to create a web application?
// plain

Express.js and Jade can be used together to create a web application. Express.js is a Node.js web application framework that provides a robust set of features for web and mobile applications. Jade is a templating language for Node.js that is used to generate HTML markup.

The following example code shows how Express.js and Jade can be used together to create a web application:

```
// Require Express.js
var express = require('express');

// Create an Express.js application
var app = express();

// Set view engine to Jade
app.set('view engine', 'jade');

// Create a route for the application
app.get('/', function (req, res) {
  // Render a Jade view
  res.render('index');
});

// Start the server
app.listen(3000);
```

This code will create a web application that will render a Jade view when the root route is accessed.

## Code explanation


- `var express = require('express')`: This line requires the Express.js module.
- `var app = express()`: This line creates an Express.js application.
- `app.set('view engine', 'jade')`: This line sets the view engine to Jade.
- `app.get('/', function (req, res) { ... })`: This line creates a route for the application, and will be called when the root route is accessed.
- `res.render('index')`: This line renders a Jade view.
- `app.listen(3000)`: This line starts the server.

## Helpful links
- [Express.js Documentation](https://expressjs.com/en/4x/api.html)
- [Jade Documentation](http://jade-lang.com/reference/)

onelinerhub: [How do I use Express.js and Jade together to create a web application?](https://onelinerhub.com/expressjs/how-do-i-use-express-js-and-jade-together-to-create-a-web-application)