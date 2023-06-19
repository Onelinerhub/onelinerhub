# How can I add an icon to my Express.js application?
// plain

You can add an icon to your Express.js application by creating a `favicon.ico` file and placing it in the root directory of your project. The `favicon.ico` file should be a 16x16px or 32x32px .ico image.

You can then include the following code in your `app.js` file to enable the icon:

```javascript
const path = require('path');

// Enable favicon
app.use(express.static(path.join(__dirname, 'public')));
app.use(favicon(path.join(__dirname, 'public', 'favicon.ico')));
```

This code will link the `favicon.ico` file to the Express.js application.

## Code explanation

- `const path = require('path');`: This line requires the `path` module which is used to access the project's root directory.
- `app.use(express.static(path.join(__dirname, 'public')));`: This line enables serving static files from the `public` folder.
- `app.use(favicon(path.join(__dirname, 'public', 'favicon.ico')));`: This line links the `favicon.ico` file to the Express.js application.

## Helpful links
- [Express.js Documentation on Favicons](https://expressjs.com/en/resources/middleware/favicon.html)
- [Creating a Favicon](https://www.w3.org/2005/10/howto-favicon)

onelinerhub: [How can I add an icon to my Express.js application?](https://onelinerhub.com/expressjs/how-can-i-add-an-icon-to-my-express-js-application)