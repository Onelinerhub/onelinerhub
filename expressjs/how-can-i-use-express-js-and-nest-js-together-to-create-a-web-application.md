# How can I use Express.js and Nest.js together to create a web application?
// plain

Express.js and Nest.js can be used together to create a web application by integrating the Express.js application into the Nest.js framework. This allows developers to use the features of both Express.js and Nest.js in the same application.

## Example code


```
// Import Express.js
const express = require('express');

// Initialize Express.js
const app = express();

// Import Nest.js
const { NestFactory } = require('@nestjs/core');

// Initialize Nest.js
const nest = await NestFactory.create(AppModule);

// Integrate Express.js into Nest.js
app.use(nest.getHttpAdapter().getInstance());

// Start the application
app.listen(3000);
```

This code imports Express.js and initializes it, imports Nest.js and initializes it, and then integrates Express.js into the Nest.js framework. Finally, the application is started on port 3000.

## Code explanation


1. `const express = require('express');` - This imports the Express.js library.
2. `const app = express();` - This initializes the Express.js application.
3. `const { NestFactory } = require('@nestjs/core');` - This imports the Nest.js library.
4. `const nest = await NestFactory.create(AppModule);` - This initializes the Nest.js application.
5. `app.use(nest.getHttpAdapter().getInstance());` - This integrates the Express.js application into the Nest.js framework.
6. `app.listen(3000);` - This starts the application on port 3000.

## Helpful links

- [Express.js](https://expressjs.com/)
- [Nest.js](https://nestjs.com/)

onelinerhub: [How can I use Express.js and Nest.js together to create a web application?](https://onelinerhub.com/expressjs/how-can-i-use-express-js-and-nest-js-together-to-create-a-web-application)