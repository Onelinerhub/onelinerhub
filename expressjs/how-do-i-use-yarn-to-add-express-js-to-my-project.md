# How do I use Yarn to add Express.js to my project?
// plain

Adding Express.js to a project using Yarn is a simple process.  First, install Express.js within the project directory by running the command `yarn add express` in the terminal. This will add Express.js to the project's dependencies in `package.json`.

Next, create an `index.js` file in the project directory. This file will be used to start the Express.js server.

In the `index.js` file, include the following code:

```javascript
const express = require('express');

const app = express();

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.listen(3000, () => {
  console.log('Server is listening on port 3000');
});
```

This code will create an Express.js server on port 3000 which will respond to `GET` requests to the root route (`/`) with the string `Hello World!`.

To start the server, run the command `yarn start` in the terminal. This will start the Express.js server and you should see the following output in the terminal:

```
Server is listening on port 3000
```

Now you can make `GET` requests to the root route (`/`) and receive the response `Hello World!`.

Parts of the code:
- `const express = require('express');`: This line imports the Express.js module in order to use its functionality.
- `const app = express();`: This line creates an Express.js application.
- `app.get('/', (req, res) => {...});`: This line creates a GET route on the root route (`/`) which will respond to `GET` requests with the string `Hello World!`.
- `app.listen(3000, () => {...});`: This line starts the Express.js server on port 3000.

## Helpful links
- [Yarn Documentation](https://yarnpkg.com/en/docs)
- [Express.js Documentation](https://expressjs.com/en/starter/installing.html)

onelinerhub: [How do I use Yarn to add Express.js to my project?](https://onelinerhub.com/expressjs/how-do-i-use-yarn-to-add-express-js-to-my-project)