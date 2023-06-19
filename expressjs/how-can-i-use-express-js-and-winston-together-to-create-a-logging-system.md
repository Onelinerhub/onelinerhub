# How can I use Express.js and Winston together to create a logging system?
// plain

Express.js and Winston can be used together to create a logging system. The following example code will demonstrate how to do this:

```
const express = require('express');
const winston = require('winston');

// Create the Express app
const app = express();

// Configure Winston to log to the console
const logger = winston.createLogger({
  transports: [
    new winston.transports.Console()
  ]
});

// Set up a route that will log a message when accessed
app.get('/', (req, res) => {
  logger.info('A request was made to the root route');
  res.send('Hello World!');
});

// Listen on port 3000
app.listen(3000);
```

This code will create an Express server that listens on port 3000 and logs a message to the console when the root route is accessed.

The code consists of the following parts:

1. Require the Express and Winston modules.
2. Create the Express app.
3. Configure Winston to log to the console.
4. Set up the root route to log a message when accessed.
5. Listen on port 3000.

## Helpful links

- [Express.js](https://expressjs.com/)
- [Winston](https://github.com/winstonjs/winston)

onelinerhub: [How can I use Express.js and Winston together to create a logging system?](https://onelinerhub.com/expressjs/how-can-i-use-express-js-and-winston-together-to-create-a-logging-system)