# How can I use Express.js to prevent XSS attacks?
// plain

XSS (Cross-site Scripting) attacks are a type of malicious code injection that can be used to steal user data, hijack user sessions, and perform other malicious activities. Express.js provides a few methods to help prevent XSS attacks.

1. Sanitizing Input: Express.js provides the `express-validator` package which can be used to sanitize user input. This package provides functions such as `escape()` and `sanitizeBody()` which can be used to prevent malicious code from being injected into the application.

```
const { check, validationResult } = require('express-validator');

app.post('/login', [
  check('username').escape(),
  check('password').escape()
], (req, res) => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(422).json({ errors: errors.array() });
  }
  // Handle login
});
```

2. Content Security Policy (CSP): Express.js also provides the `helmet` package which can be used to set a `Content-Security-Policy` header. This header can be used to specify which sources are allowed to load resources, such as scripts, stylesheets, and images.

```
const helmet = require('helmet');

app.use(helmet.contentSecurityPolicy({
  directives: {
    defaultSrc: ["'self'"],
    scriptSrc: ["'self'", "'unsafe-inline'"],
    styleSrc: ["'self'", "'unsafe-inline'"],
    imgSrc: ["'self'", "data:"],
  }
}));
```

3. X-XSS-Protection: Express.js also provides the `helmet` package which can be used to set an `X-XSS-Protection` header. This header can be used to enable the browser's built-in XSS protection.

```
const helmet = require('helmet');

app.use(helmet.xssFilter());
```

These are just a few of the methods that Express.js provides to help prevent XSS attacks. For more information, see the [Express.js security guide](https://expressjs.com/en/advanced/best-practice-security.html).

onelinerhub: [How can I use Express.js to prevent XSS attacks?](https://onelinerhub.com/expressjs/how-can-i-use-express-js-to-prevent-xss-attacks)