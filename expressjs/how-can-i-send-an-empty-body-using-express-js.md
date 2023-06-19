# How can I send an empty body using Express.js?
// plain

To send an empty body using Express.js, you can use the `send()` method. This method allows you to send an empty body response to the client. Here is an example of how to use it:

```js
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send();
});

app.listen(3000, () => {
  console.log('Server running on port 3000');
});
```

This will send an empty body response to the client.

The code above consists of the following parts:

1. `const express = require('express');` - This line imports the Express.js module.
2. `const app = express();` - This line creates an Express.js application.
3. `app.get('/', (req, res) => {` - This line creates a route handler for a GET request to the root path.
4. `res.send();` - This line sends an empty body response to the client.
5. `app.listen(3000, () => {` - This line starts the server on port 3000.

For more information, refer to the [Express.js Documentation](https://expressjs.com/en/4x/api.html#res.send).

onelinerhub: [How can I send an empty body using Express.js?](https://onelinerhub.com/expressjs/how-can-i-send-an-empty-body-using-express-js)