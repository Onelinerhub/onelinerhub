# How do I set the z-index of an element in React.js?
// plain

To set the z-index of an element in React.js, you can use the `style` prop. The `style` prop takes an object of CSS properties and values.

## Example code

```
<div style={{ position: 'relative', zIndex: 1 }}>
  <p>This is a paragraph.</p>
</div>
```

This code sets the z-index of the `div` to 1.

## Code explanation

- `<div>`: the HTML element to which the z-index will be applied
- `style`: a prop that takes an object of CSS properties and values
- `position: 'relative'`: sets the position of the element to relative
- `zIndex: 1`: sets the z-index of the element to 1

## Helpful links
- [CSS z-index property](https://www.w3schools.com/cssref/pr_pos_z-index.asp)
- [React style prop](https://reactjs.org/docs/dom-elements.html#style)

onelinerhub: [How do I set the z-index of an element in React.js?](https://onelinerhub.com/reactjs/how-do-i-set-the-z-index-of-an-element-in-react-js)