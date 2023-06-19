# How do I set up a favicon with Express.js?
// plain

To set up a favicon with Express.js, you must first create a `favicon.ico` file and save it in the root directory of your project. Then, you must require the `serve-favicon` middleware and include it in your Express.js app. Here is an example of how to do this:

```javascript
const express = require('express');
const favicon = require('serve-favicon');
const path = require('path');

const app = express();

app.use(favicon(path.join(__dirname, 'favicon.ico')));
```

This will serve the `favicon.ico` file whenever the `/favicon.ico` path is requested. No output is produced.

The code above consists of the following parts:

- `const express = require('express');` - This line imports the Express.js library.
- `const favicon = require('serve-favicon');` - This line imports the `serve-favicon` middleware.
- `const path = require('path');` - This line imports the `path` library, which is used for manipulating file paths.
- `const app = express();` - This line creates an Express.js app.
- `app.use(favicon(path.join(__dirname, 'favicon.ico')));` - This line uses the `serve-favicon` middleware with the path to the `favicon.ico` file.

## Helpful links

- [Express.js](https://expressjs.com/)
- [serve-favicon](https://www.npmjs.com/package/serve-favicon)
- [path](https://nodejs.org/api/path.html)

onelinerhub: [How do I set up a favicon with Express.js?](https://onelinerhub.com/expressjs/how-do-i-set-up-a-favicon-with-express-js)