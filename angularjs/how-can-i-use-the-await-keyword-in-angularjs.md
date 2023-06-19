# How can I use the await keyword in AngularJS?
// plain

The `await` keyword can be used in AngularJS to pause the execution of asynchronous functions. It is used to wait for the completion of a Promise before continuing with the rest of the code.

For example, the following code uses the `await` keyword to wait for the result of a Promise before logging a message to the console:
```
async function logMessage() {
  let result = await somePromise();
  console.log(result);
}
```

In the code above:
- `async` is a keyword that marks the function as asynchronous
- `somePromise()` is a function that returns a Promise
- `await` is used to pause the execution of the function until the Promise is resolved
- `result` is the result of the resolved Promise
- `console.log(result)` is used to log the result of the Promise to the console

## Helpful links
- [MDN: Async Function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)
- [MDN: await](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await)

onelinerhub: [How can I use the await keyword in AngularJS?](https://onelinerhub.com/angularjs/how-can-i-use-the-await-keyword-in-angularjs)