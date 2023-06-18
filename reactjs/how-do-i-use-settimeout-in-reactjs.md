# How do I use setTimeout in ReactJS?
// plain

`setTimeout` is a JavaScript function that allows you to execute code after a certain amount of time has elapsed. It is commonly used in ReactJS to delay the execution of a certain function.

## Example

```
function delayedGreeting() {
  alert("Hello!");
}

setTimeout(delayedGreeting, 3000);
```
## Output example

```
(after 3 seconds)
Hello!
```
The code above will execute the `delayedGreeting()` function after 3 seconds.

The code consists of the following parts:
1. `function delayedGreeting()` defines the function that will be executed after the timeout.
2. `setTimeout(delayedGreeting, 3000)` calls the `setTimeout` function, passing in the `delayedGreeting` function as the first argument and `3000` as the second argument. This will cause the `delayedGreeting` function to be executed after 3 seconds.

## Helpful links
- [MDN setTimeout reference](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/setTimeout)
- [React setTimeout example](https://reactjs.org/docs/faq-functions.html#what-if-i-need-to-setstate-with-a-value-from-an-asynchronous-call)

onelinerhub: [How do I use setTimeout in ReactJS?](https://onelinerhub.com/reactjs/how-do-i-use-settimeout-in-reactjs)