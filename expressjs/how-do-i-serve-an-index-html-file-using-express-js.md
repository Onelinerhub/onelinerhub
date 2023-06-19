# How do I serve an index.html file using Express.js?
// plain

To serve an `index.html` file using Express.js, you will need to create a route that will serve the `index.html` file. The following code block will create a route that will serve the `index.html` file located in the `public` directory:

```javascript
const express = require('express');
const app = express();

app.use(express.static(__dirname + '/public'));

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/public/index.html');
});

app.listen(3000, () => {
  console.log('Server started on port 3000');
});
```

The code above will create a route that will serve the `index.html` file located in the `public` directory when the route is accessed.

## Code explanation


- `const express = require('express');`: This line imports the Express.js library.
- `const app = express();`: This line creates an Express.js application.
- `app.use(express.static(__dirname + '/public'));`: This line tells Express.js to serve static files from the `public` directory.
- `app.get('/', (req, res) => {`: This line creates a route that will be called when the root route is accessed.
- `res.sendFile(__dirname + '/public/index.html');`: This line tells Express.js to serve the `index.html` file located in the `public` directory.
- `app.listen(3000, () => {`: This line tells Express.js to listen for requests on port 3000.

## Helpful links

- [Express.js Documentation](https://expressjs.com/en/api.html)
- [MDN Web Docs - Serving Static Files](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Express_Nodejs/skeleton_website#Serving_static_files)

onelinerhub: [How do I serve an index.html file using Express.js?](https://onelinerhub.com/expressjs/how-do-i-serve-an-index-html-file-using-express-js)