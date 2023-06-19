# How do I use Express.js to create a YouTube clone?
// plain

Using Express.js to create a YouTube clone involves creating a Node.js server that serves HTML and JavaScript files to the client. The server should also handle AJAX requests to an API endpoint which is used to interact with the data store.

The following example code creates a basic Express.js server that serves a HTML file with a `/` route:

```js
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.sendFile('index.html', { root: __dirname });
});

app.listen(3000, () => {
  console.log('Server started on port 3000');
});
```

## Output example


```
Server started on port 3000
```

## Code explanation


* `const express = require('express');` - Imports the Express.js library.
* `const app = express();` - Creates an Express.js application.
* `app.get('/', (req, res) => { ... });` - Creates a route handler for the `/` route that serves a HTML file.
* `app.listen(3000, () => { ... });` - Starts the server on port 3000.

## Helpful links

* [Express.js Docs](https://expressjs.com/en/4x/api.html)
* [Node.js Docs](https://nodejs.org/en/docs/)

onelinerhub: [How do I use Express.js to create a YouTube clone?](https://onelinerhub.com/expressjs/how-do-i-use-express-js-to-create-a-youtube-clone)