# How do I use Express.js and Koa together to create a web application?
// plain

Using Express.js and Koa together to create a web application requires some setup. First, install both Express.js and Koa using npm:

```
npm install express
npm install koa
```

Then, create a new file called `app.js` and require both Express.js and Koa, like this:

```
const express = require('express');
const koa = require('koa');
```

Next, create a new Express.js app and Koa app, and make them listen on different ports:

```
const expressApp = express();
const koaApp = new koa();

expressApp.listen(3000);
koaApp.listen(4000);
```

Now, you can use Express.js and Koa together to create your web application. For example, you can use Express.js to handle the routing of your application, and use Koa to handle the business logic of your application.

Parts of the code:

1. `npm install express` - Installing Express.js using npm
2. `npm install koa` - Installing Koa using npm
3. `const express = require('express');` - Requiring Express.js
4. `const koa = require('koa');` - Requiring Koa
5. `const expressApp = express();` - Creating a new Express.js app
6. `const koaApp = new koa();` - Creating a new Koa app
7. `expressApp.listen(3000);` - Making Express.js app listen on port 3000
8. `koaApp.listen(4000);` - Making Koa app listen on port 4000

## Helpful links

- [Express.js](https://expressjs.com/)
- [Koa](https://koajs.com/)

onelinerhub: [How do I use Express.js and Koa together to create a web application?](https://onelinerhub.com/expressjs/how-do-i-use-express-js-and-koa-together-to-create-a-web-application)