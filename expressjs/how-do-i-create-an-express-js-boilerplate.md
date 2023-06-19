# How do I create an Express.js boilerplate?
// plain

1. To create an Express.js boilerplate, first install Express.js using the command `npm install express`.
2. Create a file named `server.js` and add the following code to it:

```
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Hello World!');
});

const port = process.env.PORT || 5000;

app.listen(port, () => console.log(`Server running on port ${port}`));
```

This will create an Express.js server that listens on port 5000 and responds to requests with "Hello World!"

3. To add additional routes, add a `GET` or `POST` request to the `app` object, like this:

```
app.get('/about', (req, res) => {
  res.send('About page');
});
```

This adds a route to the `/about` page.

4. To add middleware to the application, use `app.use()` like this:

```
app.use(express.json());
```

This adds the `express.json()` middleware to the application.

5. To add a template engine, install the desired template engine and then configure Express.js to use it. For example, to use [Pug](https://pugjs.org/), install it using `npm install pug` and then add the following code to `server.js`:

```
app.set('view engine', 'pug');
```

6. To serve static files, use `app.use()` like this:

```
app.use(express.static('public'));
```

This will serve all files in the `public` directory.

7. To add a database, install the desired database driver and then configure Express.js to use it. For example, to use [Mongoose](https://mongoosejs.com/), install it using `npm install mongoose` and then add the following code to `server.js`:

```
const mongoose = require('mongoose');

mongoose
  .connect('mongodb://localhost/my_database', {
    useNewUrlParser: true,
    useUnifiedTopology: true
  })
  .then(() => console.log('Connected to MongoDB...'))
  .catch(err => console.error('Could not connect to MongoDB...', err));
```

This will connect to a MongoDB database running on the local machine.

At this point, the Express.js boilerplate is complete.

**Relevant Links**
- [Express.js](https://expressjs.com/)
- [Pug](https://pugjs.org/)
- [Mongoose](https://mongoosejs.com/)

onelinerhub: [How do I create an Express.js boilerplate?](https://onelinerhub.com/expressjs/how-do-i-create-an-express-js-boilerplate)