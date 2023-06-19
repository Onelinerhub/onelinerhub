# How do I use Express.js to fetch data?
// plain

Express.js is a web application framework for Node.js that enables developers to easily create web applications. It provides a simple and powerful API for fetching data from a server.

To use Express.js to fetch data, we can use the `fetch` API. Here is an example code:

```javascript
const express = require('express');
const app = express();

app.get('/data', (req, res) => {
  fetch('http://example.com/data.json')
    .then(response => response.json())
    .then(data => res.json(data));
});

app.listen(3000);
```

This code will fetch data from `http://example.com/data.json` and send it back as a response to the client.

The code consists of the following parts:

1. `const express = require('express');` - This line imports the Express.js module.
2. `const app = express();` - This line creates an Express.js application.
3. `app.get('/data', (req, res) => { ... });` - This line defines a route for the application which will fetch data when the `/data` URL is requested.
4. `fetch('http://example.com/data.json')` - This line fetches the data from the specified URL.
5. `.then(response => response.json())` - This line parses the response as JSON.
6. `.then(data => res.json(data))` - This line sends the parsed data as a response to the client.
7. `app.listen(3000);` - This line starts the server on port 3000.

For more information, please refer to the [Express.js documentation](https://expressjs.com/en/api.html#express).

onelinerhub: [How do I use Express.js to fetch data?](https://onelinerhub.com/expressjs/how-do-i-use-express-js-to-fetch-data)