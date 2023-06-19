# files

How do I serve static files using Express.js?
// plain

To serve static files using Express.js, you can use the `express.static` built-in middleware function. This function is based on the [serve-static](https://www.npmjs.com/package/serve-static) module and is responsible for serving the static assets of an Express.js application.

The `express.static` middleware takes one argument, the absolute path to the directory that contains the static assets to be served.

For example, given the following `index.js` file:

```js
const express = require('express');
const app = express();

app.use(express.static('public'));

app.listen(3000, () => {
  console.log('Server started on port 3000');
});
```

The `express.static` middleware will serve all the static assets located in the `public` directory, located in the same directory as the `index.js` file.

The `express.static` middleware also supports several options, such as setting the cache control, setting the index file, etc.

For more information, please refer to the [Express.js documentation](https://expressjs.com/en/starter/static-files.html).

onelinerhub: [files

How do I serve static files using Express.js?](https://onelinerhub.com/expressjs/files--how-do-i-serve-static-files-using-express-js)