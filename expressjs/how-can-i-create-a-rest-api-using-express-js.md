# How can I create a REST API using Express.js?
// plain

Creating a REST API using Express.js is a straightforward process. Here is an example of a basic API that responds to a `GET` request at the `/hello` route:

```javascript
const express = require('express');
const app = express();

app.get('/hello', (req, res) => {
  res.send('Hello World!');
});

app.listen(3000, () => {
  console.log('Server started');
});
```

## Output example

```
Server started
```

The code above consists of four parts:
1. Requiring the Express.js library: `const express = require('express');`
2. Creating an Express.js application: `const app = express();`
3. Defining a route and a callback function to respond to a `GET` request: `app.get('/hello', (req, res) => { ... });`
4. Starting the server and listening on port 3000: `app.listen(3000, () => { ... });`

For more information on creating a REST API using Express.js, please refer to the [official Express.js documentation](https://expressjs.com/en/guide/routing.html).

onelinerhub: [How can I create a REST API using Express.js?](https://onelinerhub.com/expressjs/how-can-i-create-a-rest-api-using-express-js)