# How do I disable CORS in Express.js?
// plain

To disable CORS in Express.js, you can use the [cors](https://www.npmjs.com/package/cors) middleware package. To use it, you will need to install it first:

```
$ npm install cors
```

Then, you can use it in your Express.js app:

```javascript
const express = require('express');
const cors = require('cors');

const app = express();

// Disable CORS
app.use(cors());

// Your routes
app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.listen(3000);
```

The code above will disable CORS in your Express.js app.

## Code explanation


1. `const cors = require('cors');` - This imports the cors package.
2. `app.use(cors());` - This uses the cors middleware to disable CORS.

## Helpful links

- [cors npm package](https://www.npmjs.com/package/cors)
- [Express.js documentation](https://expressjs.com/en/4x/api.html#app.use)

onelinerhub: [How do I disable CORS in Express.js?](https://onelinerhub.com/expressjs/how-do-i-disable-cors-in-express-js)