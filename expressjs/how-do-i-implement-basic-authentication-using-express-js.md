# How do I implement basic authentication using Express.js?
// plain

To implement basic authentication using Express.js, you will need to use the `express.basicAuth()` middleware. This middleware takes two parameters: a username and password. It will then check the incoming request to see if the username and password match what is provided. If they do, the request will be allowed to continue, otherwise an authentication error will be returned.

## Example code

```
app.use(express.basicAuth(function(user, pass) {
    return user === 'username' && pass === 'password';
}));
```

The code above will setup basic authentication for the Express.js application. It will check to see if the username and password provided in the request match the ones provided in the function. If they do, the request will be allowed to continue, otherwise an authentication error will be returned.

## Code explanation

- `express.basicAuth()` - This is the middleware that will be used to setup basic authentication for the Express.js application.
- `user` - This is the username that is passed in the request.
- `pass` - This is the password that is passed in the request.
- `user === 'username' && pass === 'password'` - This is the logic that will be used to check if the username and password provided in the request match the ones provided in the function.

## Helpful links
- [Express.js Basic Authentication](https://expressjs.com/en/guide/using-middleware.html#middleware.basic-auth)
- [Basic Authentication in Node.js](https://www.sitepoint.com/basic-authentication-in-node-js/)

onelinerhub: [How do I implement basic authentication using Express.js?](https://onelinerhub.com/expressjs/how-do-i-implement-basic-authentication-using-express-js)