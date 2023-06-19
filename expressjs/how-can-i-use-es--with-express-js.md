# How can I use ES6 with Express.js?
// plain

ES6 is a JavaScript specification that provides many new features to the language. Express.js is a Node.js web framework that allows developers to quickly create web applications. ES6 can be used with Express.js to create powerful web applications.

To use ES6 with Express.js, you need to install the `babel-register` package. This package allows Node.js to compile ES6 code.

```javascript
// Install babel-register
npm install babel-register
```

Once the package is installed, you can create an Express.js server using ES6 code.

```javascript
// ES6 Express server
require('babel-register');
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.listen(3000, () => {
  console.log('Server is running on port 3000');
});

// Output
Server is running on port 3000
```

The code above creates an Express server that listens on port 3000 and responds with “Hello World!” when the root URL is accessed.

To summarize, the steps to use ES6 with Express.js are:

1. Install the `babel-register` package.
2. Require `babel-register` before requiring Express.js.
3. Create an Express server using ES6 code.

## Helpful links
- [Babel](https://babeljs.io/)
- [Express.js](https://expressjs.com/)

onelinerhub: [How can I use ES6 with Express.js?](https://onelinerhub.com/expressjs/how-can-i-use-es--with-express-js)