# How do I install ReactJS?
// plain

1. Installing ReactJS is easy and can be done with a few simple steps.
2. First, create a project folder and change directory into it.
3. Next, install the React and ReactDOM libraries using npm:
```
npm install react react-dom
```
4. You can also use a CDN to include React in your project. To do this, add the following script tag to your HTML file:
```
<script src="https://unpkg.com/react@16/umd/react.development.js" crossorigin></script>
<script src="https://unpkg.com/react-dom@16/umd/react-dom.development.js" crossorigin></script>
```
5. To use React, you will also need to include the Babel JavaScript compiler. This will allow you to write React code in modern JavaScript syntax:
```
<script src="https://unpkg.com/babel-standalone@6.15.0/babel.min.js"></script>
```
6. Finally, create a file called `index.js` and add the following code:
```
import React from 'react';
import ReactDOM from 'react-dom';

ReactDOM.render(
  <h1>Hello, world!</h1>,
  document.getElementById('root')
);
```
7. To run the code, open `index.html` in your browser. You should see the phrase "Hello, world!" displayed on the page.

## Helpful links
- [React Documentation](https://reactjs.org/docs/getting-started.html)
- [Create React App](https://create-react-app.dev/)

onelinerhub: [How do I install ReactJS?](https://onelinerhub.com/reactjs/how-do-i-install-reactjs)