# How can I use ReactJS without JSX?
// plain

ReactJS can be used without JSX by using the React.createElement() method. This method allows you to create React elements with plain JavaScript.

## Example

```
const element = React.createElement(
  'h1',
  {className: 'greeting'},
  'Hello, world!'
);
```

This code will create a React element with an h1 tag, a className of 'greeting' and the text 'Hello, world!'

## Code explanation

- `React.createElement()`: This method creates a React element.
- `'h1'`: This is the HTML tag that will be used for the element.
- `{className: 'greeting'}`: This is an object containing the className of the element.
- `'Hello, world!'`: This is the text that will be displayed in the element.

## Helpful links
- https://reactjs.org/docs/react-without-jsx.html
- https://reactjs.org/docs/react-api.html#createelement

onelinerhub: [How can I use ReactJS without JSX?](https://onelinerhub.com/reactjs/how-can-i-use-reactjs-without-jsx)