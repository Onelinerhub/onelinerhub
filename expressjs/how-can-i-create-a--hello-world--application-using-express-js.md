# How can I create a "Hello World" application using Express.js?
// plain

The following steps will guide you through the process of creating a "Hello World" application using Express.js:

1. Create a new directory for your project and navigate into it.

2. Install Express.js using npm:
```
npm install express
```

3. Create a `server.js` file in the root of your project directory and open it in your code editor.

4. Import Express.js into your `server.js` file:
```js
const express = require('express');
```

5. Create an instance of Express.js in your `server.js` file:
```js
const app = express();
```

6. Create a route that will respond to a `GET` request with a "Hello World" message:
```js
app.get('/', (req, res) => {
  res.send('Hello World!');
});
```

7. Start the server:
```
node server.js
```

You can now access your "Hello World" application at `http://localhost:3000`.

## Helpful links
- [Express.js Docs](https://expressjs.com/en/api.html)
- [Getting Started with Express.js](https://expressjs.com/en/starter/installing.html)

onelinerhub: [How can I create a "Hello World" application using Express.js?](https://onelinerhub.com/expressjs/how-can-i-create-a--hello-world--application-using-express-js)