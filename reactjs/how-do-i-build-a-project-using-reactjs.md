# How do I build a project using ReactJS?
// plain

To build a project using ReactJS, you'll need to install the React library and create a `index.html` file.

Include the following code in the `index.html` file:

```html
<div id="root"></div>
<script src="https://unpkg.com/react@16/umd/react.development.js"></script>
<script src="https://unpkg.com/react-dom@16/umd/react-dom.development.js"></script>
<script src="index.js"></script>
```

This will include the necessary React and ReactDOM libraries and the `index.js` script.

In the `index.js` file, you can create a React component with the following code:

```js
class App extends React.Component {
  render() {
    return <h1>Hello World!</h1>;
  }
}

ReactDOM.render(<App />, document.getElementById("root"));
```

This will render the `<h1>Hello World!</h1>` element inside the `<div id="root"></div>` element in the `index.html` file.

For more information on building projects with ReactJS, check out the [React documentation](https://reactjs.org/docs/getting-started.html).

onelinerhub: [How do I build a project using ReactJS?](https://onelinerhub.com/reactjs/how-do-i-build-a-project-using-reactjs)