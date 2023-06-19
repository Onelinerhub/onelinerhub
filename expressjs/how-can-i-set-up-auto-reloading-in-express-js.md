# How can I set up auto reloading in Express.js?
// plain

Auto reloading in Express.js can be set up using the Nodemon package. Nodemon will watch for changes in the code and automatically restart the server when changes are detected.

```
npm install --save-dev nodemon
```

Once Nodemon is installed, you can start the server using the following command:

```
nodemon server.js
```

This will start the server and watch for any changes in the code. When changes are detected, the server will automatically restart.

## Code explanation

- npm install --save-dev nodemon: Installs the Nodemon package
- nodemon server.js: Starts the server and watches for changes in the code

## Helpful links
- https://www.npmjs.com/package/nodemon
- https://expressjs.com/en/advanced/auto-reloading.html

onelinerhub: [How can I set up auto reloading in Express.js?](https://onelinerhub.com/expressjs/how-can-i-set-up-auto-reloading-in-express-js)