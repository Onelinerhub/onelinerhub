# How do I use the ReactJS documentation to get started with ReactJS development?
// plain

ReactJS documentation is a great resource to get started with ReactJS development. To get started, you need to include the React library in your HTML page. You can use a CDN or download it from the [React website](https://reactjs.org/).

```
<script src="https://unpkg.com/react@16/umd/react.development.js" crossorigin></script>
<script src="https://unpkg.com/react-dom@16/umd/react-dom.development.js" crossorigin></script>
```

Once you have included the React library, you can start creating React components. A React component is a JavaScript class or function that optionally accepts inputs called props and returns a React element that describes how a section of the UI (User Interface) should appear.

```
class Hello extends React.Component {
  render() {
    return <h1>Hello, {this.props.name}</h1>;
  }
}

ReactDOM.render(
  <Hello name="World" />,
  document.getElementById('root')
);
```

## Output example

```
<h1>Hello, World</h1>
```

To learn more about React components, refer to the [React Components documentation](https://reactjs.org/docs/components-and-props.html). The React documentation also contains information about [state and lifecycle](https://reactjs.org/docs/state-and-lifecycle.html), [hooks](https://reactjs.org/docs/hooks-intro.html), [events](https://reactjs.org/docs/handling-events.html), and much more.

onelinerhub: [How do I use the ReactJS documentation to get started with ReactJS development?](https://onelinerhub.com/reactjs/how-do-i-use-the-reactjs-documentation-to-get-started-with-reactjs-development)