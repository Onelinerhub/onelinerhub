# How can I set up X-Frame-Options in ExpressJS?
// plain

Setting up X-Frame-Options in ExpressJS is relatively simple.

To start, we'll need to import the `helmet` package:
```
const helmet = require('helmet');
```

Next, we'll need to add the `helmet.frameguard()` middleware to our Express application:
```
app.use(helmet.frameguard({ action: 'sameorigin' }));
```

The `action` parameter can be set to either `deny` or `sameorigin` depending on your needs. `deny` will prevent rendering of the page in a frame or iframe, while `sameorigin` will allow rendering only if the origin is the same as the host.

We can also add additional parameters to the `frameguard()` middleware, such as `allowFrom` to specify a whitelist of domains that are allowed to render the page in a frame or iframe.

```
app.use(helmet.frameguard({ action: 'sameorigin', allowFrom: 'http://example.com' }));
```

That's all you need to do to set up X-Frame-Options in ExpressJS.

Parts:
- Import the `helmet` package
- Add the `helmet.frameguard()` middleware to Express application
- Set the `action` parameter to either `deny` or `sameorigin`
- Optionally add additional parameters such as `allowFrom` to specify a whitelist of domains

## Helpful links
- [Helmet.js](https://helmetjs.github.io/)
- [ExpressJS](https://expressjs.com/)

onelinerhub: [How can I set up X-Frame-Options in ExpressJS?](https://onelinerhub.com/expressjs/how-can-i-set-up-x-frame-options-in-expressjs)