# How do I set a return value for a React.js function?
// plain

Setting a return value for a React.js function is a common task. To do this, you need to call the `return` keyword within the function body. This will specify the value that the function should return when it is called.

For example, the following code block defines a React.js function called `exampleFunction` that returns the string `"Hello World!"` when called:

```js
function exampleFunction() {
  return "Hello World!";
}
```

When called, this function will return the string `"Hello World!"`:

```js
console.log(exampleFunction()); // Output: "Hello World!"
```

The `return` keyword can also be used to return other types of values, such as objects, arrays, numbers, and booleans. For example, the following code block defines a React.js function called `exampleFunction2` that returns an object when called:

```js
function exampleFunction2() {
  return {
    message: "Hello World!",
    number: 42
  };
}
```

When called, this function will return an object with two properties, `message` and `number`:

```js
console.log(exampleFunction2()); // Output: { message: "Hello World!", number: 42 }
```

It is also possible to return the result of an expression or a function call. For example, the following code block defines a React.js function called `exampleFunction3` that returns the result of adding two numbers when called:

```js
function exampleFunction3(num1, num2) {
  return num1 + num2;
}
```

When called with two numbers, this function will return the result of adding them together:

```js
console.log(exampleFunction3(3, 4)); // Output: 7
```

## Helpful links
- [MDN - return](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/return)
- [React - Functions](https://reactjs.org/docs/functions.html)

onelinerhub: [How do I set a return value for a React.js function?](https://onelinerhub.com/reactjs/how-do-i-set-a-return-value-for-a-react-js-function)