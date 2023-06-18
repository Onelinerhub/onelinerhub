# How do I render a component in ReactJS?
// plain

Rendering a component in ReactJS is done using the `ReactDOM.render()` method. This method takes two arguments: the React element or component to be rendered and the DOM node where the element should be rendered.

For example, the following code will render a `<MyComponent />` element inside a `<div>` with an id of `root`:

```
ReactDOM.render(<MyComponent />, document.getElementById('root'));
```

This code will output nothing, but it will render the `<MyComponent />` element inside the `<div>` with an id of `root`.

## Code explanation


* `ReactDOM.render()` - The method used to render a React element or component.
* `<MyComponent />` - The React element or component to be rendered.
* `document.getElementById('root')` - The DOM node where the element should be rendered.

## Helpful links

* [ReactDOM.render() - React Documentation](https://reactjs.org/docs/react-dom.html#render)
* [React Components - React Documentation](https://reactjs.org/docs/components-and-props.html)

onelinerhub: [How do I render a component in ReactJS?](https://onelinerhub.com/reactjs/how-do-i-render-a-component-in-reactjs)