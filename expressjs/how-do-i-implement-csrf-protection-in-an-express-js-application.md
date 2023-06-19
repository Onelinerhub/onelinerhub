# How do I implement CSRF protection in an Express.js application?
// plain

To implement CSRF protection in an Express.js application, you can use the [csurf](https://www.npmjs.com/package/csurf) middleware. It provides easy-to-use protection against Cross-Site Request Forgery attacks.

First, install the csurf package:

```
npm install csurf
```

Then, require the package in your app and use it as a middleware:

```javascript
const csrf = require('csurf');
const csrfProtection = csrf({ cookie: true });

app.use(csrfProtection);
```

The `csrfProtection` middleware will add a `req.csrfToken()` function to the request, which can be used to create the CSRF token. This token should be added as a hidden field to all forms in the application:

```javascript
<input type="hidden" name="_csrf" value="<%= csrfToken %>">
```

Finally, the middleware will check the token on all requests and reject the request if the token is invalid.

Links:
- [csurf](https://www.npmjs.com/package/csurf)
- [Express.js CSRF Protection](https://expressjs.com/en/advanced/best-practice-security.html#use-csrf-protection)

onelinerhub: [How do I implement CSRF protection in an Express.js application?](https://onelinerhub.com/expressjs/how-do-i-implement-csrf-protection-in-an-express-js-application)