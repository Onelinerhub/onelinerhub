# How do I use the Express.js router to create routes for my web application?
// plain

The Express.js router is an essential part of any web application built with Express.js. It allows you to create routes and specify how the application responds to requests. To use the Express.js router, you must first import the Router class from Express.js:

```
const { Router } = require('express');
```

Next, create a new router instance:

```
const router = new Router();
```

You can then create routes and specify how your application should respond to requests. For example, the following code creates a route that responds with a welcome message when a GET request is made to the root URL:

```
router.get('/', (req, res) => {
  res.send('Welcome to my web application!');
});
```

Finally, you must add the router instance to your Express.js application:

```
const app = express();

// Add router to the application
app.use(router);
```

You can create as many routes as you need for your application and specify the response for each.

**Parts of code explained:**

- `const { Router } = require('express');`: imports the Router class from Express.js
- `const router = new Router();`: creates a new router instance
- `router.get('/', (req, res) => { ... });`: creates a route that responds to a GET request to the root URL
- `app.use(router);`: adds the router instance to the Express.js application

**## Helpful links**
- [Express.js Router Documentation](https://expressjs.com/en/guide/routing.html)
- [Express.js API Reference](https://expressjs.com/en/4x/api.html#router)

onelinerhub: [How do I use the Express.js router to create routes for my web application?](https://onelinerhub.com/expressjs/how-do-i-use-the-express-js-router-to-create-routes-for-my-web-application)