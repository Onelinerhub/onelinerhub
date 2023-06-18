# How do I create a template using ReactJS?
// plain

To create a template using ReactJS, you can use the `React.createElement` method. This method takes three arguments: the type of element to be created, any properties to be set on the element, and the children of the element. The type of element can be a string, such as `"div"` or `"h1"`, or a React component.

For example, the following code creates a `<div>` element with two `<h1>` children:

```js
const template = React.createElement(
  "div",
  null,
  React.createElement("h1", null, "Hello World"),
  React.createElement("h1", null, "Goodbye World")
);
```

The output of this code is a `ReactElement` object:

```js
ReactElement {
  type: "div",
  props: {
    children: [
      ReactElement { type: "h1", props: { children: "Hello World" } },
      ReactElement { type: "h1", props: { children: "Goodbye World" } }
    ]
  }
}
```

The `React.createElement` method is a powerful way to create React templates. It allows you to quickly create complex React elements with any number of children.

For more information, see the [React documentation](https://reactjs.org/docs/react-api.html#createelement).

onelinerhub: [How do I create a template using ReactJS?](https://onelinerhub.com/reactjs/how-do-i-create-a-template-using-reactjs)