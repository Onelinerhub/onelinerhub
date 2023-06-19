# How can I use Express.js with TypeScript?
// plain

Express.js is a web application framework for Node.js that provides a robust set of features for web and mobile applications. TypeScript is a typed superset of JavaScript that compiles to plain JavaScript. Using Express.js with TypeScript is possible by using the [ts-node](https://www.npmjs.com/package/ts-node) package.

To use Express.js with TypeScript, we need to install the `ts-node` package:

```
npm install ts-node
```

Then we can create a `server.ts` file with the following code:
```
import express from "express";

const app = express();

app.get("/", (req, res) => {
  res.send("Hello World!");
});

app.listen(3000, () => {
  console.log("Server running on port 3000");
});
```

Once the server is running, we can access the application by going to `http://localhost:3000` in the browser.

The code above consists of the following parts:

1. `import express from "express"` - This imports the Express.js module.
2. `const app = express()` - This creates an Express.js application.
3. `app.get("/", (req, res) => { ... })` - This defines a route handler for the root path (`/`).
4. `app.listen(3000, () => { ... })` - This starts the Express.js server on port 3000.

By using TypeScript with Express.js, we can take advantage of the type-safety and other features of TypeScript.

## Helpful links

- [Express.js](https://expressjs.com/)
- [TypeScript](https://www.typescriptlang.org/)
- [ts-node](https://www.npmjs.com/package/ts-node)

onelinerhub: [How can I use Express.js with TypeScript?](https://onelinerhub.com/expressjs/how-can-i-use-express-js-with-typescript)