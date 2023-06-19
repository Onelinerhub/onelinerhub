# How do I use Express.js locals to pass variables to my views?
// plain

Express.js locals are variables that are available to all views rendered by the Express application. They are used to provide dynamic content to the view, such as user data or application configuration.

To use Express.js locals, you must first create the variable and assign it a value. This can be done in the application's main configuration file or in the route handler for the view. For example:

```
// main configuration file
app.locals.myVar = 'Hello World!';

// route handler
res.locals.myVar = 'Hello World!';
```

In the view, you can access the variable using `<%= myVar %>` or `<%- myVar %>` depending on if you want to escape the output or not.

```
<p>My variable is <%= myVar %></p>

<!-- Output:
<p>My variable is Hello World!</p>
-->
```

## Code explanation


- `app.locals.myVar = 'Hello World!';`: This is used to create a variable 'myVar' and assign it the value 'Hello World!' in the application's main configuration file.

- `res.locals.myVar = 'Hello World!';`: This is used to create a variable 'myVar' and assign it the value 'Hello World!' in the route handler for the view.

- `<%= myVar %>`: This is used to access the variable 'myVar' in the view.

## Helpful links

- [Express.js Locals](https://expressjs.com/en/api.html#res.locals)
- [Express.js Guide](https://expressjs.com/en/guide/using-template-engines.html)

onelinerhub: [How do I use Express.js locals to pass variables to my views?](https://onelinerhub.com/expressjs/how-do-i-use-express-js-locals-to-pass-variables-to-my-views)