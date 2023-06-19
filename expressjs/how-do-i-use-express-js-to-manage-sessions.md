# How do I use Express.js to manage sessions?
// plain

Express.js is a web application framework for Node.js that provides a range of features to help manage sessions. It can be used to store and retrieve session data between requests.

Here is an example of how to use Express.js to manage sessions:

```javascript
// Initialize the session middleware
const session = require('express-session');
app.use(session({
  secret: 'my-secret',
  resave: false,
  saveUninitialized: true
}));

// Store session data
app.get('/session', (req, res) => {
  req.session.myData = { name: 'John Doe' };
  res.send('Session data stored');
});

// Retrieve session data
app.get('/session', (req, res) => {
  const myData = req.session.myData;
  res.send(`Retrieved data: ${myData.name}`);
});
```

## Output example


`Retrieved data: John Doe`

The code above demonstrates how to use Express.js to manage sessions. It initializes the session middleware with a secret, which is required for session data encryption, and sets the `resave` and `saveUninitialized` options. It then stores and retrieves session data using the `req.session` object.

#### List of Code Parts with Explanation

* `const session = require('express-session');` - This imports the `express-session` module, which enables session management.

* `app.use(session({ secret: 'my-secret', resave: false, saveUninitialized: true }));` - This initializes the session middleware with a secret, which is required for session data encryption, and sets the `resave` and `saveUninitialized` options.

* `req.session.myData = { name: 'John Doe' };` - This stores data in the session object.

* `const myData = req.session.myData;` - This retrieves data from the session object.

#### Relevant Links

* [Express.js Session Documentation](https://expressjs.com/en/resources/middleware/session.html)
* [Express.js Guide](https://expressjs.com/en/guide/using-middleware.html)

onelinerhub: [How do I use Express.js to manage sessions?](https://onelinerhub.com/expressjs/how-do-i-use-express-js-to-manage-sessions)