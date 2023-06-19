# How do I create a backend with Express.js?
// plain

Creating a backend with Express.js is a straightforward process. It requires Node.js and npm to be installed beforehand.

Once Node.js and npm are installed, you can create a new project directory and install Express.js with the following commands:

```
$ mkdir myproject
$ cd myproject
$ npm init -y
$ npm install express
```

After Express.js is installed, you can create a file named `index.js` and add the following code to it:

```js
const express = require('express')
const app = express()

app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.listen(3000, () => console.log('Server running on port 3000'))
```

The code above will create a server listening on port 3000 and will respond to `GET` requests with a `Hello World!` message.

When the code is run, the output should look like this:

```
$ node index.js
Server running on port 3000
```

The code consists of the following parts:

- `const express = require('express')` - imports the Express.js module;
- `const app = express()` - creates an Express.js application instance;
- `app.get('/', (req, res) => { ... })` - defines a route handler for `GET` requests to the root path;
- `res.send('Hello World!')` - sends a response with a `Hello World!` message;
- `app.listen(3000, () => console.log('Server running on port 3000'))` - starts the server listening on port 3000.

For more information, you can refer to the [Express.js documentation](https://expressjs.com/en/guide/routing.html).

onelinerhub: [How do I create a backend with Express.js?](https://onelinerhub.com/expressjs/how-do-i-create-a-backend-with-express-js)