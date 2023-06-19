# How can I use Express.js with React to develop a web application?
// plain

Express.js is a web application framework for Node.js. It can be used to develop web applications with React. Here is an example of how to do so:

```javascript
const express = require('express');
const app = express();
const React = require('react');
const ReactDOMServer = require('react-dom/server');

app.get('/', (req, res) => {
  const html = ReactDOMServer.renderToString(
    <h1>Hello World</h1>
  );
  res.send(html);
});

app.listen(3000, () => {
  console.log('server started');
});
```

This example code will create a server on port 3000 and render a React component to the response when a request is made to the root path.

## Code explanation


1. `const express = require('express');` - This line imports the Express.js module
2. `const app = express();` - This line creates an Express.js application instance
3. `const React = require('react');` - This line imports the React module
4. `const ReactDOMServer = require('react-dom/server');` - This line imports the ReactDOMServer module
5. `app.get('/', (req, res) => { ... });` - This line sets up a route handler for the root path
6. `const html = ReactDOMServer.renderToString(<h1>Hello World</h1>);` - This line renders a React component to a string
7. `res.send(html);` - This line sends the rendered component as the response
8. `app.listen(3000, () => { ... });` - This line starts the server on port 3000

## Helpful links

- [Express.js Docs](https://expressjs.com/en/4x/api.html)
- [React Docs](https://reactjs.org/docs/getting-started.html)

onelinerhub: [How can I use Express.js with React to develop a web application?](https://onelinerhub.com/expressjs/how-can-i-use-express-js-with-react-to-develop-a-web-application)