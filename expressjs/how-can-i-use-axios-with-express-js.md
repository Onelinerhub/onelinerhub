# How can I use Axios with Express.js?
// plain

Axios is a popular, promise-based HTTP client that can be used in both the browser and in Node.js. It can be used with Express.js to make HTTP requests to external services.

Here is an example of how to use Axios with Express.js:

```js
const express = require('express');
const axios = require('axios');

const app = express();

app.get('/api/users', (req, res) => {
  axios.get('https://jsonplaceholder.typicode.com/users')
    .then(response => {
      res.json(response.data);
    })
    .catch(err => {
      res.status(500).send(err);
    });
});

app.listen(3000);
```

This example will make a GET request to the [JSONPlaceholder API](https://jsonplaceholder.typicode.com/) for a list of users and return the response in JSON format.

The code consists of the following parts:

1. Require the Express and Axios modules:

```js
const express = require('express');
const axios = require('axios');
```

2. Create an Express server instance:

```js
const app = express();
```

3. Create an endpoint that makes a GET request to the JSONPlaceholder API and returns the response in JSON:

```js
app.get('/api/users', (req, res) => {
  axios.get('https://jsonplaceholder.typicode.com/users')
    .then(response => {
      res.json(response.data);
    })
    .catch(err => {
      res.status(500).send(err);
    });
});
```

4. Start the server:

```js
app.listen(3000);
```

onelinerhub: [How can I use Axios with Express.js?](https://onelinerhub.com/expressjs/how-can-i-use-axios-with-express-js)