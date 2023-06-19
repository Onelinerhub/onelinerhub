# What is Express.js?
// plain

```
Express.js is a Node.js web application framework that provides a robust set of features for web and mobile applications. It is used to build single-page, multi-page, and hybrid web applications. It is the de facto standard server framework for Node.js.

## Example code

const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Hello World!');
});

const port = 3000;
app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`);
});

## Output example

Example app listening at http://localhost:3000

## Code explanation

const express = require('express'); // importing the express module
const app = express(); // creating an instance of Express
app.get('/', (req, res) => { // creating a route for '/'
  res.send('Hello World!'); // sending a response when the route is accessed
});
const port = 3000; // setting the port to 3000
app.listen(port, () => { // listening for requests on the specified port
  console.log(`Example app listening at http://localhost:${port}`);
});

## Helpful links
https://expressjs.com/
https://www.tutorialspoint.com/expressjs/index.htm
https://www.freecodecamp.org/news/introduction-to-express-js-what-is-express-js-and-why-should-i-care-ea3f3a614a89/
```

onelinerhub: [What is Express.js?](https://onelinerhub.com/expressjs/what-is-express-js)