# How can I use ReactJS to zoom in and out of elements on a page?
// plain

ReactJS provides a way to zoom in and out of elements on a page using the built-in `zoom` CSS property. To use the `zoom` property, you can set it on the element you want to zoom in or out of. For example:

```js
const MyComponent = () => {
  return (
    <div style={{ zoom: 2 }}>
      This element will be zoomed in by a factor of 2
    </div>
  );
};
```

You can also use the `scale` property to achieve the same effect. For example:

```js
const MyComponent = () => {
  return (
    <div style={{ transform: 'scale(2)' }}>
      This element will be zoomed in by a factor of 2
    </div>
  );
};
```

## Code explanation

- `zoom`: The built-in `zoom` CSS property that can be set on the element you want to zoom in or out of.
- `scale`: The `scale` property that can also be used to achieve the same effect as `zoom`.

## Helpful links
- [MDN - CSS zoom](https://developer.mozilla.org/en-US/docs/Web/CSS/zoom)
- [MDN - CSS transform](https://developer.mozilla.org/en-US/docs/Web/CSS/transform)

onelinerhub: [How can I use ReactJS to zoom in and out of elements on a page?](https://onelinerhub.com/reactjs/how-can-i-use-reactjs-to-zoom-in-and-out-of-elements-on-a-page)