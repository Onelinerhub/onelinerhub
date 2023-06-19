# How can I use Express.js and Keycloak together to secure an application?
// plain

Express.js and Keycloak can be used together to secure an application by implementing authentication and authorization. The following steps should be taken:

1. Install Keycloak server and create a realm, client, and user.
2. Install the Keycloak Node.js adapter and configure it to connect to the Keycloak server.
3. Add the Keycloak middleware to the Express.js application.

## Example code

```javascript
const express = require('express');
const session = require('express-session');
const Keycloak = require('keycloak-connect');

const app = express();
const memoryStore = new session.MemoryStore();
const keycloak = new Keycloak({ store: memoryStore });

app.use(session({
  secret: 'some secret',
  resave: false,
  saveUninitialized: true,
  store: memoryStore
}));

app.use(keycloak.middleware());
```

4. Protect the Express.js routes that require authentication.

## Example code

```javascript
app.get('/secured', keycloak.protect(), (req, res) => {
  res.json({
    message: 'This is a secured route.'
  });
});
```

5. Use Keycloak to manage user roles and access rights.

## Example code

```javascript
app.get('/admin', keycloak.protect('realm:admin'), (req, res) => {
  res.json({
    message: 'This route is only accessible to users with the admin role.'
  });
});
```

6. Log out the user when the session ends.

## Example code

```javascript
app.get('/logout', (req, res) => {
  req.session.destroy(() => {
    req.logout();
    res.redirect('/');
  });
});
```

7. Start the Express.js application.

## Example code

```javascript
app.listen(3000, () => {
  console.log('Server is running on port 3000');
});
```

## Output example

```
Server is running on port 3000
```

## Helpful links
- [Keycloak Node.js Adapter](https://www.keycloak.org/docs/latest/securing_apps/index.html#_nodejs_adapter)
- [Protecting Routes with Keycloak Middleware](https://www.keycloak.org/docs/latest/securing_apps/index.html#_nodejs_protect_routes)

onelinerhub: [How can I use Express.js and Keycloak together to secure an application?](https://onelinerhub.com/expressjs/how-can-i-use-express-js-and-keycloak-together-to-secure-an-application)