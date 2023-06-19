# How can I use Next.js and Express.js together?
// plain

Next.js and Express.js can be used together to create a powerful web application.

To do so, you will need to create a server.js file in the root of your Next.js project. This file will contain the Express.js code that will handle the requests and responses.

## Example code

```
const express = require('express');
const next = require('next');

const dev = process.env.NODE_ENV !== 'production';
const app = next({ dev });
const handle = app.getRequestHandler();

app.prepare().then(() => {
  const server = express();

  server.get('*', (req, res) => {
    return handle(req, res);
  });

  server.listen(3000, err => {
    if (err) throw err;
    console.log('> Ready on http://localhost:3000');
  });
});
```

This code will create an Express server that will handle all requests with the Next.js request handler.

## Code explanation

- `const express = require('express');` - This imports the Express.js library.
- `const next = require('next');` - This imports the Next.js library.
- `const dev = process.env.NODE_ENV !== 'production';` - This sets the environment to development.
- `const app = next({ dev });` - This creates an instance of Next.js with the environment set to development.
- `const handle = app.getRequestHandler();` - This creates a handler that will handle the requests.
- `app.prepare().then(() => { ... });` - This prepares the Next.js app and then runs the code inside the callback.
- `server.get('*', (req, res) => { ... });` - This sets up a route that will handle all requests with the handler created earlier.
- `server.listen(3000, err => { ... });` - This starts the Express server on port 3000.

## Helpful links
- [Next.js Documentation](https://nextjs.org/docs)
- [Express.js Documentation](https://expressjs.com/en/api.html)

onelinerhub: [How can I use Next.js and Express.js together?](https://onelinerhub.com/expressjs/how-can-i-use-next-js-and-express-js-together)