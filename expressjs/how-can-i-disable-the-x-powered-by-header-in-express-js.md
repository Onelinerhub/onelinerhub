# How can I disable the X-Powered-By header in Express.js?
// plain

To disable the X-Powered-By header in Express.js, you can use the `app.disable('x-powered-by')` function. This will prevent Express from including the X-Powered-By header in the response.

## Example code

```
const express = require('express');
const app = express();

app.disable('x-powered-by');

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.listen(3000);
```

## Output example

```
Server listening on port 3000
```

The `app.disable('x-powered-by')` function takes a single string argument, which is the name of the header you want to disable. In this case, it is `x-powered-by`.

You can also disable multiple headers at once by passing an array of strings. For example:

```
app.disable(['x-powered-by', 'x-frame-options']);
```

This will disable both the X-Powered-By and X-Frame-Options headers.

## Helpful links

- [Express.js Documentation - App Settings](https://expressjs.com/en/4x/api.html#app.settings.table)
- [Express.js Documentation - App Disable](https://expressjs.com/en/4x/api.html#app.disable)

onelinerhub: [How can I disable the X-Powered-By header in Express.js?](https://onelinerhub.com/expressjs/how-can-i-disable-the-x-powered-by-header-in-express-js)