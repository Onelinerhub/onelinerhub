# How do I use an Express.js logger?
// plain

Using an Express.js logger is an easy way to log information about your Express.js application. It allows you to log information about HTTP requests, errors, and other application events.

To use an Express.js logger, you must first install the Morgan package.

```
npm install morgan
```

Then, you must require Morgan in your Express.js application.

```
const morgan = require('morgan');
```

Next, you must configure Morgan to use the format of your choice.

```
app.use(morgan('combined'));
```

Finally, you must use the Morgan middleware in your application.

```
app.use(morgan('combined'));
```

This will cause Morgan to log all requests to the console.

## Code explanation


1. Install Morgan package - `npm install morgan`
2. Require Morgan in Express.js application - `const morgan = require('morgan');`
3. Configure Morgan to use desired format - `app.use(morgan('combined'));`
4. Use Morgan middleware in application - `app.use(morgan('combined'));`

## Helpful links

- [Morgan documentation](https://github.com/expressjs/morgan)
- [Express.js logging tutorial](https://www.digitalocean.com/community/tutorials/how-to-use-logging-middleware-in-express)

onelinerhub: [How do I use an Express.js logger?](https://onelinerhub.com/expressjs/how-do-i-use-an-express-js-logger)