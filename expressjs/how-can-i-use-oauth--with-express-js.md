# How can I use OAuth2 with Express.js?
// plain

OAuth2 is a protocol that allows users to authorize third-party applications to access their information without having to share their passwords. Express.js is a web application framework for Node.js that can be used to create OAuth2 authentication endpoints. Here's an example of how to use OAuth2 with Express.js:

```
const express = require('express');
const oauth2 = require('simple-oauth2');

const app = express();

// Create OAuth2 client
const oauth2Client = oauth2.create({
  client: {
    id: 'YOUR_CLIENT_ID',
    secret: 'YOUR_CLIENT_SECRET',
  },
  auth: {
    tokenHost: 'https://example.com',
    tokenPath: '/oauth/token',
    authorizePath: '/oauth/authorize',
  },
});

// Generate authorization URI
const authorizationUri = oauth2Client.authorizationCode.authorizeURL({
  redirect_uri: 'http://localhost:3000/callback',
  scope: 'read',
  state: 'random_state_string',
});

// Redirect user to authorization URI
app.get('/', (req, res) => {
  res.redirect(authorizationUri);
});

// Callback service parsing the authorization code and asking for the access token
app.get('/callback', async (req, res) => {
  const code = req.query.code;
  const options = {
    code,
  };

  try {
    const result = await oauth2Client.authorizationCode.getToken(options);
    const accessToken = oauth2Client.accessToken.create(result);
    console.log(accessToken);
  } catch (error) {
    console.error('Access Token Error', error.message);
    res.status(500).json('Authentication failed');
  }
});

app.listen(3000, () => {
  console.log('Express server started on port 3000');
});
```

The example code above will:

1. Require the Express.js and OAuth2 modules.
2. Create an Express.js app.
3. Create an OAuth2 client with the provided client ID and secret.
4. Generate an authorization URI with the provided redirect URI, scope, and state.
5. Redirect the user to the authorization URI.
6. Parse the authorization code from the callback URL and request an access token.
7. Log the access token to the console.

## Helpful links

- [Express.js Documentation](https://expressjs.com/en/api.html)
- [Simple OAuth2 Documentation](https://github.com/lelylan/simple-oauth2)

onelinerhub: [How can I use OAuth2 with Express.js?](https://onelinerhub.com/expressjs/how-can-i-use-oauth--with-express-js)