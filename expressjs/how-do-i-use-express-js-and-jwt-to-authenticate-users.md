# How do I use Express.js and JWT to authenticate users?
// plain

To use Express.js and JWT to authenticate users, you will need to do the following steps:

1. Install the jsonwebtoken and express-jwt packages:
```
$ npm install jsonwebtoken express-jwt
```

2. Create a JWT secret key:
```
const jwtSecret = 'your_secret_key';
```

3. Create a middleware to check the JWT:
```
const jwtCheck = expressJwt({
    secret: jwtSecret
});
```

4. Use the middleware to protect routes:
```
app.get('/protected', jwtCheck, (req, res) => {
    res.send('Protected route');
});
```

5. Generate a JWT token:
```
const token = jwt.sign({ userId: 123 }, jwtSecret);
```

6. Pass the token to the client:
```
res.send({
    token: token
});
```

7. On subsequent requests, the client should include the token in the Authorization header:
```
Authorization: Bearer <token>
```

## Helpful links
- [jsonwebtoken](https://www.npmjs.com/package/jsonwebtoken)
- [express-jwt](https://www.npmjs.com/package/express-jwt)

onelinerhub: [How do I use Express.js and JWT to authenticate users?](https://onelinerhub.com/expressjs/how-do-i-use-express-js-and-jwt-to-authenticate-users)