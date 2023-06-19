# How do I set up Express.js JWT authentication?
// plain

To set up Express.js JWT authentication, you need to install the jsonwebtoken package first, then create a secret key to sign the token, and then create a middleware to verify the token.

1. Install the jsonwebtoken package:
```
npm install jsonwebtoken
```

2. Create a secret key to sign the token:
```
const secret = 'supersecret';
```

3. Create a middleware to verify the token:
```
const verifyToken = (req, res, next) => {
  const token = req.headers['x-access-token'];
  if (!token) {
    return res.status(403).send({
      auth: false,
      message: 'No token provided.'
    });
  }
  jwt.verify(token, secret, (err, decoded) => {
    if (err) {
      return res.status(500).send({
        auth: false,
        message: 'Failed to authenticate token.'
      });
    }
    // If everything is good, save to request for use in other routes
    req.userId = decoded.id;
    next();
  });
};
```

4. Use the middleware in the routes that need authentication:
```
app.get('/protected', verifyToken, (req, res) => {
  res.send('Access granted.');
});
```

For more details, please refer to [this guide](https://medium.com/@siddharthac6/json-web-token-jwt-the-right-way-of-implementing-with-node-js-65b8915d550e).

<br>

## Code explanation
**

1. Install the jsonwebtoken package:
```
npm install jsonwebtoken
```
This command installs the jsonwebtoken package to your project.

2. Create a secret key to sign the token:
```
const secret = 'supersecret';
```
This code creates a secret key to sign the token.

3. Create a middleware to verify the token:
```
const verifyToken = (req, res, next) => {
  const token = req.headers['x-access-token'];
  if (!token) {
    return res.status(403).send({
      auth: false,
      message: 'No token provided.'
    });
  }
  jwt.verify(token, secret, (err, decoded) => {
    if (err) {
      return res.status(500).send({
        auth: false,
        message: 'Failed to authenticate token.'
      });
    }
    // If everything is good, save to request for use in other routes
    req.userId = decoded.id;
    next();
  });
};
```
This code creates a middleware to verify the token. It first checks if the token exists in the request header, and then verifies the token with the secret key. If the token is verified, it will save the decoded token to the request for use in other routes.

4. Use the middleware in the routes that need authentication:
```
app.get('/protected', verifyToken, (req, res) => {
  res.send('Access granted.');
});
```
This code uses the middleware in the routes that need authentication. When the token is verified, it will send a response of "Access granted".

onelinerhub: [How do I set up Express.js JWT authentication?](https://onelinerhub.com/expressjs/how-do-i-set-up-express-js-jwt-authentication)