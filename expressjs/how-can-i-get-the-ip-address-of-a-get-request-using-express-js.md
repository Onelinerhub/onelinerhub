# How can I get the IP address of a GET request using Express.js?
// plain

To get the IP address of a GET request using Express.js, you can use the `req.ip` property. This property will return the IP address of the request.

For example:

```javascript
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  console.log(req.ip);
  res.send('Hello World!');
});

app.listen(3000, () => console.log('Server started'));
```

## Output example

```
Server started
```

The code above will print the IP address of the request to the console.

## Code explanation


1. `require('express')` - This imports the Express.js library into the application.
2. `app.get('/', (req, res) => {...})` - This defines a route handler for GET requests to the root path.
3. `console.log(req.ip)` - This prints the IP address of the request to the console.
4. `res.send('Hello World!')` - This sends a response to the client.

## Helpful links
- [Express.js Documentation](https://expressjs.com/en/4x/api.html#req)

onelinerhub: [How can I get the IP address of a GET request using Express.js?](https://onelinerhub.com/expressjs/how-can-i-get-the-ip-address-of-a-get-request-using-express-js)