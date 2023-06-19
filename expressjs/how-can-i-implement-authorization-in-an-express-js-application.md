# How can I implement authorization in an Express.js application?
// plain

Authorization in an Express.js application can be implemented by using the Express.js middleware Passport.js. Passport.js provides a simple way to implement authentication and authorization in an Express.js application.

Below is an example of how to use Passport.js in an Express.js application:

```javascript
const passport = require('passport');
const express = require('express');
const app = express();

// Initialize Passport
app.use(passport.initialize());

// Set up a route to handle authentication
app.get('/auth/google', passport.authenticate('google', {
  scope: ['profile', 'email']
}));

// Set up a route to handle the callback
app.get('/auth/google/callback', passport.authenticate('google', {
  successRedirect: '/',
  failureRedirect: '/login'
}));
```

In the example code above:

1. The `passport` module is imported.
2. The `passport.initialize()` middleware is used to initialize Passport.
3. The `passport.authenticate()` middleware is used to authenticate the user with the Google OAuth2 service.
4. The `successRedirect` and `failureRedirect` options are used to redirect the user to the appropriate page after authentication.

For more information about using Passport.js in an Express.js application, see the [Passport.js documentation](http://www.passportjs.org/docs/).

onelinerhub: [How can I implement authorization in an Express.js application?](https://onelinerhub.com/expressjs/how-can-i-implement-authorization-in-an-express-js-application)