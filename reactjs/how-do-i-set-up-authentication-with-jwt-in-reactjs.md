# How do I set up authentication with JWT in ReactJS?
// plain

Setting up authentication with JWT in ReactJS involves a few steps. Firstly, create an API endpoint to generate the JWT token when the user logs in, and a middleware to validate the token for each request. The following example code block creates a login API endpoint with Express.js:

```
app.post('/login', (req, res) => {
  const username = req.body.username;
  const password = req.body.password;

  // Authenticate the user
  if (username === 'demo' && password === 'demo') {
    const token = jwt.sign({
      username: username
    }, 'secret');
    res.json({
      token: token
    });
  } else {
    res.sendStatus(401);
  }
});
```

Then, use the `use` method of the `axios` module to set the header with the JWT token for each request. The following example code block sets the header for all requests:

```
axios.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    config.headers.Authorization =  token ? `Bearer ${token}` : '';
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);
```

Finally, create a middleware to validate the JWT token on the server side. The following example code block validates the token with Express.js:

```
app.use(function(req, res, next) {
  const token = req.headers['authorization'];
  if (token) {
    jwt.verify(token, 'secret', function(err, decoded) {
      if (err) {
        return res.json({
          success: false,
          message: 'Failed to authenticate token.'
        });
      } else {
        req.decoded = decoded;
        next();
      }
    });
  } else {
    return res.status(403).send({
      success: false,
      message: 'No token provided.'
    });
  }
});
```

In summary, setting up authentication with JWT in ReactJS involves:

1. Creating an API endpoint to generate the JWT token when the user logs in
2. Setting the header with the JWT token for each request
3. Creating a middleware to validate the JWT token on the server side

## Helpful links

- [JWT Authentication with Node.js](https://jwt.io/introduction/)
- [Axios interceptors](https://github.com/axios/axios#interceptors)

onelinerhub: [How do I set up authentication with JWT in ReactJS?](https://onelinerhub.com/reactjs/how-do-i-set-up-authentication-with-jwt-in-reactjs)