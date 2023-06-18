# How do I create an app using ReactJS?
// plain

1. To create an app using ReactJS, you need to install the React and ReactDOM libraries. You can do this with npm by running `npm install react react-dom`.

2. Then, create a new file called `index.js` and add the following code:

```
import React from 'react';
import ReactDOM from 'react-dom';

ReactDOM.render(
  <h1>Hello, world!</h1>,
  document.getElementById('root')
);
```

3. This code will render the text "Hello, world!" in an element with the ID of `root` (which you'll need to add to your HTML file).

4. Next, create an HTML file called `index.html` and add the following code:

```
<html>
  <head>
    <title>My React App</title>
  </head>
  <body>
    <div id="root"></div>
    <script src="index.js"></script>
  </body>
</html>
```

5. Now, open `index.html` in your browser and you should see the text "Hello, world!"

6. To build a more complex app, you can create components and render them in the `index.js` file. You can also use libraries like [React Router](https://reacttraining.com/react-router/) to handle routing.

7. For more information, check out the [React documentation](https://reactjs.org/docs/getting-started.html).

onelinerhub: [How do I create an app using ReactJS?](https://onelinerhub.com/reactjs/how-do-i-create-an-app-using-reactjs)