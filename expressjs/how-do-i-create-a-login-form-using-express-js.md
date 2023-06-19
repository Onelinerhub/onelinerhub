# How do I create a login form using Express.js?
// plain

Creating a login form using Express.js is easy. Below is an example code block that will generate a basic login form.

```
// Require the Express Module
var express = require('express');

// Create an Express App
var app = express();

// Require body-parser (to receive post data from clients)
var bodyParser = require('body-parser');

// Integrate body-parser with our App
app.use(bodyParser.urlencoded({ extended: true }));

// Require path
var path = require('path');

// Setting our Static Folder Directory
app.use(express.static(path.join(__dirname, './static')));

// Setting our Views Folder Directory
app.set('views', path.join(__dirname, './views'));

// Setting our View Engine set to EJS
app.set('view engine', 'ejs');

// Routes
// Root Request
app.get('/', function(req, res) {
    // This is where we will retrieve the users from the database and include them in the view page we will be rendering.
    res.render('index');
})

// Add User Request
app.post('/users', function(req, res) {
    console.log("POST DATA", req.body);
    // This is where we would add the user from req.body to the database.
    res.redirect('/');
})

// Setting our Server to Listen on Port: 8000
app.listen(8000, function() {
    console.log("listening on port 8000");
})
```

This code will generate a basic login form with a route for posting the login data. The code consists of the following parts:

1. Require the Express Module: This line imports the Express module into the program.
2. Create an Express App: This line creates an instance of an Express App.
3. Require body-parser: This line imports the body-parser module, which is used to receive post data from clients.
4. Integrate body-parser with the App: This line integrates the body-parser module with the Express App.
5. Require path: This line imports the path module, which is used to access the directory of the program.
6. Setting our Static Folder Directory: This line sets the directory where the static files are stored.
7. Setting our Views Folder Directory: This line sets the directory where the view files are stored.
8. Setting our View Engine set to EJS: This line sets the view engine to EJS.
9. Routes: This section contains the routes for the program, including the root request and the add user request.
10. Setting our Server to Listen on Port: This line sets the port for the server to listen on.

## Helpful links
- [Express.js Official Documentation](https://expressjs.com/en/api.html)
- [body-parser Official Documentation](https://www.npmjs.com/package/body-parser)

onelinerhub: [How do I create a login form using Express.js?](https://onelinerhub.com/expressjs/how-do-i-create-a-login-form-using-express-js)