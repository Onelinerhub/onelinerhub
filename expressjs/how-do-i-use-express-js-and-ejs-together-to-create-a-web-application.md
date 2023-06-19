# How do I use Express.js and EJS together to create a web application?
// plain

Express.js and EJS can be used together to create a web application. EJS is a templating language that allows you to render dynamic HTML pages with JavaScript. Express.js is a web application framework for Node.js that simplifies the process of creating web applications.

Below is an example of how to use Express.js and EJS together to create a web application:

```javascript
// Import Express.js and EJS
const express = require('express');
const ejs = require('ejs');

// Create an Express.js app
const app = express();

// Use EJS as the view engine
app.set('view engine', 'ejs');

// Set up a route to the home page
app.get('/', function(req, res) {
  res.render('home');
});

// Start the server on port 3000
app.listen(3000, function() {
  console.log('Server is running on port 3000');
});
```

## Output example

```
Server is running on port 3000
```

## Code explanation

- `require('express')`: Imports the Express.js library.
- `require('ejs')`: Imports the EJS library.
- `const app = express()`: Creates an Express.js app.
- `app.set('view engine', 'ejs')`: Sets EJS as the view engine.
- `app.get('/', function(req, res) { ... })`: Sets up a route to the home page.
- `app.listen(3000, function() { ... })`: Starts the server on port 3000.

## Helpful links
- [Express.js](https://expressjs.com/)
- [EJS](https://ejs.co/)

onelinerhub: [How do I use Express.js and EJS together to create a web application?](https://onelinerhub.com/expressjs/how-do-i-use-express-js-and-ejs-together-to-create-a-web-application)