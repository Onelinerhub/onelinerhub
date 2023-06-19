# How can I use Express.js to create a Model-View-Controller application?
// plain

Express.js is a web application framework for Node.js that can be used to create a Model-View-Controller (MVC) application. The following example code illustrates how to use Express.js to create a basic MVC application.

```
const express = require('express');
const app = express();

// Routes
app.get('/', (req, res) => {
  res.send('Hello World!');
});

// Controller
const helloWorld = (req, res) => {
  res.send('Hello World!');
};

// Model
const users = [
  {name: 'John', age: 30},
  {name: 'Jane', age: 25}
];

// View
const renderUsers = (users) => {
  let html = '<ul>';
  users.forEach(user => {
    html += `<li>${user.name} (${user.age})</li>`;
  });
  html += '</ul>';
  return html;
};

// Routes
app.get('/users', (req, res) => {
  res.send(renderUsers(users));
});

// Listen on port 3000
app.listen(3000, () => console.log('Example app listening on port 3000!'));
```

The example code above includes the following parts:

* `const express = require('express');` - This imports the Express.js module.
* `app.get('/', (req, res) => { res.send('Hello World!'); });` - This is a routing call that defines the URL path and the response to be sent when the URL is accessed.
* `const helloWorld = (req, res) => { res.send('Hello World!'); };` - This is the controller, which is a function that handles the request and response.
* `const users = [{name: 'John', age: 30}, {name: 'Jane', age: 25}];` - This is the model, which is an array of data.
* `const renderUsers = (users) => { ... };` - This is the view, which is a function that renders the data into an HTML response.
* `app.listen(3000, () => console.log('Example app listening on port 3000!'));` - This starts the Express.js server and listens on port 3000.

For more information on creating MVC applications with Express.js, see the [Express.js documentation](https://expressjs.com/en/guide/using-template-engines.html).

onelinerhub: [How can I use Express.js to create a Model-View-Controller application?](https://onelinerhub.com/expressjs/how-can-i-use-express-js-to-create-a-model-view-controller-application)