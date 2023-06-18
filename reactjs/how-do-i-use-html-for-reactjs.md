# How do I use HTML for ReactJS?
// plain

To use HTML for ReactJS, you need to use the React library and JSX syntax. JSX is an extension of the JavaScript language that allows you to write HTML directly within your JavaScript code. The React library then converts the JSX into HTML code that the browser can understand.

For example, the following code:

```
const element = <h1>Hello, world!</h1>;
ReactDOM.render(element, document.getElementById('root'));
```

will output the following HTML code:

```
<h1>Hello, world!</h1>
```

The code consists of two parts:
- The first part creates a React element with the HTML tag `<h1>` and the text `Hello, world!`.
- The second part renders the React element to the DOM using the `ReactDOM.render` method.

For further reading, you can check out the official React documentation on [JSX](https://reactjs.org/docs/introducing-jsx.html) and [Rendering Elements](https://reactjs.org/docs/rendering-elements.html).

onelinerhub: [How do I use HTML for ReactJS?](https://onelinerhub.com/reactjs/how-do-i-use-html-for-reactjs)