# How can I render HTML pages using Express.js?
// plain

Express.js is a web application framework for Node.js that enables you to render HTML pages. To render HTML pages using Express.js, you need to create a route for the HTML page and use the `res.sendFile` method. Here is an example of how to do this:

```
//Import Express.js
const express = require('express');

//Create an instance of Express.js
const app = express();

//Create a route for the HTML page
app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

//Start the server
app.listen(3000, () => {
  console.log('Server started on port 3000');
});
```

## Output example

```
Server started on port 3000
```

1. **Import Express.js** - This imports the Express.js module.
2. **Create an instance of Express.js** - This creates an instance of Express.js.
3. **Create a route for the HTML page** - This creates a route that will render the HTML page when the route is accessed.
4. **Use the `res.sendFile` method** - This method is used to send the HTML page to the browser.
5. **Start the server** - This starts the server so that the HTML page can be rendered.

## Helpful links

- [Express.js Documentation](https://expressjs.com/en/api.html)
- [Using Express.js to Render HTML Pages](https://www.codementor.io/@mattgoldspink/using-express-js-to-render-html-pages-du107yb1r)

onelinerhub: [How can I render HTML pages using Express.js?](https://onelinerhub.com/expressjs/how-can-i-render-html-pages-using-express-js)