# How do I start using ReactJS?
// plain

###### ReactJS is a JavaScript library for building user interfaces. To start using ReactJS, you need to include the React library in your HTML page.

```
<script src="https://unpkg.com/react@16/umd/react.development.js" crossorigin></script>
<script src="https://unpkg.com/react-dom@16/umd/react-dom.development.js" crossorigin></script>
```

###### Next, you need to create an HTML element to render the React component. This can be done by creating a `div` element with an `id` attribute.

```
<div id="root"></div>
```

###### Then, you need to create a React component. This can be done by defining a JavaScript function that returns a React element.

```
function Hello() {
  return <h1>Hello World!</h1>;
}
```

###### Finally, you need to render the React component to the DOM. This can be done using the `ReactDOM.render()` method.

```
ReactDOM.render(<Hello />, document.getElementById('root'));
```

###### Output:
`Hello World!`

## Code explanation

- `<script>`: Used to include the React library in the HTML page.
- `<div>`: Used to create an HTML element to render the React component.
- `function`: Used to define a React component.
- `ReactDOM.render()`: Used to render the React component to the DOM.

###### ## Helpful links
- [React Documentation](https://reactjs.org/docs/getting-started.html)
- [React Tutorial](https://reactjs.org/tutorial/tutorial.html)

onelinerhub: [How do I start using ReactJS?](https://onelinerhub.com/reactjs/how-do-i-start-using-reactjs)