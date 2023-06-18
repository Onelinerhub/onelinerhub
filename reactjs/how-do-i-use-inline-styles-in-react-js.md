# How do I use inline styles in React JS?
// plain

Inline styles in React JS allow you to apply styles directly to a specific React element. This is done by using the `style` attribute, and passing in an object containing CSS properties and their corresponding values.

For example:

```js
<h1 style={{ color: 'red', fontSize: '50px' }}>Hello World!</h1>
```

This code will render a `<h1>` element with a red color and a font size of 50px.

The `style` attribute takes an object containing one or more CSS properties and their values. Each property is written in camelCase (e.g. `fontSize` instead of `font-size`).

## Code explanation


- `<h1>`: The HTML element to which the style will be applied.
- `style`: The attribute used to apply inline styles.
- `{{ color: 'red', fontSize: '50px' }}`: The object containing the CSS properties and their values.

For more information, please see the following links:

- [React - Inline Styles](https://reactjs.org/docs/dom-elements.html#style)
- [CSS in JS](https://speakerdeck.com/vjeux/react-css-in-js)

onelinerhub: [How do I use inline styles in React JS?](https://onelinerhub.com/reactjs/how-do-i-use-inline-styles-in-react-js)