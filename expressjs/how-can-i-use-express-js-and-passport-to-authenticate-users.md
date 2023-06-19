# How can I use Express.js and Passport to authenticate users?
// plain

Express.js and Passport can be used together to authenticate users. Passport is an authentication middleware for Node.js that works with Express.js. It provides a simple way to authenticate users with username and password, OAuth tokens, and other authentication methods.

To use Express.js and Passport to authenticate users, you will need to install and configure Passport. After that, you can use Passport's authentication strategies to authenticate users. Here is an example code block of how to use Passport's LocalStrategy to authenticate users with username and password:

```js
const passport = require('passport');
const LocalStrategy = require('passport-local').Strategy;

passport.use(new LocalStrategy(
  function(username, password, done) {
    User.findOne({ username: username }, function (err, user) {
      if (err) { return done(err); }
      if (!user) {
        return done(null, false, { message: 'Incorrect username.' });
      }
      if (!user.validPassword(password)) {
        return done(null, false, { message: 'Incorrect password.' });
      }
      return done(null, user);
    });
  }
));
```

This code block will authenticate a user with a username and password. It will check if the username and password are correct and return a user object if they are correct.

## Code explanation


1. `const passport = require('passport');`: This imports the Passport module.
2. `const LocalStrategy = require('passport-local').Strategy;`: This imports the Passport LocalStrategy module.
3. `passport.use(new LocalStrategy(`: This creates a new LocalStrategy.
4. `function(username, password, done) {`: This is the callback function that will be called when a user attempts to authenticate. It takes in the username, password, and a done callback.
5. `User.findOne({ username: username }, function (err, user) {`: This will search for a user with the given username.
6. `if (err) { return done(err); }`: This will return an error if one occurs.
7. `if (!user) {`: This will check if a user was found.
8. `return done(null, false, { message: 'Incorrect username.' });`: This will return an error message if the username is incorrect.
9. `if (!user.validPassword(password)) {`: This will check if the password is correct.
10. `return done(null, false, { message: 'Incorrect password.' });`: This will return an error message if the password is incorrect.
11. `return done(null, user);`: This will return the user object if the username and password are correct.

## Helpful links

- [Passport.js Documentation](http://www.passportjs.org/docs/)
- [Express.js Documentation](https://expressjs.com/en/4x/api.html)

onelinerhub: [How can I use Express.js and Passport to authenticate users?](https://onelinerhub.com/expressjs/how-can-i-use-express-js-and-passport-to-authenticate-users)