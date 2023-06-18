# How do I use quotes in ReactJS?
// plain

In ReactJS, you can use quotes to enclose strings in JSX code. Here is an example of how to use quotes in ReactJS:

```
const App = () => {
  return <h1>Hello, "World"</h1>;
};
```

This code will render a heading with the text "Hello, World".

When using quotes in ReactJS, there are a few things to keep in mind:

1. Single quotes and double quotes can both be used. For example, `<h1>Hello, "World"</h1>` and `<h1>Hello, 'World'</h1>` are both valid.

2. If you need to use quotes inside a string, you can use backslashes to escape them. For example, `<h1>Hello, \"World\"</h1>` will render the same as the previous examples.

3. If you need to use both single and double quotes in the same string, you can use template literals. For example, `<h1>Hello, ${`"World"`}</h1>` will render the same as the previous examples.

These are the basics of using quotes in ReactJS. For more information, check out the following links:

- [MDN - Template Literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals)
- [React - JSX In Depth](https://reactjs.org/docs/jsx-in-depth.html)

onelinerhub: [How do I use quotes in ReactJS?](https://onelinerhub.com/reactjs/how-do-i-use-quotes-in-reactjs)