# How can I use Express.js and Node.js together to create a web application?
// plain

Express.js and Node.js can be used together to create a web application by writing server-side logic in JavaScript.

The following example code shows how to use Express.js and Node.js together to create a simple web application.

```
// Import Express.js
const express = require('express');

// Create an Express.js app
const app = express();

// Define a route
app.get('/', (req, res) => {
  res.send('Hello World!');
});

// Start the server
app.listen(3000, () => {
  console.log('Server is running at http://localhost:3000');
});
```

## Output example

```
Server is running at http://localhost:3000
```

The code consists of the following parts:
1. Import Express.js: `const express = require('express');`
2. Create an Express.js app: `const app = express();`
3. Define a route: `app.get('/', (req, res) => { res.send('Hello World!'); });`
4. Start the server: `app.listen(3000, () => { console.log('Server is running at http://localhost:3000'); });`

## Helpful links
1. [Express.js](https://expressjs.com/)
2. [Node.js](https://nodejs.org/en/)

onelinerhub: [How can I use Express.js and Node.js together to create a web application?](https://onelinerhub.com/expressjs/how-can-i-use-express-js-and-node-js-together-to-create-a-web-application)